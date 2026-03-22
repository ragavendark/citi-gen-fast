from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Session_Local = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()
