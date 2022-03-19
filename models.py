import imp
from pydantic import BaseModel


class Product(BaseModel):
    product_id: int
    product_description: str
    product_name: str
