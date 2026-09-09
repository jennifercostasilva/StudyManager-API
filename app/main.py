from fastapi import FastAPI
from sqlalchemy import text

from app.infrastructure.database import Base, SessionLocal, engine
from app.models import course, enrollment, user


Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def home():
    return {"message": "StudyManager API"}


@app.get("/database-test")
def database_test():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "message": "Conexão com o banco funcionando"
        }
    finally:
        db.close()