import pymysql as sql
from pymysql import  Error

def conectar(host, nomeuser, senha):
    conectado = None
    try:
        conectado = sql.connect(host=host, user=nomeuser, passwd=senha)
        print("Conectado com sucesso")
    except Error as erro:
        print(f"Erro {erro}")

    return conectado

def executarQuery(coneccao, query):
    cursor = coneccao.cursor()
    try:
        cursor.execute(query)
        coneccao.commit()
        print("Exito")
    except Error as erro:
        print(erro)




if __name__ == '__main__':
    coneccao = conectar('localhost', 'root', 'root')

    executarQuery(coneccao, 'use jennaortega')









