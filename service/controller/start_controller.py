from flask import Response
from flask_restplus import Resource
import requests

from service.restplus import api

start = api.namespace("")


@start.route('/', methods=['GET'])
class StartController(Resource):
    @api.response(200, 'Enviado com sucesso.')
    def get(self) -> dict:
        """Welcome to AS Template Flask API."""
       
        return Response('aplicação funcionando')




