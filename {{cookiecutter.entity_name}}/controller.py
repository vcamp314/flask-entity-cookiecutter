from flask_restx import Resource
from flask import request
from flask_restx import Namespace
from flask_accepts import accepts, responds
from flask.wrappers import Response
from typing import List

from .schema import {{cookiecutter.entity_name|capitalize}}Schema
from .model import {{cookiecutter.entity_name|capitalize}}
from .service import {{cookiecutter.entity_name|capitalize}}Service

api = Namespace("{{cookiecutter.entity_name|capitalize}}", description="{{cookiecutter.entity_name|capitalize}} information")


@api.route("/")
class {{cookiecutter.entity_name|capitalize}}Resource(Resource):
    """{{cookiecutter.entity_name|capitalize}}s"""

    @responds(schema={{cookiecutter.entity_name|capitalize}}Schema(many=True))
    def get(self) -> List[{{cookiecutter.entity_name|capitalize}}]:
        """Get all {{cookiecutter.entity_name|capitalize}}s"""

        return {{cookiecutter.entity_name|capitalize}}Service.get_all()

    @accepts(schema={{cookiecutter.entity_name|capitalize}}Schema, api=api)
    @responds(schema={{cookiecutter.entity_name|capitalize}}Schema)
    def post(self):
        """Create a Single {{cookiecutter.entity_name|capitalize}}"""

        return {{cookiecutter.entity_name|capitalize}}Service.create(request.parsed_obj)


@api.route("/<int:id>")
@api.param("id", "{{cookiecutter.entity_name|capitalize}} database ID")
class {{cookiecutter.entity_name|capitalize}}IdResource(Resource):
    @responds(schema={{cookiecutter.entity_name|capitalize}}Schema)
    def get(self, id: int) -> {{cookiecutter.entity_name|capitalize}}:
        """Get Single {{cookiecutter.entity_name|capitalize}}"""

        return {{cookiecutter.entity_name|capitalize}}Service.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single {{cookiecutter.entity_name|capitalize}}"""

        from flask import jsonify

        id = {{cookiecutter.entity_name|capitalize}}Service.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema={{cookiecutter.entity_name|capitalize}}Schema, api=api)
    @responds(schema={{cookiecutter.entity_name|capitalize}}Schema)
    def put(self, id: int) -> {{cookiecutter.entity_name|capitalize}}:
        """Update Single {{cookiecutter.entity_name|capitalize}}"""

        changes = request.parsed_obj
        {{cookiecutter.entity_name|lower}} = {{cookiecutter.entity_name|capitalize}}Service.get_by_id(id)
        return {{cookiecutter.entity_name|capitalize}}Service.update({{cookiecutter.entity_name|lower}}, changes)
