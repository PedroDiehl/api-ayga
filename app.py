'''
Função principal para armazenar a REST API desenvolvida como parte do
processo seletivo para developer backend da Ayga IOT.

Candidato: Pedro Henrique Diehl
'''


from flask import Flask, request
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET'])
def HelloWorld():
    '''
    teste teste teste
    '''

    return "beyblade"


