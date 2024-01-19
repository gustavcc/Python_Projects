from funcoes import BuscarDB
import sqlite3
from sqlite3 import Error
from colorama import Fore
from time import sleep

def contem_especial(valor):
    especial = ['!','@','.','#','%','*','&',';']
    for letter in valor:
        if letter in especial:
            return True
    return False

def contem_letras(valor):
    for caractere in valor:
        if "a" <= caractere <= "z" or "A" <= caractere <= "Z":
            return True
    return False

while True:
    telefone = input(f'\nInsira o telefone de\nex: (00)0000 0000\n→ ')
    if contem_especial(telefone) or len(telefone)!=13 or telefone[0]!='(' or telefone[3]!=')' or telefone[8]!=" ":
        print(Fore.RED+'\nInsira um telefone válido!\n'+Fore.RESET)
        sleep(2)
    else: 
        break