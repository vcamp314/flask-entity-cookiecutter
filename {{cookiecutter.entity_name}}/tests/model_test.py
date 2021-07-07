from pytest import fixture
from flask_sqlalchemy import SQLAlchemy

from app.test.fixtures import app, db  # noqa
from app.{{cookiecutter.entity_name|lower}}.model import {{cookiecutter.entity_name|capitalize}}


@fixture
def {{cookiecutter.entity_name|lower}}() -> {{cookiecutter.entity_name|capitalize}}:
    return {{cookiecutter.entity_name|capitalize}}(id=1, name="Test name", description="Test description")


def test_{{cookiecutter.entity_name|capitalize}}_create({{cookiecutter.entity_name|lower}}: {{cookiecutter.entity_name|capitalize}}):
    assert {{cookiecutter.entity_name|lower}}


def test_{{cookiecutter.entity_name|capitalize}}_retrieve({{cookiecutter.entity_name|lower}}: {{cookiecutter.entity_name|capitalize}}, db: SQLAlchemy):  # noqa
    db.session.add({{cookiecutter.entity_name|lower}})
    db.session.commit()
    s = {{cookiecutter.entity_name|capitalize}}.query.first()
    assert s.__dict__ == {{cookiecutter.entity_name|lower}}.__dict__
