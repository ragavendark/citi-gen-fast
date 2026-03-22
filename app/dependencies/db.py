from app.core.database import Session_Local


def get_db():
    db = Session_Local()

    try:
        yield db
    finally:
        db.close()
