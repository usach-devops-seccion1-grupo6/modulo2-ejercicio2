"""Archivo que contiene los endpoints"""
from flask import request, Blueprint
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.common.error_handling import ObjectNotFound
from .schemas import UsuarioSchema
from ..models import Usuario

usuarios_v1_0_bp = Blueprint('usuarios_v1_0_bp', __name__)
usuario_schema = UsuarioSchema()
api = Api(usuarios_v1_0_bp)


class UsuarioListResource(Resource):
    """Maneja los acciones para listar y agregar usuarios."""

    def get(self):
        """Permite listar un usuario"""
        usuarios = Usuario.get_all()
        result = usuario_schema.dump(usuarios, many=True)
        return result

    def post(self):
        """Permite agregar un usuario"""
        temp = request.get_json()
        try:
            data = usuario_schema.load(temp)

            usuario = Usuario.simple_filter_one(email=data['email'])
            if usuario:
                raise ObjectNotFound('El usuario ya existe')

        except ValidationError as err:
            raise ObjectNotFound(err.messages)

        usuario = Usuario(
            nombre=data['nombre'],
            email=data['email'],
            clave=data['clave']
        )

        usuario.save()
        resp = usuario_schema.dump(usuario)
        return resp, 201


class UsuarioResource(Resource):
    """Permite agregar un usuario"""

    def get(self, email):
        """Permite mostrar un usuario"""
        usuario = Usuario.simple_filter_one(email=email)
        if usuario is None:
            raise ObjectNotFound('El usuario no existe')

        resp = usuario_schema.dump(usuario)
        return resp

    def delete(self, email):
        """Permite eliminar un usuario"""
        usuario = Usuario.simple_filter_one(email=email)
        if usuario is None:
            raise ObjectNotFound('El usuario no existe')

        usuario.delete()
        return '', 204

    def put(self, email):
        """Permite modificar un usuario"""
        temp = request.get_json()
        try:
            temp['email'] = email
            data = usuario_schema.load(temp)

            usuario = Usuario.simple_filter_one(email=email)
            if usuario is None:
                raise ObjectNotFound('El usuario no existe')

        except ValidationError as err:
            raise ObjectNotFound(err.messages)

        usuario.nombre = data['nombre']
        usuario.clave = data['clave']

        usuario.update()
        return ''


api.add_resource(
    UsuarioListResource,
    '/api/v1.0/usuarios/',
    endpoint='usuario_list_resource')

api.add_resource(
    UsuarioResource,
    '/api/v1.0/usuarios/<string:email>',
    endpoint='usuario_resource')
