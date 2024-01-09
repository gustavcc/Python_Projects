import os
import sqlite3
from sqlite3 import Error
from colorama import Fore

########## Criar conexão
def ConexaoBanco():
    path = "C:\\Users\\ritac\\OneDrive\\Documentos\\GitHub\\Python_Projects™\\Agenda_sqlite\\Agenda.db"
    connection = None
    try:
        connection=sqlite3.connect(path)
    except Error as er:
        print('Erro: ',er)
    return connection

vConection=ConexaoBanco()

#########! Criar tabela
# vSql='''CREATE TABLE Telefones(
#             id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome VARCHAR(40) NOT NULL,
#             telefone VARCHAR(14) NOT NULL,
#             email VARCHAR(40) NOT NULL
# );'''

# def criarTabela(connection,sql):
#     try:
#         c=connection.cursor()
#         c.execute(sql)
#         print('Tabela criada')
#     except Error as er:
#         print('Erro: ',er)
        
# criarTabela(vConection,vSql)

##########! Inserir dados
# nome = input('Nome\n=>')
# telefone = input('Telefone\n=>')
# email = input('Email\n=>')

# vsql = f'''INSERT INTO Contatos (nome,telefone,email)
#         VALUES('{nome}','{telefone}','{email}')
# '''
# def inserirDados(connection,sql):
#     try:
#         c=connection.cursor()
#         c.execute(sql)
#         connection.commit()
#         print('Registro inserido')
#     except Error as er:
#         print('Erro: ',er)

# inserirDados(vConection,vsql)