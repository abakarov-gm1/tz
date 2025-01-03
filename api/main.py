from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from routes.Auth import router as auth, get_user_from_token
from elastic import get_data, add_data_to_document, create_index
from services.productService import create_product

app = FastAPI()

app.include_router(auth, prefix="/auth", tags=["auth"])


@app.get("/")
def main():
    create_index()
    return HTMLResponse(content=open("static/index.html").read(), status_code=200)


class Product(BaseModel):
    name: str
    description: str
    price: int
    quantity: int


@app.post("/create-product")
def add_product(product: Product):
    create_product(
        product.name,
        product.description,
        product.price,
        product.quantity
    )
    add_data_to_document()
    return {"Status": "Success"}


@app.get("/search/products")
def get_product(query: str):
    return get_data(query)


@app.get("/indexing-data/products")
def index():
    add_data_to_document()
    return {"message": "данные добалены в индекс"}
