from fastapi import FastAPI
from app.api.v1.routes import order, product, user
from app.core.database import Base, engine
import app.models
app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
def greeting():
    return "Product management System"

app.include_router(user.router)
app.include_router(product.router)
app.include_router(order.router)