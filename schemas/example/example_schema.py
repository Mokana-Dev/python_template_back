from pydantic import BaseModel
from typing import Optional


class ExampleCreateSchema(BaseModel):
    code: str
    name: str
    description: str
    price: str
    id_example_user_type: int


class ExampleUpdateSchema(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
