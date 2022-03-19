from fastapi import APIRouter, HTTPException
from models import Product
import json
from redis_config import r


router = APIRouter()


@router.post("/add-product")
async def add_product(product: Product):
    '''
    This endpoint will add a product to the database.
    '''
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

    # check if product id already exists
    if r.exists(product.product_id):
        raise HTTPException(
            status_code=400, detail="Product ID already exists")
    else:
        r.set(product.product_id, data)
        return {"message": "Product added successfully"}
