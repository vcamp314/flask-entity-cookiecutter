from typing import List

from app import db  # noqa
from .model import {{cookiecutter.entity_name|capitalize}}
from .interface import {{cookiecutter.entity_name|capitalize}}Interface


class {{cookiecutter.entity_name|capitalize}}Service:
    @staticmethod
    def get_all() -> List[{{cookiecutter.entity_name|capitalize}}]:
        return {{cookiecutter.entity_name|capitalize}}.query.all()

    @staticmethod
    def get_by_id({{cookiecutter.entity_name|lower}}_id: int) -> {{cookiecutter.entity_name|capitalize}}:
        return {{cookiecutter.entity_name|capitalize}}.query.get({{cookiecutter.entity_name|lower}}_id)

    @staticmethod
    def update({{cookiecutter.entity_name|lower}}: {{cookiecutter.entity_name|capitalize}}, {{cookiecutter.entity_name|lower}}_change_updates: {{cookiecutter.entity_name|capitalize}}Interface) -> {{cookiecutter.entity_name|capitalize}}:
        {{cookiecutter.entity_name|lower}}.update({{cookiecutter.entity_name|lower}}_change_updates)
        db.session.commit()
        return {{cookiecutter.entity_name|lower}}

    @staticmethod
    def delete_by_id({{cookiecutter.entity_name|lower}}_id: int) -> List[int]:
        {{cookiecutter.entity_name|lower}} = {{cookiecutter.entity_name|capitalize}}.query.filter({{cookiecutter.entity_name|capitalize}}.id == {{cookiecutter.entity_name|lower}}_id).first()
        if not {{cookiecutter.entity_name|lower}}:
            return []
        db.session.delete({{cookiecutter.entity_name|lower}})
        db.session.commit()
        return [{{cookiecutter.entity_name|lower}}_id]

    @staticmethod
    def create(new_attrs: {{cookiecutter.entity_name|capitalize}}Interface) -> {{cookiecutter.entity_name|capitalize}}:
        new_{{cookiecutter.entity_name|lower}} = {{cookiecutter.entity_name|capitalize}}(
            id=new_attrs["id"],
            name=new_attrs["name"],
            description=new_attrs["description"],
        )

        db.session.add(new_{{cookiecutter.entity_name|lower}})
        db.session.commit()

        return new_{{cookiecutter.entity_name|lower}}
