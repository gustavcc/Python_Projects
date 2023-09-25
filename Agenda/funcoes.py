import json
import os

agenda_json = 'C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos Python/Agenda/agenda.json'

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

def cadastro(agenda, id_contato):
    while True:
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" CADASTRO ":^60}\n{"-"*60}')
        print('''
1 - Continuar para cadastro.
0 - Voltar.''')
        opcao = input('\n→ ')
        if opcao:
            if opcao=='1':
                while True:
                    nome = input("Insira o nome da contato: ")
                endereco = input(f"Insira o endereço de {nome}: ")
                quant_tel = int(input(f"Deseja inserir quantos telefones para {nome}? ")) 
                lista_telefone = []  
                for i in range (quant_tel):  
                    telefone = input(f"Insira o {i+1}º telefone de {nome}: ")
                    lista_telefone.append(telefone)
                    agenda[nome] = [endereco, lista_telefone]
            if opcao=='0':
                break
            else:
                continue
        else:
            print("\nNão é válido 'Enter' como entrada\n")
    print(f'{"-"*60}\n{"- "*30}')
    return ""

def editar(agenda):
    print("---CONTATOS---")
    for cont in agenda.keys():
        print(cont)
    contato = input("Qual contato deseja editar? ")
    while True:
        print("""\n
        1. Nome
        2. Endereço
        3. Telefone""")
        resp = int(input("Que informação você deseja editar? "))
        while True:
            if resp==1 or resp==2 or resp==3:
                break
            else:
                print("Posição inexistente. Você pode escolher de 1 a 3")
                resp = int(input("Insira novamente a informação que você deseja editar: "))
        if resp == 1:
            nome = input("insira o novo nome: ")
            agenda[nome] = agenda.pop(contato)
        elif resp == 3:
            if len(agenda[contato][1]) >= 1:
                posicao_tel = int(input(f"""Você pode alterar os seguintes números --> {agenda[contato][1]}
                \nInsira a posição do telefone que deseja editar: """))
                tel_novo = input("Insira o novo telefone: ")
                for num in range(len(agenda[contato][1])):
                    if num == posicao_tel:
                        agenda[contato][1][posicao_tel] = tel_novo   
            elif len(agenda[contato][1]) == 0:
                while True:
                    resposta = input("Esse contato não possui número. Deseja inserir um número? s/n").lower()
                    if resposta == 's':
                        quant_tel = int(input(f"Deseja inserir quantos telefones para {nome}? ")) 
                        lista_telefone_nova = []  
                        for i in range (quant_tel):  
                            telefone = input(f"Insira o {i+1}º telefone de {nome}: ")
                            lista_telefone_nova.append(telefone)
                            agenda[contato] = [lista_telefone_nova, endereco]
        elif resp == 2:
            endereco = input("Insira o novo endereço: ")
            agenda[contato][0] = endereco
        break
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