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

def contem_numbers(number):
    for letter in number:
        if letter in ['1','2','3','4','5','6','7','8','9','0']:
            return True
    return False

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
                while True:
                    os.system('cls')
                    print(f"\n{'-'*30}")   
                    nome = input(f'\nInsira o nome\n→ ').capitalize().strip()
                    vSQL = '''SELECT * FROM Contatos'''
                    contatos = BuscarDB(connection,vSQL)
                    for contato in contatos:
                        if contato[1]==nome:
                            print(Fore.BLUE+f'\n{nome} é um nome já existente!\n'+Fore.RESET)
                            resp = input('Deseja alterá-lo? (s/n)\n→ ').lower().strip()
                            break
                        else:
                            resp='n'
                            break
                    if resp=='s' or resp[0]=='s':
                        continue
                    else: break
                while True:
                    telefone = input(f'\nInsira o telefone de {nome}\nex: (00)0000 0000\n→ ')
                    if contem_especial(telefone) or len(telefone)!=13 or telefone[0]!='(' or telefone[3]!=')' or telefone[8]!=" ":
                        print(Fore.RED+'\nInsira um telefone válido!\n'+Fore.RESET)
                        sleep(2)
                    else: break
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
                    print('Aperte "ENTER" para continuar...\n')
                    input()
                except:
                    print(Fore.RED+'\nErro de conexão... O contato não foi cadastrado!\n'+Fore.RESET)
                    sleep(2)
                continue
            elif option=='0':
                break
            else: 
                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                sleep(2)
        else:
            print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
            sleep(2)
    print('-'*30)
    print('Aperte "ENTER" para voltar...\n')
    input()

def Editar(connection):
    while True:
        os.system('cls')
        
    
    
    
    print('-'*30)
    print('Aperte qualquer tecla para voltar...\n')
    input()

def Excluir(connection):
    while True:
        os.system('cls')
        print(f"{'-'*30}\n{'- '*15}\n{'Excluir':^30}\n{'- '*15}\n{'-'*30}")
        option = input('''
1 - Excluir contato
0 - Voltar ao Menu
\n→ ''')
        if option:
            if option=='1':
                os.system('cls')
                print('-'*30)
                nome = input(Fore.BLUE+'\nInsira o nome do contato que deseja excluir\n→ '+Fore.RESET).capitalize().strip()
                if nome:
                    vSQL = f'''SELECT * FROM Contatos WHERE nome="{nome}"'''
                    contatos = BuscarDB(connection,vSQL)
                    have = False
                    for cont in contatos:
                        if cont[1]==nome:   
                            have = True
                            print(f"\n{'-'*30}")
                            print(f"{'Contatos':^30}")
                            print('-'*30)
                            for contato in contatos:
                                print(f"\nID______ → {contato[0]}\nNome____ → {contato[1]}\nTelefone → {contato[2]}\nEmail___ → {contato[3]}")
                            break
                        else:
                            print(Fore.RED+f"\n{nome} não existe na base de dados!\n"+Fore.RESET)
                    if have:
                        while True:
                            try:
                                id_contato = int(input(Fore.BLUE+f"\nInsira o ID do contato que deseja excluir\n→ "+Fore.RESET))
                                for id_c in contatos:
                                    if id_c[1]==nome:
                                        if id_c[0]==id_contato:
                                            break
                                if id_c[0]==id_contato:
                                    break
                                else:
                                    print(Fore.RED+'\nEsse ID não existe!'+Fore.RESET)
                                sleep(2)
                            except ValueError:
                                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                                sleep(2)
                        resp='s'
                        while resp=='s':
                            resp = input(Fore.RED+f"\nRealmente deseja exlcluir esse contato? (s/n)\n→ "+Fore.RESET)
                            if resp:
                                if resp=='s' or resp[0]=='s':
                                    vSQL = f'''DELETE FROM Contatos  WHERE id_contato="{id_contato}"'''
                                    CommitDB(connection,vSQL)
                                    print(f"\n{'-'*30}")
                                    print(Fore.GREEN+f"Contato excluido com sucesso!"+Fore.RESET)
                                    print(f"{'-'*30}\n")
                                    break
                                else:
                                    resp='n'
                            else:
                                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                                sleep(2)
                        print('-'*30)
                        print('Aperte "ENTER" para continuar...\n')
                        input()
                    else:
                        print(Fore.RED+'\nEsse nome não existe!\n'+Fore.RESET)
                        print('-'*30)
                        print('Aperte "ENTER" para continuar...\n')
                        input()
                else:
                    print(Fore.RED+'\nNome inválido!\n'+Fore.RESET)
                    sleep(2)
            elif option=='0':
                break
            else:
                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                sleep(2)
        else:
            print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
            sleep(2)
    print('-'*30)
    print('Aperte "ENTER" para voltar...\n')
    input()

def Mostrar(connection):
    os.system('cls')
    print('Aperte qualquer tecla para voltar...')
    input()
