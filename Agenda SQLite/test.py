from funcoes import BuscarDB
import sqlite3
from sqlite3 import Error
from colorama import Fore
from time import sleep

def ContemEspecial(string):
    for letter in string:
        print(letter)
        if letter in ['!','@','.','#','%','*','&',';']:
            sleep(1)
            return True
        else: return False
        
while True:
                    telefone = input(f'\nInsira o telefone de\nex: (00)0000 0000\n→ ')
                    if not ContemEspecial(telefone) and len(telefone)==13 and telefone[0]=='(' and telefone[3]==')' and telefone[8]==" ":
                        break
                    else:
                        print(Fore.RED+'\nInsira um telefone válido!\n'+Fore.RESET)
                        sleep(2)