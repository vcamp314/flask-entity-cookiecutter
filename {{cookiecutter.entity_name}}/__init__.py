from .model import {{cookiecutter.entity_name|capitalize}}
from .schema import {{cookiecutter.entity_name|capitalize}}Schema


def register_routes(root_api, root="/api"):
    from .controller import api as {{cookiecutter.entity_name|lower}}_api

    root_api.add_namespace({{cookiecutter.entity_name|lower}}_api, path=f"{root}/{{cookiecutter.entity_name|lower}}")
