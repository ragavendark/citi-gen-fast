from fastapi import FastAPI
from api.v1.routes import users

# Create Fast Api Instance
app = FastAPI()


# we will enable rest api endpoint at localhost:8000/
@app.get("/")
def read_root():
    return {"message": "Hello World"}


# health check endpoint
@app.get("/health")
def health_check():
    return {"status": "Ok"}


app.include_router(users.router, prefix="/api/v1")
