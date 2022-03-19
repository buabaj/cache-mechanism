from fastapi import APIRouter, HTTPException
from redis_config import r
from models import Product
import json

router = APIRouter()


@router.put("/update-product/{product_id}")
async def update_product(product_id: int, product: Product):
    if product.product_id == "":
        raise HTTPException(status_code=400, detail="Product ID is required")
    elif product.product_name == "":
        raise HTTPException(status_code=400, detail="Product Name is required")
    elif product.product_description == "":
        raise HTTPException(
            status_code=400, detail="Product Description is required")

    data = {"product_description": product.product_description,
            "product_name": product.product_name}
    data = json.dumps(data)

    if r.exists(product_id):
        r.set(product_id, data)
        return {"message": "Product updated successfully"}
    else:
        raise HTTPException(
            status_code=404, detail="Product ID does not exist")
