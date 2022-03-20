import threading
import json


class CacheStorage:
    '''
    This Class is a slim implementation of a local cache storage using the dictionary approach.
    This cache storage has a built-in stale time of 5 minutes after which all items stored locally in cache expires and is rendered invalid.
    '''

    # set stale time to 5 minutes
    stale_time = 60*5
    cache = {}

    def set_interval_for_cache_invalidation(func, sec):
        '''
        This method sets an interval for recursively running the function to clear and invalidate the cache.
        '''
        def func_wrapper():
            CacheStorage.set_interval_for_cache_invalidation(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def clear_cache():
        '''
        This method clears items in the local cache storage and renders them invalid.
        '''
        CacheStorage.cache.clear()

    def set(self, id, data):
        '''
        This method adds a item that has been fetched from the Redis server to the local cache memory
        All items set to the local cache memory are rendered invalid after the stale time of 5 minutes.
        '''
        CacheStorage.cache[id] = data
        CacheStorage.set_interval_for_cache_invalidation(
            CacheStorage.clear_cache, CacheStorage.stale_time)

    def get(self, id):
        '''
        This method fetches existing items from the local cache storage.
        This prevents users from having to make requests over and over again to the database server but rather fetch cached items saved in memory.
        Caching helps save bandwith on database servers and makes the fetching of cached data relatively faster.
        '''
        data = CacheStorage.cache.get(id)
        name = data.get("product_name")
        description = data.get("product_description")
        return name, description

    def backup(self, id, data):
        '''This endpoint loads data that has been changed back to the local cache memory'''
        if id in CacheStorage.cache.keys():
            old_data = CacheStorage.cache.get(id)
            CacheStorage.cache.update({id: old_data, id: json.loads(data)})
        else:
            CacheStorage.set(id, data)


# print(cache)
