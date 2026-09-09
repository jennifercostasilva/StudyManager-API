from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EnrollmentCreate(BaseModel):
    user_id: int = Field(gt=0)
    course_id: int = Field(gt=0)


class EnrollmentResponse(BaseModel):
    id: int
    user_id: int
    course_id: int
    enrolled_at: datetime

    model_config = ConfigDict(from_attributes=True)