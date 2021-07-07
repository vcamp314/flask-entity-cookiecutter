from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import {{cookiecutter.entity_name|capitalize}}Interface


class {{cookiecutter.entity_name|capitalize}}(db.Model):
    """A {{cookiecutter.entity_name|capitalize}}"""

    __tablename__ = "{{cookiecutter.entity_name|lower}}"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    def update(self, changes: {{cookiecutter.entity_name|capitalize}}Interface):
        for key, val in changes.items():
            setattr(self, key, val)
        return
