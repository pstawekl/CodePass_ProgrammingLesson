from __future__ import annotations
from datetime import date, datetime

import re
from typing import Any, Dict, List, Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator


class Information(BaseModel):
    """
        Information - a model defined for the API

        status: The status of this Information.
        affected: The affected of this Information.
        message: The message of this Information.
    """

    status: int = Field(alias="status")
    affected: int = Field(alias="affected")
    message: str = Field(alias="message")

Information.update_forward_refs()
