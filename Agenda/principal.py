import json
from funcoes import *
import os

while True:

    agenda_json = 'C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Agenda/agenda.json'

    if not os.path.isfile(agenda_json):
        # Se o arquivo não existe, crie-o
        with open(agenda_json, 'w') as arquivo:
            arquivo.write('{}')
    with open(agenda_json,"r",encoding="utf8") as arquivo:
        agenda = {}
        arquivo_json = json.load(arquivo)
        agenda = arquivo_json

    os.system("cls")
    opcao = menu()
    os.system("cls")
    if opcao == '1':
        id_contato = 0
        if not agenda.keys(): # definir o valor do id
            id_contato = 0
        else:
            for id in agenda.keys():
                id_contato = int(id)
        id_contato += 1

        print(cadastro(agenda, id_contato))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '2':
        print(editar(agenda))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '3':
        print(excluir(agenda))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '4':
        print(pesquisar(agenda))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '5':
        print(ordem_adcionado(agenda))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '6':
        print("\n---ORDEM ALFABÉTICA---")
        for key in (ordem_abc(agenda)):
            print(key)
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == '0':
        print("Fim do programa\n")
        break
    else:
        print("\nResponda de acordo com as opções: 1 ao 6, ou 0\n")
        continue