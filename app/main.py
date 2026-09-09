from fastapi import FastAPI

from app.controllers import (
    course_controller,
    enrollment_controller,
    user_controller
)
from app.infrastructure.database import Base, engine
from app.models import course, enrollment, user


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="StudyManager API",
    description="API para gerenciamento de usuários, cursos e matrículas"
)


app.include_router(user_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)


@app.get("/")
def home():
    return {
        "message": "StudyManager API funcionando"
    }