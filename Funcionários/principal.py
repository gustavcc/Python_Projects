from time import sleep

import secundario

funcionarios = {}
while True:
    resposta = secundario.menu()
    if resposta == 1:
        print(secundario.cadastro(funcionarios))
        sleep(3)
    elif funcionarios != {}:
        if resposta == 2:
            print(secundario.editar(funcionarios))
            sleep(3)
        elif resposta == 3:
            print(secundario.excluir(funcionarios))
            sleep(3)
        elif resposta == 4:
            print(secundario.classificar_matricula(funcionarios))
            sleep(3)
        elif resposta == 5:
            print(secundario.pesquisar_matricula(funcionarios))
            sleep(3)
        elif resposta == 6:
            print(secundario.pesquisar_nome(funcionarios))
            sleep(3)
        elif resposta == 7:
            print(secundario.ordem_salario_maior1000(funcionarios))
            sleep(3)
        elif resposta == 8:
            print(secundario.ordem_salario_menor1000(funcionarios))
            sleep(3)
        elif resposta == 9:
            print(secundario.ordem_salario_igual1000(funcionarios))
            sleep(3)
        elif resposta == 10:
            print("Fim do programa\n")
            break
        else:
            print("Rosponda corretamente: dentre as opções 1 ao 10")
    else:
        print("Listav vazia")
        continue