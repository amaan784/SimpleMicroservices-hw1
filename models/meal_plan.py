from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class MealPlanBase(BaseModel):
    meal_plan_id: UUID = Field(
        default_factory=uuid4,
        description="Persistent meal plan ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    name: str = Field(
        ...,
        description="Meal Plan name.",
        json_schema_extra={"example": "Unlimited 7 day"},
    )
    type: str = Field(
        ...,
        description="Meal Plan type.",
        json_schema_extra={"example": "swipes"},
    )
    cost: float = Field(
        ...,
        description="Cost of meal plan in USD.",
        json_schema_extra={"example": "1000"},
    )
    start_date: Optional[datetime] = Field(
        None,
        description="Meal plan official start date.",
        json_schema_extra={"example": "2025-09-14T00:00:00Z"},
    )
    end_date: Optional[datetime] = Field(
        None,
        description="Meal plan official end date.",
        json_schema_extra={"example": "2026-09-14T00:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "meal_plan_id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Unlimited 7 day",
                    "type": "swipes",
                    "cost": "1000",
                    "start_date": "2025-09-14T00:00:00Z",
                    "end_date": "2026-09-14T00:00:00Z",
                }
            ]
        }
    }


class MealPlanCreate(MealPlanBase):
    """Creation payload; ID is generated server-side but present in the base model."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "meal_plan_id": "11111111-1111-4111-8111-111111111111",
                    "name": "Unlimited 5 day",
                    "type": "swipes",
                    "cost": "800",
                    "start_date": "2025-08-15T00:00:00Z",
                    "end_date": "2026-08-15T00:00:00Z",
                }
            ]
        }
    }


class MealPlanUpdate(BaseModel):
    """Partial update; meal plan ID is taken from the path, not the body."""
    name: Optional[str] = Field(
        None,
        description="Meal Plan name.",
        json_schema_extra={"example": "Unlimited 7 day"},
    )
    type: Optional[str] = Field(
        None,
        description="Meal Plan type.",
        json_schema_extra={"example": "swipes"},
    )
    cost: Optional[float] = Field(
        None,
        description="Cost of meal plan in USD.",
        json_schema_extra={"example": "1000"},
    )
    start_date: Optional[datetime] = Field(
        None,
        description="Meal plan official start date.",
        json_schema_extra={"example": "09/14/2025"},
    )
    end_date: Optional[datetime] = Field(
        None,
        description="Meal plan official end date.",
        json_schema_extra={"example": "09/14/2026"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                  "name": "Unlimited 5 day",
                  "type": "swipes",
                  "cost": "800",
                  "start_date": "2025-08-15T00:00:00Z",
                  "end_date": "2026-08-15T00:00:00Z",
                },
                {"cost": "500"},
            ]
        }
    }


class MealPlanRead(MealPlanBase):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "meal_plan_id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Unlimited 7 day",
                    "type": "swipes",
                    "cost": "1000",
                    "start_date": "2025-08-15T00:00:00Z",
                    "end_date": "2026-08-15T00:00:00Z",
                    "created_at": "2025-08-15T10:20:30Z",
                    "updated_at": "2025-08-16T12:00:00Z",
                }
            ]
        }
    }
