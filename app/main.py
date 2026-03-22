from fastapi import FastAPI
from app.api.v1.routes import order , product, user
 
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

main_app = FastAPI()


main_app.include_router(product.router)
main_app.include_router(order.router)
main_app.include_router(user.router)