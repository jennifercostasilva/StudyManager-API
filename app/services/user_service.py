from sqlalchemy.orm import Session

from app.repositories import user_repository
from app.schemas.user_schema import UserCreate, UserUpdate


def create_user(db: Session, user_data: UserCreate):
    existing_user = user_repository.get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise ValueError("Email already registered")

    return user_repository.create_user(db, user_data)


def get_users(db: Session):
    return user_repository.get_all_users(db)


def get_user(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise ValueError("User not found")

    return user


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise ValueError("User not found")

    user_with_email = user_repository.get_user_by_email(
        db,
        user_data.email
    )

    if user_with_email and user_with_email.id != user_id:
        raise ValueError("Email already registered")

    return user_repository.update_user(
        db,
        user,
        user_data
    )


def delete_user(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise ValueError("User not found")

    user_repository.delete_user(db, user)

    return True