from fastapi import FastAPI
from sqlalchemy import text

from app.schemas.user_schema import UserCreate
from app.schemas.course_schema import CourseCreate
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

@app.post("/test-user")
def test_user(user: UserCreate):
    return user

@app.post("/test-course")
def test_course(course: CourseCreate):
    return course