from pydantic import BaseModel
from typing import Any, Optional, Generic, TypeVar

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[str] = None