import json
import os
from colorama import Fore
from time import sleep

# agenda_json = 'C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Agenda/agenda.json'

def contem_letras(valor):
    for caractere in valor:
        if 'a' <= caractere <= 'z' or 'A' <= caractere <= 'Z':
            return True
    return False

def menu():
    print(f"\n{'- '*30}")
    print(f'{"-"*60}\n{" AGENDA ":^60}\n{"-"*60}')
    print("""
1 - Cadastrar contato.
2 - Editar um contato.
3 - Excluir um contato.
4 - Pesquisar contato pelo 'Nome'.
5 - Classificar por ordem de contatos cadastrados.
6 - Classificar contatos ordenados pelos nomes.
0 - Encerrar programa.""")
    while True:
        opcao = input("\n→ ")
        if opcao:
            return opcao
        else:
            print("\nNão é válido 'Enter' como entrada")

def cadastro(agenda, id_contato, agenda_json):
    while True:
        os.system('cls')
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" CADASTRO ":^60}\n{"-"*60}')
        print('''
1 - Continuar para cadastro.
0 - Sair.''')
        opcao = input('\n→ ')
        if opcao:
            if opcao=='1':
                while True:
                    nome = input("\nInsira o nome\n→ ").capitalize().strip()
                    if nome:
                        especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                        diferente = False
                        for letra in nome:
                            if letra in especial:
                                diferente = True
                                break
                        if diferente:
                            print("\nO nome não pode conter números e caracteres especiais!\n")
                        else:
                            break
                    else:
                        print("\nNão é válido valor vazio\n")
                
                while True:
                    endereco = input(f"\nInsira o endereço de {nome}\n→ ").capitalize().strip()
                    if endereco:
                        especial = ['!','@','#','$','%','&',',','.',';']
                        diferente = False
                        for letra in endereco:
                            if letra in especial:
                                diferente = True
                                break
                        if diferente:
                            print("\nO endereço não pode conter caracteres especiais!\n")
                        else:
                            break
                    else:
                        print("\nNão é válido valor vazio\n")
                resp = 's'
                lista_telefone = []
                while resp[0] in 'sS':
                    telefone = input(f"\nInsira o telefone de {nome}\nex: (00)0000-0000\n→ ").strip()
                    if telefone:
                        if telefone[0]!='(' or telefone[3]!=')' or telefone[8]!='-' or len(telefone)!=13 or contem_letras(telefone):
                            print("\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!")
                        else:
                            break
                    else:
                        print("\nNão é válido valor vazio\n")
                    lista_telefone.append(telefone)
                    resp = input("\nDeseja adicionar outro telefone? (sim/não)\n→ ")
                agenda[id_contato] = {'nome': nome, 'endereço': endereco, 'telefone': lista_telefone}
                with open(agenda_json,'w', encoding='utf8') as arquivo:
                    json.dump(agenda,arquivo,indent=4)
                print("\nContato cadastrado com sucesso!\n")
            elif opcao=='0':
                break
            else:
                print('\nEscolha um valor numérico (1 ou 0)!\n')
        else:
            print("\nNão é válido valor vazio\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""

def editar(agenda, agenda_json):
    while True:
        os.system('cls')
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" EDITAR ":^60}\n{"-"*60}')
        print('''
1 - Continuar para editar.
0 - Sair.''')
        opcao = input("\n→ ")
        if opcao:
            if opcao=='1':
                if not agenda:
                    os.system('cls')
                    print(f'\n{"-"*60}')
                    print(Fore.RED+"Não há clientes!"+Fore.RESET)
                    print(f'{"-"*60}\n')
                    break
                else:
                    while True:
                        print(f'\n{"-"*60}\n{"CONTATOS":^60}\n{"-"*60}') # ! contatos disponíveis
                        for id,contato in agenda.items():
                            print(f"ID: {id} → NOME: {contato['nome']}")
                        id = input("\nInsira o ID do contato que desejar\n→ ")
                        if id:
                            if id in agenda.keys():
                                while True:
                                    print("""
1 - Nome
2 - Endereço
3 - Telefone
0 - Sair
""")
                                    opcao_editar = input(f'\nInsira o que deseja editar de {agenda[id]["nome"]}\n→ ').lower().strip()
                                    if opcao_editar:
                                        if opcao_editar == '1' or opcao_editar[0] == 'n':
                                            while True:
                                                novo_nome = input("\nInsira o novo nome\n→ ").capitalize().strip()
                                                if novo_nome:
                                                    especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                                                    diferente = False
                                                    for letra in novo_nome:
                                                        if letra in especial:
                                                            diferente = True
                                                            break
                                                    if diferente:
                                                        print("\nO nome não pode conter números e caracteres especiais!\n")
                                                    else:
                                                        break
                                                else:
                                                    continue
                                            agenda[id]['nome'] = novo_nome
                                            with open(agenda_json, 'w', encoding="utf-8") as arquivo:
                                                json.dump(agenda,arquivo,indent=4)
                                            print(f"\nO nome foi alterado com sucesso!\n")
                                            sleep(3)
                                            break
                                        if opcao_editar =='2' or opcao_editar[0] == 'e':
                                            while True:
                                                novo_endereco = input(f"\nInsira o novo endereço de {agenda[id]['nome']}\n→ ").capitalize().strip()
                                                if novo_endereco:
                                                    especial = ['!','@','#','$','%','&',',','.',';']
                                                    diferente = False
                                                    for letra in novo_endereco:
                                                        if letra in especial:
                                                            diferente = True
                                                            break
                                                    if diferente:
                                                        print("\nO endereço não pode conter caracteres especiais!\n")
                                                    else:
                                                        break
                                                else:
                                                    continue
                                            agenda[id]['endereço'] = novo_endereco
                                            with open(agenda_json, 'w', encoding="utf-8") as arquivo:
                                                json.dump(agenda,arquivo,indent=4)
                                            print(f"\nO endereço foi alterado com sucesso!\n")
                                            sleep(3)
                                            break
                                        if opcao_editar == '3' or opcao_editar[0] == 't':
                                            if len(agenda[id]['telefone']) > 1:
                                                while True:
                                                    print(f"\n{agenda[id]['nome']} possui os seguintes telefones:")
                                                    codigos = []
                                                    for i, numero in enumerate(agenda[id]['telefone']):
                                                        codigos.append(i)
                                                        print(f"Código: {i} - {numero}")
                                                    opcao_telefone = input("\nQuer editar qual telefone? (insira o código)\n→ ")
                                                    if opcao_telefone:
                                                        if int(opcao_telefone) in codigos:
                                                            novo_telefone = input(f"\nInsira o novo telefone de {agenda[id]['nome']}\nex: (00)0000-0000\n→ ").strip()
                                                            while True:
                                                                if novo_telefone:
                                                                    if novo_telefone[0]!='(' or novo_telefone[3]!=')' or novo_telefone[8]!='-' or len(novo_telefone)!=13 or contem_letras(novo_telefone):
                                                                        print("\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!")
                                                                    else:
                                                                        break
                                                                else:
                                                                    print("\nNão é válido valor vazio\n")
                                                            agenda[id]['telefone'][int(opcao_telefone)] = novo_telefone
                                                            with open(agenda_json, 'w', encoding="utf-8") as arquivo:
                                                                json.dump(agenda,arquivo,indent=4)
                                                            print(f"\nO telefone foi alterado com sucesso!\n")
                                                            sleep(3)
                                                            break
                                                        else:
                                                            print("\nInsira um código válido\n")
                                                    else:
                                                        print("\nNão é válido valor vazio\n")
                                            else:
                                                while True:
                                                    novo_telefone = input(f"\nInsira o novo telefone de {agenda[id]['nome']}\nex: (00)0000-0000\n→ ").strip()
                                                    if novo_telefone:
                                                        if novo_telefone[0]!='(' or novo_telefone[3]!=')' or novo_telefone[8]!='-' or len(novo_telefone)!=13 or contem_letras(novo_telefone):
                                                            print("\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!")
                                                        else:
                                                            break
                                                    else:
                                                        print("\nNão é válido valor vazio\n")
                                                agenda[id]['telefone'][0] = novo_telefone
                                                with open(agenda_json, 'w', encoding="utf-8") as arquivo:
                                                    json.dump(agenda,arquivo,indent=4)
                                                print(f"\nO telefone foi alterado com sucesso!\n")
                                                sleep(3)
                                                break
                                            break
                                        if opcao_editar == '0':
                                            break
                                        else:
                                            print("\nInsira um ID válido\n")
                                    else:
                                        print("\nNão é válido valor vazio\n")
                                break
                            else:
                                print("\nEsse contato não existe\n")
                        else:
                            print("\nNão é válido valor vazio\n")
            if opcao == '0':
                break
            else:
                print('\nEscolha um valor numérico (1 ou 0)!\n')
        else:
            print("\nNão é válido valor vazio\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""

def excluir(agenda):
    print("\n---CONTATOS---")
    for cont in agenda.keys():
        print(cont)
    contato = input("Insira o contato que deseja excluir: ")
    agenda.pop(contato)
    return agenda

def pesquisar(agenda):
    print("\n---CONTATOS---")
    for cont in agenda.keys():
        print(cont)
    contato = input("Insira o contato que deseja  pesquisar: \n")
    for k, v in agenda.items():
        if k == contato:
            print(f'---{k.upper()}---')
            for values in v:
                print(f"{values}")
        else:
            print("Esse contato não existe")
    
def ordem_adcionado(agenda):
    print("\n---ORDEM DE ADICIONADOS---")
    for k, v in (agenda.items()):
        print(f'{k} --> {v}')

def ordem_abc(agenda):
    abc = []
    for contato in agenda.keys():
        abc.append(contato)
    abc.sort()
    return abc