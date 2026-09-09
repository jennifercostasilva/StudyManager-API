from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.schemas.user_schema import (
    UserCreate,
    UserCoursesResponse,
    UserResponse,
    UserUpdate
)
from app.services import user_service


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(
        db,
        user_data
    )


@router.get(
    "",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):
    return user_service.get_users(db)

@router.get(
    "/{user_id}/courses",
    response_model=UserCoursesResponse
)
def get_user_courses(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.get_user_courses(
        db,
        user_id
    )

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.get_user(
        db,
        user_id
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    return user_service.update_user(
        db,
        user_id,
        user_data
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user_service.delete_user(
        db,
        user_id
    )