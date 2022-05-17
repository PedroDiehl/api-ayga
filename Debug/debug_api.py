'''

'''

import requests

BASE = "https://ayga-api.herokuapp.com/"

def debug_api():
    '''
    Função utilizada para reaizar chamadas a API com intuito de debugar os retornos.
    '''

    print("\nTestando GET")
    resposta = requests.get(f"{BASE}pedro")
    print(resposta)
    print(resposta.json())

    print("\nTestando POST")
    resposta = requests.post(f"{BASE}")
    print(resposta)
    print(resposta.json())

    return

if __name__ == "__main__":
    debug_api()