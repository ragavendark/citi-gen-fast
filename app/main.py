from fastapi import FastAPI
from app.api.v1 import product
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(product.router)
