'''
Módulo utilizado para debugar o banco de dados e suas querys
'''

import json

def debug_db(json_file):

    with open(json_file) as f:
        data = json.load(f)

    sinais = data[0]["signals"]
    sinal1 = sinais[0]
    sinal2 = sinais[1]

    data_sinal1 = sinal1["logs"][0]["date"]
    data_sinal2 = sinal2["logs"][0]["date"]

    print(data_sinal1)
    print(data_sinal2)

    print(type(data_sinal1))
    print(type(data_sinal2))
    
    print(data_sinal1.replace("Z", ""))
    print(data_sinal2.replace("Z", ""))

    return

if __name__ == "__main__":
    debug_db("example_json.json")