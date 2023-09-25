import json
import os

agenda_json = 'C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Agenda/agenda.json'

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

def cadastro(agenda, id_contato):
    os.system('cls')
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
                        continue
                
                while True:
                    endereco = input(f"\nInsira o endereço de {nome}\n→ ").capitalize().strip()
                    if endereco:
                        especial = ['!','@','#','$','%','&',',','.',';']
                        diferente = False
                        for letra in nome:
                            if letra in especial:
                                diferente = True
                                break
                        if diferente:
                            print("\nO endereço não pode conter caracteres especiais!\n")
                        else:
                            break
                    else:
                        continue
                resp = 's'
                lista_telefone = []
                while resp[0] in 'sS':
                    telefone = input(f"\nInsira o telefone de {nome}\nex: (00)0000-0000\n→ ").strip()
                    if telefone:
                        if telefone[0]!='(' or telefone[3]!=')' or telefone[8]!='-' or len(telefone)!=13 or contem_letras(telefone):
                            print("\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!")
                    else:
                        continue
                    lista_telefone.append(telefone)
                    resp = input("\nDeseja adicionar outro telefone? (sim/não)\n→ ")
                agenda[id_contato] = {'nome': nome, 'endereço': endereco, 'telefone': lista_telefone}
                with open(agenda_json,'w', encoding='utf8') as arquivo:
                    json.dump(agenda,arquivo,indent=4)
                print("\nContatp cadastrado com sucesso!\n")
                break
            elif opcao=='0':
                break
            else:
                print('\nEscolha o valor numérico (1 ou 0)!\n')
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