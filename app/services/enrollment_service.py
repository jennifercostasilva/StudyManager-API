from sqlalchemy.orm import Session

from app.exceptions.handlers import AppError
from app.repositories import (
    course_repository,
    enrollment_repository,
    user_repository
)
from app.schemas.enrollment_schema import EnrollmentCreate


def create_enrollment(
    db: Session,
    enrollment_data: EnrollmentCreate
):
    user = user_repository.get_user_by_id(
        db,
        enrollment_data.user_id
    )

    if not user:
        raise AppError("User not found", 404)

    course = course_repository.get_course_by_id(
        db,
        enrollment_data.course_id
    )

    if not course:
        raise AppError("Course not found", 404)

    existing_enrollment = enrollment_repository.get_enrollment(
        db,
        enrollment_data.user_id,
        enrollment_data.course_id
    )

    if existing_enrollment:
        raise AppError(
            "User already enrolled in this course",
            409
        )

    return enrollment_repository.create_enrollment(
        db,
        enrollment_data
    )