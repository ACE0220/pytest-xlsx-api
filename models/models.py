from typing import List

from pydantic import BaseModel


class Case(BaseModel):
    id: str
    meta: dict[str, str]
    steps: List[dict]


class Suite(BaseModel):
    name: str
    cases: List[Case]


