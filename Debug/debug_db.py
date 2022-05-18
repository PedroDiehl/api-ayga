'''
Módulo utilizado para debugar o banco de dados e suas querys
'''

import json
import sqlite3

JSON_FILE = "example_json.json"
DB_FILE = "debug_B66db.sqlite"
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

def create_db():
    '''
    Função para criar o banco de dados
    '''

    # Create a table named signals with 4 columns
    # Column 1: ID
    # Column 2: date in the format YYYY-MM-DDTHH:MM:SS.SSSZ
    # Column 3: type
    # Column 4: value

    c.execute('''CREATE TABLE signals 
                (id INTEGER PRIMARY KEY, 
                date TIMESTAMP, 
                type TEXT, 
                value TEXT)'''
                )

    conn.commit()

    print("Banco de dados criado com sucesso!\n")

    return


def test_insert():
    '''
    
    '''

    return

def search_query():
    '''
    
    '''

    return

def debug_db():
    '''
    Função para administrar os comandos no banco de dados em debug
    '''

    with open(JSON_FILE) as f:
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
    print("3 - Testar inserção")
    print("4 - Rodar Query")
    print("Outro - ENCERRAR\n")

    while True:
        escolha = input("Escolha: ")

        if escolha == "1":
            create_db()

        elif escolha == "2":
            debug_db()

        elif escolha == "3":
            test_insert()

        elif escolha == "4":
            search_query()

        else:
            print("Encerrando...\n")
            break

    conn.close()
    return

if __name__ == "__main__":
    menu_debugdb()