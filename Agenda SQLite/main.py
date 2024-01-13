import os
import sqlite3
from sqlite3 import Error
from colorama import Fore

def ConnectionDB():
    path = "C:\\Users\\ritac\\OneDrive\\Documentos\\GitHub\\Python_Projects™\\Agenda SQLite\\Agenda.db"
    c = None
    try:
        c=sqlite3.connect(path)
    except Error as er:
        print('Erro: ',er)
    return c

vConnection=ConnectionDB()

