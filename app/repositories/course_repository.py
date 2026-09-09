from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course_schema import CourseCreate, CourseUpdate


def create_course(db: Session, course_data: CourseCreate):
    course = Course(
        title=course_data.title,
        description=course_data.description,
        workload=course_data.workload
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


def get_all_courses(db: Session):
    return db.query(Course).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def update_course(db: Session, course: Course, course_data: CourseUpdate):
    course.title = course_data.title
    course.description = course_data.description
    course.workload = course_data.workload

    db.commit()
    db.refresh(course)

    return course


def delete_course(db: Session, course: Course):
    db.delete(course)
    db.commit()