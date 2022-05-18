'''
Módulo utilizado para debugar o banco de dados e suas querys
'''

import json
import sqlite3

def create_db(db_file):
    '''
    Função para criar o banco de dados
    '''

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Create a table named signals with 4 columns
    # Column 1: ID
    # Column 2: date in the format YYYY-MM-DDTHH:MM:SS.SSSZ
    # Column 3: type
    # Column 4: value

    c.execute("CREATE TABLE signals (id INTEGER PRIMARY KEY, date TEXT, type TEXT, value TEXT)")

    conn.commit()
    conn.close()

    return

def debug_db(json_file):
    '''
    Função para administrar os comandos no banco de dados em debug
    '''

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

def menu_debugdb():
    '''
    Menu de terminal para escolher qual operação realizar
    '''

    print("\n-----------------------------\nEscolha o que deseja testar:\n-----------------------------\n")
    print("1 - Criar Banco de Dados")
    print("2 - Acessar debug")
    print("Outro - ENCERRAR\n")

    while True:
        escolha = input("Escolha: ")

        if escolha == "1":
            db_file = "B66db.sqlite"
            create_db(db_file)

        elif escolha == "2":
            debug_db("example_json.json")

        else:
            print("Encerrando...\n")
            break

    return

if __name__ == "__main__":
    menu_debugdb()