from __future__ import annotations
from datetime import date, datetime

import re
from typing import Any, Dict, List, Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator


class Object(BaseModel):
    """
        Object - a model defined for the API

        id: The id of this Object.
        description: The description of this Object.
        value: The value of this Object.
    """

    id: str = Field(alias="id")
    description: str = Field(alias="description")
    value: str = Field(alias="value")

    @validator("id")
    def id_pattern(cls, value):
        assert value is not None and re.match(r"^.{0,20}", value)
        return value

    @validator("description")
    def description_pattern(cls, value):
        assert value is not None and re.match(r"^.{0,40}", value)
        return value

    @validator("value")
    def value_pattern(cls, value):
        assert value is not None and re.match(r"^.{0,20}", value)
        return value

Object.update_forward_refs()
