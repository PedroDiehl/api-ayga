'''
Função utilizada para debugar o formato dos JSONs enviados ao servidor
'''

import json


def json_to_dict(json_file):
    '''
    Função para converter um arquivo JSON para um dicionário Python
    '''

    with open(json_file) as f:
        data = json.load(f)

    print("--------------------\nDADOS CRUS:\n--------------------\n")
    print(f"{data}\n")

    print("--------------------\n.JSON ENTRADA:\n--------------------\n")
    print(f"{data[0]}")

    print("--------------------\nPRIMEIRAS CHAVES:\n--------------------\n")
    print(f"{data[0].keys()}\n")

    print("--------------------\nDISPOSITIVO:\n--------------------\n")
    print(f'UUID: {data[0]["deviceUUID"]}\n')

    print("--------------------\nSINAIS DE DADOS:\n--------------------\n")
    sinais = data[0]["signals"]
    print(f"{len(sinais)} sinais dados")
    print(f"{sinais}\n")

    for index, sinal in enumerate(sinais):
        print(f"--------------------\nSINAL {index + 1}:\n--------------------")
        print(f"{sinal}\n")
        print(f'Dispositivo: {sinal["UUID"]}\n')

        print("Registros:\n")
        registros = sinal["logs"]
        for registro in registros:
            print(f'{registro}')
            print(f'Data: {registro["date"]}')
            print(f'Valor: {registro["value"]}\n')

    return

if __name__ == "__main__":
    json_to_dict("example_json.json")
