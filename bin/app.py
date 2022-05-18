'''
Script Python onde foi desenvolvida a REST API como parte do
processo seletivo para developer backend da Ayga IOT.
Candidato: Pedro Henrique Diehl
'''


import json
import sqlite3
from flask_restful import Api, Resource
from flask import Flask, request, jsonify

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect("B66db.db")
curs = conn.cursor()

class GetSavedData(Resource):
    '''
    Utilizada para retornar todos os dados salvos no banco de dados
    Método GET

    Retorna .json
    '''

    def get(self):
        '''
        
        '''

        with open("data_json.json", 'r') as f:
            data = json.load(f)

        return jsonify(data)

class PostData(Resource):
    '''
    Utilizada para receber os dados do dispositvo e salvar no banco de dados
    Método: POST

    Retorna {"status": "ok"}
    '''

    def post(self):

        dados = json.load(open(request.get_json()))
        sinais = dados[0]["signals"]
        for sinal in sinais:
            tipo = sinal["UUID"]

            for registro in sinal["logs"]:
                data = registro["date"]
                valor = registro["value"]

                # Inserção no banco de dados
                curs.execute("INSERT INTO signals (date, type, value) VALUES (?, ?, ?)", (data, tipo, valor))
                curs.commit()

        return {"status": "ok"}

api.add_resource(GetSavedData, "/get_saved_data")
api.add_resource(PostData, "/post_data")

if __name__ == "__main__":
    app.run(debug=False)
