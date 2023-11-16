from __future__ import annotations
from datetime import date, datetime

import re
from typing import Any, Dict, List, Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator


class Error(BaseModel):
    """
        Error - a model defined for errors in the API

        code: The code of this Error.
        message: The message of this Error.
    """

    code: int = Field(alias="code")
    message: str = Field(alias="message")

Error.update_forward_refs()
