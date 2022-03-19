from fastapi.testclient import TestClient
from app import app


client = TestClient(app)

# test index route for 200 status code


def test_index_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# test add product route for 200 status code


def test_add_product():
    response = client.post(
        "/add-product", json={"product_id": "69", "product_name": "rayban", "product_description": "a pair of sleek eyewear"})
    assert response.status_code == 200

# test add product with existing product id


def test_add_product_with_existing_id():
    response = client.post(
        "/add-product", json={"product_id": "69", "product_name": "rayban", "product_description": "a pair of sleek eyewear"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Product ID already exists"}

# test get product route for 200 status code


def test_get_product():
    response = client.get("/get-product/69")
    assert response.status_code == 200

# test get product with non-existing product id


def test_product_with_non_existing_id():
    response = client.get("/get-product/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product ID does not exist"}

# test update product route for 200 status code


def test_update_product():
    response = client.put("/update-product/69", json={
                          "product_id": "69", "product_name": "rayban", "product_description": "a pair of sleek glasses"})
    assert response.status_code == 200
    assert response.json() == {"message": "Product updated successfully"}

# test update product route with non existent id


def test_product_route_with_non_existent_id():
    response = client.put("/update-product/100", json={
                          "product_id": "100", "product_name": "rayban", "product_description": "a pair of sleek glasses"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Product ID does not exist"}

# test delete product with id


def test_delete_product():
    response = client.delete("/delete-product/69")
    assert response.status_code == 204
    assert response.json() == {"message": "Product successfully deleted"}

# test delete product with non-existent id


def test_delete_product_with_non_existent_id():
    response = client.delete("/delete-product/100")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product does not exist in database"}
