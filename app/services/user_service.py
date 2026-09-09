from sqlalchemy.orm import Session

from app.exceptions.handlers import AppError
from app.repositories import user_repository
from app.schemas.user_schema import UserCreate, UserUpdate


def create_user(db: Session, user_data: UserCreate):
    existing_user = user_repository.get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise AppError("Email already registered", 409)

    return user_repository.create_user(db, user_data)


def get_users(db: Session):
    return user_repository.get_all_users(db)


def get_user(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise AppError("User not found", 404)

    return user


def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):
    user = user_repository.get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise AppError("User not found", 404)

    user_with_email = user_repository.get_user_by_email(
        db,
        user_data.email
    )

    if user_with_email and user_with_email.id != user_id:
        raise AppError("Email already registered", 409)

    return user_repository.update_user(
        db,
        user,
        user_data
    )


def delete_user(db: Session, user_id: int):
    user = user_repository.get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise AppError("User not found", 404)

    user_repository.delete_user(db, user)

    return True

def get_user_courses(db: Session, user_id: int):
    user = user_repository.get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise AppError("User not found", 404)

    courses = []

    for enrollment in user.enrollments:
        courses.append(enrollment.course)

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at,
        "courses": courses
    }