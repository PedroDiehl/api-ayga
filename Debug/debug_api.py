'''
Script Python utilizado para rodar comandos para debugar a API em desenvolvimento
'''


import itertools
import requests
import json
import logging

logging.basicConfig(filename='debug_api.log', encoding='utf-8', 
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', 
                    level=logging.DEBUG
                    )

#BASE = "http://127.0.0.1:5000/"
BASE = "https://ayga-api.herokuapp.com/"


def log_respostas(metodo, objetivo, resposta):
    '''
    Função utilizada para fazer o registro do erro em logs
    '''

    print(f"Testando {metodo} -> {objetivo}")

    logging.info(f"Resposta obtida - Método {metodo} -> Objetivo {objetivo}: {resposta}")
    try:
        logging.info(f"{resposta.json()}\n")
    except json.decoder.JSONDecodeError as err:
        logging.info(f"Erro no .json - Método {metodo}: {err}\n")

    return

def debug_api():
    '''
    Função utilizada para reaizar chamadas a API com intuito de debugar os retornos.
    '''

    metodos = ("GET", "POST")
    objetivos = ("GET", "POST")

    for metodo, objetivo in itertools.product(metodos, objetivos):
        if metodo == "GET" and objetivo == "GET":
            resposta = requests.get(f"{BASE}get_saved_data")

        elif metodo == "GET" and objetivo == "POST":
            resposta = requests.get(f"{BASE}post_data")

        elif metodo == "POST" and objetivo == "GET":
            resposta = requests.post(f"{BASE}get_saved_data")

        elif metodo == "POST" and objetivo == "POST":
            resposta = requests.post(f"{BASE}post_data")

        log_respostas(metodo, objetivo, resposta)

    return

if __name__ == "__main__":
    debug_api()
