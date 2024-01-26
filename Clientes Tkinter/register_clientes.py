import tkinter as tk
import sqlite3
from sqlite3 import Error
import pandas as pd

def Connection():
    path = "clientes.db"
    c = None
    try:
        c = sqlite3.connect(path)
    except Error as er:
        print("\nErro: ",er)
    finally:
        return c

# função que define a criação do DB e da tabela
# def CriarTabela():
#     connection = Connection()
#     try:
#         vsql = '''CREATE TABLE Clientes(
#                         id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
#                         nome TEXT,
#                         sobrenome TEXT,
#                         telefone TEXT,
#                         email TEXT
#  );'''
#         c = connection.cursor()
#         c.execute(vsql)
#         connection.commit()
#         print('\nTabela Criada\n')
#     except Error as er:
#         print("\nErro: ",er)
# CriarTabela()

#* Funções
def cadastrar_cliente():
    connection = Connection()
    try:
        c = connection.cursor()
        c.execute(f"INSERT INTO Clientes (nome,sobrenome,telefone,email) VALUES('{Entry_nome.get()}','{Entry_sobrenome.get()}','{Entry_telefone.get()}','{Entry_email.get()}');")
        connection.commit()
        print("\nCliente castrado")
        Entry_nome.delete(0, "end")
        Entry_sobrenome.delete(0, "end")
        Entry_email.delete(0, "end")
        Entry_telefone.delete(0, "end")
    except Error as er:
        print("\nErro: ",er)

def exportar_cliente():
    pass

#* Interface Gráfica
window = tk.Tk()

# titulo
window.title('Cadastro de Clientes')

# labels
Label_nome = tk.Label(window, text='Nome')
Label_nome.grid(row=0, column=0, padx=10, pady=10)

Label_sobrenome = tk.Label(window, text='Sebrenome')
Label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

Label_email = tk.Label(window, text='Email')
Label_email.grid(row=2, column=0, padx=10, pady=10)

Label_telefone = tk.Label(window, text='Telefone')
Label_telefone.grid(row=3, column=0, padx=10, pady=10)

# entrys
Entry_nome = tk.Entry(window, text='Nome', width=30)
Entry_nome.grid(row=0, column=1, padx=10, pady=10)

Entry_sobrenome = tk.Entry(window, text='Sebrenome', width=30)
Entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

Entry_email = tk.Entry(window, text='Email', width=30)
Entry_email.grid(row=2, column=1, padx=10, pady=10)

Entry_telefone = tk.Entry(window, text='Telefone', width=30)
Entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# buttons
Entry_cadastrar = tk.Button(window, text='Cadastrar Cliente', command = cadastrar_cliente)
Entry_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

Entry_exportar = tk.Button(window, text='Exportar Cliente Excel', command = exportar_cliente)
Entry_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

window.mainloop()