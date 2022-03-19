import uvicorn
from fastapi import FastAPI, Request
from routers import addProduct, getProduct, deleteProduct, updateProduct

app = FastAPI()
app.include_router(addProduct.router)
app.include_router(getProduct.router)
app.include_router(deleteProduct.router)
app.include_router(updateProduct.router)


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app)
