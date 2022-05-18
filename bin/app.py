'''
Script Python onde foi desenvolvida a REST API como parte do
processo seletivo para developer backend da Ayga IOT.
Candidato: Pedro Henrique Diehl
'''


import os
import psycopg2
from flask_restful import Api, Resource
from flask import Flask, request, jsonify


app = Flask(__name__)
api = Api(app)

def connect_db():
    '''
    Função para conectar ao banco de dados.
    '''

    try:
        conn = psycopg2.connect(os.environ.get('DATABASE_URL'))

    except psycopg2.OperationalError as conn_error:
        conn = None

    return conn

def selecionar_tipos(curs):
    '''
    Função para selecionar os tipos de sinais
    '''

    curs.execute("SELECT DISTINCT type FROM signals")
    tipos = curs.fetchall()

    return tuple(tipo[0] for tipo in tipos)

def create_json(signals):
    '''
    Função para criar o json a ser retornado
    '''

    return {"deviceUUID": "00000B66", "signals": signals}

class GetSavedData(Resource):
    '''
    Utilizada para retornar todos os dados salvos no banco de dados
    Método GET

    Retorna .json
    '''

    def get(self):

        if conn := connect_db():
            curs = conn.cursor()
        else:
            return jsonify({"error": "Não foi possível conectar ao banco de dados"})

        signals = []
        for tipo in selecionar_tipos(curs):

            # Seleciona data e valor onde o tipo é igual ao tipo atual
            # Try block for curs.execute() psycopg2 error
            curs.execute("SELECT date, value FROM signals WHERE type = %s", (tipo,))
            data = curs.fetchall()

            # Cria a lista de logs através de list compreenshion
            logs = [{"date": date, "value": value} for date, value in data]

            # Cria o dicionário de tipo de sinal e registros
            formato_json_sinais = {"UUID": tipo, "logs": logs}

            # Cria a lista de dicionários de tipo de sinal e registros
            signals.append(formato_json_sinais)

        return jsonify(create_json(signals))

class GetSavedDataByType(Resource):
    '''
    Utilizada para retornar os dados salvos no banco de dados com filtros
    Método GET

    Recebe como argumento o tipo do sinal que terá seus dados retornados
    Retorna .json
    '''

    def get(self, tipo):

        if conn := connect_db():
            curs = conn.cursor()
        else:
            return jsonify({"error": "Não foi possível conectar ao banco de dados"})

        if tipo in selecionar_tipos(curs):
            # Seleciona data e valor onde o tipo é igual ao tipo atual
            curs.execute("SELECT date, value FROM signals WHERE type = %s", (tipo,))
            data = curs.fetchall()

            # Cria a lista de logs através de list compreenshion
            logs = [{"date": date, "value": value} for date, value in data]

            # Cria o dicionário de tipo de sinal e registros
            formato_json_sinais = {"UUID": tipo, "logs": logs}

            return jsonify(create_json([formato_json_sinais]))

        else:
            return jsonify({"error": "Tipo de sinal não encontrado"})

class GetSavedDataByDate(Resource):
    '''
    Utilizada para retornar os dados salvos no banco de dados com filtros
    Método GET

    Recebe como argumento a data para retornar a coleta dos sinais
    Retorna .json
    '''

    def get(self, data_busca):

        if conn := connect_db():
            curs = conn.cursor()
        else:
            return jsonify({"error": "Não foi possível conectar ao banco de dados"})

        signals = []
        for tipo in selecionar_tipos(curs):

            # Seleciona data e valor onde o tipo é igual ao tipo atual
            # Try block for curs.execute() psycopg2 error
            try:
                curs.execute("SELECT date, value FROM signals WHERE type = %s AND date BETWEEN %s AND %s + INTERVAL '1 day'", (tipo, data_busca, data_busca))
            except psycopg2.errors.InvalidDatetimeFormat as invalid_dt_error:
                return jsonify({"error": "Formato de data inválido, correto: YYYY-MM-DDTHH:MM:SSZ"})

            data = curs.fetchall()

            # Cria a lista de logs através de list compreenshion
            logs = [{"date": date, "value": value} for date, value in data]

            # Cria o dicionário de tipo de sinal e registros
            formato_json_sinais = {"UUID": tipo, "logs": logs}

            # Cria a lista de dicionários de tipo de sinal e registros
            signals.append(formato_json_sinais)

        return jsonify(create_json(signals))

class GetSavedDataByDateInterval(Resource):
    '''
    Utilizada para retornar os dados salvos no banco de dados com filtros
    Método GET

    Recebe como argumentos o tipo do sinal e o intervalo de datas
    Retorna .json
    '''

    def get(self, tipo, data_inicio, data_fim):

        if conn := connect_db():
            curs = conn.cursor()
        else:
            return jsonify({"error": "Não foi possível conectar ao banco de dados"})

        if tipo in selecionar_tipos(curs):
            # Garante que a query não irá retornar em error
            try:
                curs.execute("SELECT date, value FROM signals WHERE type = %s AND date BETWEEN %s AND %s", (tipo, data_inicio, data_fim))
            except psycopg2.errors.InvalidDatetimeFormat as invalid_dt_error:
                return jsonify({"error": "Formato de data inválido, correto: YYYY-MM-DDTHH:MM:SSZ"})

            data = curs.fetchall()

            # Cria a lista de logs através de list compreenshion
            logs = [{"date": date, "value": value} for date, value in data]

            # Cria o dicionário de tipo de sinal e registros
            formato_json_sinais = {"UUID": tipo, "logs": logs}

            return jsonify(create_json([formato_json_sinais]))

        else:
            return jsonify({"error": "Tipo de sinal não encontrado"})

class PostData(Resource):
    '''
    Utilizada para receber os dados do dispositvo e salvar no banco de dados
    Método: POST

    Retorna {"status": "ok"}
    '''

    def post(self):

        if conn := connect_db():
            curs = conn.cursor()
        else:
            return jsonify({"error": "Não foi possível conectar ao banco de dados"})

        # Recebe os dados e faz a leitura
        dados = request.get_json()
        
        # Save any error to except err 
        try:
            for dado in dados:
                sinais = dado["signals"]

                # Filtra os dados e faz a inserção no banco de dados
                for sinal in sinais:
                    tipo = sinal["UUID"]

                    for registro in sinal["logs"]:
                        data = registro["date"]
                        valor = registro["value"]

                        # Inserção no banco de dados
                        curs.execute("INSERT INTO signals (date, type, value) VALUES (%s, %s, %s)", (data, tipo, valor))
                        conn.commit()

        except Exception as post_error:
            return jsonify({"status": "error", "message": "Falha na solicitação."})

        return jsonify({"status": "ok", "message": "Dados salvos com sucesso!"})

# Adiciona os recursos a API
api.add_resource(PostData, "/post_data")
api.add_resource(GetSavedData, "/get_saved_data")
api.add_resource(GetSavedDataByType, "/get_saved_data_by_type/<string:tipo>")
api.add_resource(GetSavedDataByDate, "/get_saved_data_by_date/<string:data_busca>")
api.add_resource(GetSavedDataByDateInterval, "/get_saved_data_by_date_interval/<string:tipo>/<string:data_inicio>/<string:data_fim>")


if __name__ == "__main__":
    app.run(debug=False)
