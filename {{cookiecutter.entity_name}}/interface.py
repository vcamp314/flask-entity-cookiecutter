from datetime import datetime
from typing import TypedDict


class {{cookiecutter.entity_name|capitalize}}Interface(TypedDict, total=False):
    id: int
    name: str
    description: str
