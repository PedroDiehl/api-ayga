'''
Função principal para armazenar a REST API desenvolvida como parte do
processo seletivo para developer backend da Ayga IOT.
Candidato: Pedro Henrique Diehl
'''


from flask import Flask, request
from flask_restful import Api, abort, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    '''
    teste teste teste
    '''

    def get(self, name):
        return {"data": name}

api.add_resource(HelloWorld, '/<string:name>')

if __name__ == "__main__":
    app.run(debug=False)