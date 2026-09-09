from sqlalchemy.orm import Session

from app.repositories import course_repository
from app.schemas.course_schema import CourseCreate, CourseUpdate


def create_course(db: Session, course_data: CourseCreate):
    return course_repository.create_course(db, course_data)


def get_courses(db: Session):
    return course_repository.get_all_courses(db)


def get_course(db: Session, course_id: int):
    course = course_repository.get_course_by_id(db, course_id)

    if not course:
        raise ValueError("Course not found")

    return course


def update_course(
    db: Session,
    course_id: int,
    course_data: CourseUpdate
):
    course = course_repository.get_course_by_id(db, course_id)

    if not course:
        raise ValueError("Course not found")

    return course_repository.update_course(
        db,
        course,
        course_data
    )


def delete_course(db: Session, course_id: int):
    course = course_repository.get_course_by_id(db, course_id)

    if not course:
        raise ValueError("Course not found")

    course_repository.delete_course(db, course)

    return True