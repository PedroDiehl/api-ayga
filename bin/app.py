'''
Script Python onde foi desenvolvida a REST API como parte do
processo seletivo para developer backend da Ayga IOT.

Candidato: Pedro Henrique Diehl
'''


from flask import Flask, request
from flask_restful import Api, abort, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

class TesteGET(Resource):
    '''
    TESTE GET
    '''

    def get(self, name):
        return {"data": name}

class TestePOST(Resource):
    '''
    TESTE POST
    '''

    def post(self):
        return {"data": "posted"}

api.add_resource(TesteGET, '/<string:name>')
api.add_resource(TestePOST, "/")

if __name__ == "__main__":
    app.run(debug=False)