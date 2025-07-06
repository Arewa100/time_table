from pydantic import BaseModel, Field
from datetime import datetime, timedelta, timezone
from typing import Optional


class Task(BaseModel):
    title: Optional[str] = None
    date_of_creation: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    day_of_task_execution: Optional[datetime] = None
    duration_of_task_execution: Optional[timedelta] = None
    task_content: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
        validate_assignment = True