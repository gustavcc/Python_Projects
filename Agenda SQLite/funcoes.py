import os
from sqlite3 import Error
from colorama import Fore
from time import sleep

def Menu():
    os.system('cls')
    print(f"{'-'*30}\n{'- '*15}\n{'Agenda':^30}\n{'- '*15}\n{'-'*30}")
    option = input('''
1 - Cadastrar contato
2 - Editar contato
3 - Excluir contato
4 - Mostrar lista de contatos
0 - Fechar agenda
\n→ ''')
    return option

def ContemNumber(string):
    for letter in string:
        if letter in ['1','2','3','4','5','6','7','8','9','0']:
            return True
        else: return False

def ContemString(string):
    string = string.lower()
    if 'a' <=string<= 'z':
        return True
    else: return False

def ContemEspecial(string):
    for letter in string:
        if letter in ['!','@','.','#','%','*','&',';']:
            return True
        else: return False

def CommitDB(connection,sql):
    c = connection.cursor()
    c.execute(sql)
    connection.commit()

def BuscarDB(connection,sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        result = c.fetchall()
        return result
    except Error as er:
        print(Fore.RED+'Erro de conexão: '+Fore.RESET,er)

def Cadastro(connection):    
    while True:
        os.system('cls')
        print(f"{'-'*30}\n{'- '*15}\n{'Cadastro':^30}\n{'- '*15}\n{'-'*30}")
        option = input('''
1 - Cadastrar contato
0 - Voltar ao Menu
\n→ ''')
        if option:
            if option=='1':
                resp='n'
                while resp=='n' or resp[0]=='n':
                    os.system('cls')
                    print(f"\n{'-'*30}")   
                    nome = input(f'\nInsira o nome\n→ ').capitalize().strip()
                    vSQL = '''SELECT * FROM Contatos'''
                    contatos = BuscarDB(connection,vSQL)
                    for contato in contatos:
                        if contato[1]==nome:
                            print(f'\n{nome} é um nome já existente!\n')
                            resp = input('\nDeseja continuar? (s/n)\n→ ').lower().strip()
                        else: resp='s'
                while True:
                    telefone = input(f'\nInsira o telefone de\nex: (00)0000 0000\n→ ')
                    if not ContemEspecial(telefone) and len(telefone)==13 and telefone[0]=='(' and telefone[3]==')' and telefone[8]==" ":
                        break
                    else:
                        print(Fore.RED+'\nInsira um telefone válido!\n'+Fore.RESET)
                        sleep(2)
                while True:
                    email = input(f'\nInsira o email de {nome}\nex: exemplo@agenda.com\n→ ')
                    if '@' in email and '.com' in email:
                        break
                    else:
                        print(Fore.RED+'\nInsira um email válido!\n')
                        sleep(2)
                
                vSQL = f'''INSERT INTO Contatos (nome,telefone,email)
                            VALUES('{nome}','{telefone}','{email}')'''
                try:
                    CommitDB(connection,vSQL)
                    print(Fore.GREEN+f'\n{nome} cadastrado com sucesso!\n'+Fore.RESET)
                    print('-'*30)
                    print('Aperte qualquer tecla para voltar...\n')
                    input()
                except:
                    print(Fore.RED+'\nErro de conexão... O contato não foi cadastrado!\n'+Fore.RESET)
                    sleep(2)
                continue
            elif option=='0':
                break
            else: 
                print(Fore.RED+'\nInsira uma opção válida!\n')
                sleep(2)
        else:
            print(Fore.RED+'\nInsira uma opção válida!\n')
            sleep(2)
    print('-'*30)
    print('Aperte qualquer tecla para voltar...\n')
    input()

def Editar(connection):
    os.system('cls')
    
    
    
    print('-'*30)
    print('Aperte qualquer tecla para voltar...\n')
    input()

def Excluir(connection):
    os.system('cls')
    print('Aperte qualquer tecla para voltar...')
    input()

def Mostrar(connection):
    os.system('cls')
    print('Aperte qualquer tecla para voltar...')
    input()
