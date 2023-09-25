from academia_funcoes import * # importando as funções que criamos
import os
import json # importa os aquivos onde vão ser armazenados as informações

clientes_json = "C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Academia/clientes.json"
avaliacoes_json = "C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Academia/avaliacoes.json"
exercicios_json = "C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos_Python/Academia/lista_exercicios.json"

while True:
    os.system("cls")
    opcao = menu() # mostra o menu de opções
    with open(clientes_json,"r",encoding="utf8") as arquivo:
        clientes = {} # criando o dicionário clientes a partir das informações armazernadas em clientes.json,
        # assim salva as informações e pode utilizalas mesmo se fechar o programa e sem ficar abrindo o arquivo
        cliente = json.load(arquivo)
        clientes = cliente
    with open(avaliacoes_json,"r",encoding="utf8") as arquivo:
        avaliacoes = {}# criando o dicionário avaliacoes a partir das informações armazernadas em avaliacoes.json,
        # assim salva as informações e pode utilizalas mesmo se fechar o programa e sem ficar abrindo o arquivo
        avaliacao = json.load(arquivo)
        avaliacoes = avaliacao
    with open(exercicios_json,"r",encoding="utf8") as arquivo:
        lista_exercicios = {}# criando o dicionário lista_exercicios a partir das informações armazernadas em lista_exercicios.json,
        # assim salva as informações e pode utilizalas mesmo se fechar o programa e sem ficar abrindo o arquivo
        lista = json.load(arquivo)
        lista_exercicios = lista

    if opcao == 1: # função dadastrar é usada
        id_cliente, id_avaliacao, id_lista_exercicio = 0,0,0,
        if not clientes.keys(): # definir o valor do id_cliente
            id_cliente = 0
        else:
            for contador1 in cliente.keys():
                id_cliente = int(contador1)
        if not avaliacoes.keys(): # definir o valor do id_avaliacao
            id_avaliacao = 0
        else:
            for contador2 in avaliacoes.keys():
                id_avaliacao = int(contador2)
        if not lista_exercicios.keys():
            id_lista_exercicio = 0
        else:
            for contador3 in lista_exercicios.keys():
                id_lista_exercicio = int(contador3)
        id_cliente += 1  
        id_avaliacao += 1 
        id_lista_exercicio += 1
        print(cadastrar(clientes, avaliacoes, lista_exercicios, id_cliente, id_avaliacao, id_lista_exercicio))
        print("\nAperte uma tecla para retornar...")
        input()
    elif opcao == 2: # função editar é usada
        print(editar(clientes, avaliacoes, lista_exercicios))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 3: # função excluir é usada
        print(excluir(clientes, avaliacoes, lista_exercicios))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 4: # função pesquisar é usada
        print(pesquisar(clientes, avaliacoes, lista_exercicios))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 5: # função listar é usada
        print(listar(clientes, avaliacoes, lista_exercicios))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 6: # função relatório é usada
        print(relatorio(clientes, avaliacoes, lista_exercicios))
        print("Aperte uma tecla para retornar...")
        input()
    elif opcao == 0: # opção que encerra o programa
        print(f"\n{'- '*30}")
        print("-"*60) # deixar bunito
        print("\nFim do programa -> sentiremos sua falta :(\n")
        print("-"*60) # deixar bunito
        print(f"{'- '*30}")
        break
    else: # caso for escolhido uma opção errada
        print("Rosponda corretamente: dentre as opções 1 ao 7")