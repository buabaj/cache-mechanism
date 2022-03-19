from fastapi import APIRouter, HTTPException
import json
from redis_config import r
from CacheMechanism.cache import CacheStorage

cache_storage = CacheStorage()
print('cache storage at initial run of server', CacheStorage.cache)

router = APIRouter()


@router.get("/get-product/{product_id}")
async def get_product(product_id: int):
    if product_id not in CacheStorage.cache.keys():
        # check if data exists in redis
        if r.exists(product_id):
            data = r.get(product_id)
            data = json.loads(data)

            cache_storage.set(id=product_id, data=data)
            print('from db', CacheStorage.cache)
            return {"product_id": product_id,
                    "product_description": data["product_description"],
                    "product_name": data["product_name"]}
        else:
            raise HTTPException(
                status_code=404, detail="Product ID does not exist")
    else:
        # get data from cache
        name, description = cache_storage.get(product_id)
        print('from cache', CacheStorage.cache)
        return {"product_id": product_id,
                "product_description": description,
                "product_name": name}
