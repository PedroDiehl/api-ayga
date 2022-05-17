'''
Script Python utilizado para rodar comandos para debugar a API em desenvolvimento
'''


from ast import While
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

    print(f"Testando {metodo} -> {objetivo}\n")

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

    print("\n-----------------------------\nEscolha o que deseja testar:\n-----------------------------\n")
    print("1 - GET -> GET")
    print("2 - GET -> POST")
    print("3 - POST -> GET")
    print("4 - POST -> POST")
    print("Outro - ENCERRAR\n")

    while True:
        escolha = input("Escolha: ")

        if escolha == "1":
            resposta = requests.get(f"{BASE}get_saved_data")
            metodo = "GET"
            objetivo = "GET"

        elif escolha == "2":
            resposta = requests.get(f"{BASE}post_data")
            metodo = "GET"
            objetivo = "POST"

        elif escolha == "3":
            resposta = requests.post(f"{BASE}get_saved_data")
            metodo = "POST"
            objetivo = "GET"

        elif escolha == "4":
            resposta = requests.post(f"{BASE}post_data")
            metodo = "POST"
            objetivo = "POST"

        else:
            print("Encerrando...\n")
            break

        log_respostas(metodo, objetivo, resposta)

    return

if __name__ == "__main__":
    debug_api()
