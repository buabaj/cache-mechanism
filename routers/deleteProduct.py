from fastapi import APIRouter, HTTPException
from redis_config import r


router = APIRouter()


@router.delete("/delete-product/{product_id}", status_code=204)
async def delete_product(product_id: int):
    if r.exists(product_id):
        r.delete(product_id)
        return {'message': 'Product successfully deleted'}
    else:
        raise HTTPException(
            status_code=404, detail='Product does not exist in database')
