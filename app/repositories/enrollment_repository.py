from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment
from app.schemas.enrollment_schema import EnrollmentCreate


def create_enrollment(db: Session, enrollment_data: EnrollmentCreate):
    enrollment = Enrollment(
        user_id=enrollment_data.user_id,
        course_id=enrollment_data.course_id
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment


def get_enrollment(
    db: Session,
    user_id: int,
    course_id: int
):
    return (
        db.query(Enrollment)
        .filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id
        )
        .first()
    )


def get_enrollments_by_user(db: Session, user_id: int):
    return (
        db.query(Enrollment)
        .filter(Enrollment.user_id == user_id)
        .all()
    )