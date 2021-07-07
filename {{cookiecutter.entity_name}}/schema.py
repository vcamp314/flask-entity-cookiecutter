from app import ma
from .model import {{cookiecutter.entity_name|capitalize}}


class {{cookiecutter.entity_name|capitalize}}Schema(ma.SQLAlchemyAutoSchema):
    """{{cookiecutter.entity_name|capitalize}}"""

    class Meta:
        model = {{cookiecutter.entity_name|capitalize}}
