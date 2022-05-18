'''
Módulo utilizado para debugar o banco de dados e suas querys
'''

import json
import sqlite3

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

    print("Banco de dados criado com sucesso!\n")

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

    print("Dados inseridos com sucesso!\n")

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
    print("Outro - ENCERRAR\n")

    while True:
        escolha = input("Escolha: ")

        if escolha == "1":
            create_db()
        elif escolha == "2":
            test_insert()
        elif escolha == "3":
            print(f'{curs.execute("SELECT * FROM signals").fetchall()}\n')
            print("Busca geral realizada com sucesso!\n")

        elif escolha == "4":
            curs.execute("DELETE FROM signals")
            print("Tabela limpa com sucesso!\n")

        elif escolha == "5":
            print(f"{curs.execute('SELECT DISTINCT type FROM signals ORDER BY type').fetchall()}\n")
            print("Busca por tipo realizada com sucesso!\n")

        else:
            print("Encerrando...\n")
            break

        conn.commit()

    conn.close()
    return

if __name__ == "__main__":
    menu_debugdb()