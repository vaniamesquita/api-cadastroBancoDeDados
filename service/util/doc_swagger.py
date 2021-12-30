
from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'id': fields.List(fields.Integer(), required=True),
    'nome': fields.List(fields.String(), required=True, description= "Digite seu nome"),
    'sobrenome': fields.List(fields.String(), required=True, description= "Digite seu sobrenome"),
    'estado': fields.List(fields.String(), required=True, description= "Digite seu estado") })

