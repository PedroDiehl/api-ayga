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

    print(data)
    print(data.keys())
    print(data["deviceUUID"])
    print(data["signals"])
    print(len(data["signals"]))
    print(data["signals"][0].keys())
    print(data["signals"][0]["UUID"])
    print(f'{data["signals"][0]["logs"]}\n')

    print("--------------------\nLOGS DE TEMPERATURA:\n--------------------\n")
    for log in data["signals"][0]["logs"]:
        print(log)
        print(log["date"])
        print(log["value"])
        print()
    return

if __name__ == "__main__":
    json_to_dict("example_json.json")
