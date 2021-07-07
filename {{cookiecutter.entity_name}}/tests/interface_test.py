from pytest import fixture

from app.{{cookiecutter.entity_name|lower}}.model import {{cookiecutter.entity_name|capitalize}}
from app.{{cookiecutter.entity_name|lower}}.interface import {{cookiecutter.entity_name|capitalize}}Interface


@fixture
def interface() -> {{cookiecutter.entity_name|capitalize}}Interface:

    params: {{cookiecutter.entity_name|capitalize}}Interface = {
        "id": 1,
        "name": "Test name",
        "description": "Test description",
    }
    return params


def test_{{cookiecutter.entity_name|capitalize}}Interface_create(interface: {{cookiecutter.entity_name|capitalize}}Interface):
    assert interface


def test_{{cookiecutter.entity_name|capitalize}}Interface_works(interface: {{cookiecutter.entity_name|capitalize}}Interface):
    assert {{cookiecutter.entity_name|capitalize}}(**interface)
