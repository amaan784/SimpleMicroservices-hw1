from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class DiningLocationBase(BaseModel):
    dining_location_id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Dining Location ID (server-generated).",
        json_schema_extra={"example": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb"},
    )
    name: str = Field(
        ...,
        description="Dining Location name.",
        json_schema_extra={"example": "Grace Dodge"},
    )
    capacity: int = Field(
        ...,
        description="Dining Location capacity.",
        json_schema_extra={"example": "200"},
    )


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "dining_location_id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "name": "Grace Dodge",
                    "capacity": "200",
                }
            ]
        }
    }


class DiningLocationCreate(DiningLocationBase):
    """Creation payload; ID is generated server-side but present in the base model."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "dining_location_id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "name": "Grace Dodge",
                    "capacity": "200",
                }
            ]
        }
    }


class DiningLocationUpdate(BaseModel):
    """Partial update; Dining Location ID is taken from the path, not the body."""
    name: Optional[str] = Field(
        None,
        description="Dining Location name.",
        json_schema_extra={"example": "Grace Dodge"},
    )
    capacity: Optional[int] = Field(
        None,
        description="Dining Location capacity.",
        json_schema_extra={"example": "200"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Grace Dodge",
                    "capacity": "200",
                },
                {"capacity": "500"},
            ]
        }
    }


class DiningLocationRead(DiningLocationBase):
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
                    "dining_location_id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "name": "Grace Dodge",
                    "capacity": "200",
                    "created_at": "2025-08-15T10:20:30Z",
                    "updated_at": "2025-08-16T12:00:00Z",
                }
            ]
        }
    }