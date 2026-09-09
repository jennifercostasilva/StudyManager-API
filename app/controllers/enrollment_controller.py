from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.schemas.enrollment_schema import (
    EnrollmentCreate,
    EnrollmentResponse
)
from app.services import enrollment_service


router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post(
    "",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_enrollment(
    enrollment_data: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    return enrollment_service.create_enrollment(
        db,
        enrollment_data
    )