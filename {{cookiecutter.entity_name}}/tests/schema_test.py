from pytest import fixture

from app.{{cookiecutter.entity_name|lower}}.model import {{cookiecutter.entity_name|capitalize}}
from app.{{cookiecutter.entity_name|lower}}.schema import {{cookiecutter.entity_name|capitalize}}Schema
from app.{{cookiecutter.entity_name|lower}}.interface import {{cookiecutter.entity_name|capitalize}}Interface


@fixture
def schema() -> {{cookiecutter.entity_name|capitalize}}Schema:
    return {{cookiecutter.entity_name|capitalize}}Schema()


def test_{{cookiecutter.entity_name|capitalize}}Schema_create(schema: {{cookiecutter.entity_name|capitalize}}Schema):
    assert schema


def test_{{cookiecutter.entity_name|capitalize}}Schema_works(schema: {{cookiecutter.entity_name|capitalize}}Schema):
    params: {{cookiecutter.entity_name|capitalize}}Interface = schema.load(
        {"id": 1, "name": "Test name", "description": "Test description"}
    )
    {{cookiecutter.entity_name|lower}} = {{cookiecutter.entity_name|capitalize}}(**params)

    assert {{cookiecutter.entity_name|lower}}.id == 1
    assert {{cookiecutter.entity_name|lower}}.name == "Test name"
    assert {{cookiecutter.entity_name|lower}}.description == "Test description"
