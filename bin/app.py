'''
Script Python onde foi desenvolvida a REST API como parte do
processo seletivo para developer backend da Ayga IOT.
Candidato: Pedro Henrique Diehl
'''


import json
import sqlite3
from flask import Flask, request
from flask_restful import Api, Resource

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

        tipos = curs.execute("SELECT DISTINCT type FROM signals").fetchall()

        signals = []
        for tipo in tipos:

            # Seleciona data e valor onde o tipo é igual ao tipo atual
            data = curs.execute("SELECT date, value FROM signals WHERE type = :tipo", {"tipo": tipo[0]}).fetchall()

            # Cria a lista de logs através de list compreenshion
            logs = [{"date": date, "value": value} for date, value in data]

            # Cria o dicionário de tipo de sinal e registros
            formato_json_sinais = {"UUID": tipo[0], 
                                    "logs": logs}

            # Cria a lista de dicionários de tipo de sinal e registros
            signals.append(formato_json_sinais)

        # Cria o dicionário de dados do dispositivo
        formato_json = {"deviceUUID": "00000B66",
                        "signals": signals}

        return formato_json

class PostData(Resource):
    '''
    Utilizada para receber os dados do dispositvo e salvar no banco de dados
    Método: POST

    Retorna {"status": "ok"}
    '''

    def post(self):

        # Recebe os dados e faz a leitura
        dados = json.load(open(request.get_json()))
        sinais = dados[0]["signals"]

        # Filtra os dados e faz a inserção no banco de dados
        for sinal in sinais:
            tipo = sinal["UUID"]

            for registro in sinal["logs"]:
                data = registro["date"]
                valor = registro["value"]

                # Inserção no banco de dados
                curs.execute("INSERT INTO signals (date, type, value) VALUES (?, ?, ?)", (data, tipo, valor))
                curs.commit()

        return {"status": "ok"}

# Adiciona os recursos a API
api.add_resource(GetSavedData, "/get_saved_data")
api.add_resource(PostData, "/post_data")

if __name__ == "__main__":
    app.run(debug=False)
