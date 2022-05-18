'''
Módulo utilizado para debugar o banco de dados e suas querys
'''


import json
import sqlite3
from flask import jsonify

JSON_FILE = "example_json.json"
DB_FILE = "debug_B66db.db"
conn = sqlite3.connect(DB_FILE)
curs = conn.cursor()

def create_db():
    '''
    Função para criar o banco de dados
    '''

    # Create a table named signals with 4 columns
    # Column 1: ID
    # Column 2: date in the format YYYY-MM-DDTHH:MM:SS.SSSZ
    # Column 3: type
    # Column 4: value

    curs.execute('''CREATE TABLE signals 
                (id INTEGER PRIMARY KEY, 
                date TIMESTAMP, 
                type TEXT, 
                value TEXT)'''
                )

    return

def test_insert():
    '''
    Teste para inserir dados no banco de dados
    '''

    sinais = json.load(open(JSON_FILE))[0]["signals"]

    with open(JSON_FILE) as f:
        data = json.load(f)

    sinais = data[0]["signals"]
    for sinal in sinais:
        tipo = sinal["UUID"]

        for registro in sinal["logs"]:
            data = registro["date"]
            valor = registro["value"]

            curs.execute("INSERT INTO signals (date, type, value) VALUES (?, ?, ?)", (data, tipo, valor))

    return

def test_json_data():
    '''
    Teste para serealizar os dados para retornar no .json
    '''

    # Seleciona os tipos de sinais
    tipos = curs.execute("SELECT DISTINCT type FROM signals").fetchall()

    signals = []
    for tipo in tipos:
        #print(tipo[0])

        # Seleciona data e valor onde o tipo é igual ao tipo atual
        data = curs.execute("SELECT date, value FROM signals WHERE type = :tipo", {"tipo": tipo[0]}).fetchall()

        logs = [{"date": date, "value": value} for date, value in data]

        formato_json = {"UUID": tipo[0], 
                        "logs": logs
                        }

        signals.append(formato_json)

    #print(signals)

    format_json = {"deviceUUID": "00000B66",
                    "signals": signals}

    print(format_json)
    print(json.dumps(format_json, indent=4))
    print(jsonify(format_json))

    return

def menu_debugdb():
    '''
    Menu de terminal para escolher qual operação realizar
    '''

    print("\n-----------------------------\nEscolha o que deseja testar:\n-----------------------------\n")
    print("1 - Criar Banco de Dados")
    print("2 - Testar inserção")
    print("3 - Testar busca geral")
    print("4 - Limpar tabela")
    print("5 - Testar busca por tipo de sinal")
    print("6 - Testar busca por data")
    print("7 - Testar formatar .json")
    print("Outro - ENCERRAR\n")

    while True:
        escolha = input("Escolha: ")

        if escolha == "1":
            create_db()
            print("Banco de dados criado com sucesso!\n")

        elif escolha == "2":
            test_insert()
            print("Dados inseridos com sucesso!\n")

        elif escolha == "3":
            print(f'{curs.execute("SELECT * FROM signals").fetchall()}\n')
            print("Busca geral realizada com sucesso!\n")

        elif escolha == "4":
            curs.execute("DELETE FROM signals")
            print("Tabela limpa com sucesso!\n")

        elif escolha == "5":
            print(f"{curs.execute('SELECT DISTINCT type FROM signals ORDER BY type').fetchall()}\n")
            print("Busca por tipo realizada com sucesso!\n")

        elif escolha == "6":
            print(f"{curs.execute('SELECT DISTINCT date FROM signals ORDER BY date').fetchall()}\n")
            print("Busca por data realizada com sucesso!\n")

        elif escolha == "7":
            test_json_data()
            print("Teste de .json realizado com sucesso!\n")

        else:
            print("Encerrando...\n")
            break

        conn.commit()

    conn.close()
    return

if __name__ == "__main__":
    menu_debugdb()