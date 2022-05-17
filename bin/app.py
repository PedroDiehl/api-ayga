'''
Script Python onde foi desenvolvida a REST API como parte do
processo seletivo para developer backend da Ayga IOT.
Candidato: Pedro Henrique Diehl
'''


import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_restful import Api, abort, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class GetSavedData(Resource):
    '''
    Utilizada para retornar todos os dados salvos no banco de dados
    Método GET

    Retorna .json
    '''

    def get(self):

        with open("data_json.json", 'r') as f:
            data = json.load(f)

        return data

class PostData(Resource):
    '''
    Utilizada para receber os dados do dispositvo e salvar no banco de dados
    Método: POST

    Não retorna nada
    '''

    def post(self):
        #print(request)
        #print(type(request))
        #print(request.form)
        with open("data_json.json", "w") as outfile:
            json.dump(request.get_json(), outfile, indent=4)

        return {"status": "ok"}


api.add_resource(GetSavedData, "/get_saved_data")
api.add_resource(PostData, "/post_data")

if __name__ == "__main__":
    app.run(debug=False)
