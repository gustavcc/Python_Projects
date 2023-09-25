def menu():
    print("""
        1. Cadastrar os 10 empregados;
        2. Editar um empregado.
        3. Excluir um empregado;
        4. Classificar os registros por número de matrícula.
        5. Pesquisar um determinado empregado pelo número de matrícula.
        6. Pesquisar um determinado empregado pelo nome.
        7. Apresentar de forma ordenada os registros dos empregados que
        recebem salários acima de 1000.
        8. Apresentar de forma ordenada os registros dos empregados que
        recebem salários abaixo a 1000.
        9. Apresentar de forma ordenada os registros dos empregados que
        recebem salários iguais a 1000.
        10. Sair do programa cadastro.""")
    resposta = int(input("\nInsira qual dessas opções voçê quer executar: \n"))
    return resposta

def cadastro(funcionarios):
    for fun in range(2):
        matricula = input("Insira a matricula do funcionário: ")
        nome = input(f"Insira o nome do funcionário de matricula  {matricula}: ")
        salario = float(input(f"Insira o salário de {nome}: "))
        funcionarios[matricula] = [nome, salario]
    return funcionarios

def editar(funcionarios):
    print("---EMPREGADOS---")
    for fun in funcionarios.keys():
        print(fun)
    while True:
        empregado = input("Qual empregado deseja editar? ")
        if empregado in funcionarios:
            break
        else:
            print(f"Esse empregado não existe. Você só pode escolher esses: ")
            for fun in funcionarios.keys():
                print(fun)
    while True:
        print("""\n
        1. Matrícula
        2. Nome
        3. Salário""")
        resp = int(input("Que informação você deseja editar? "))
        while True:
            if resp==1 or resp==2 or resp==3:
                break
            else:
                print("Posição inexistente. Você pode escolher de 1 a 3")
                resp = int(input("Insira novamente a informação que você deseja editar: "))
        if resp == 1:
            matricula_nova = input("insira a nova matrícula: ")
            funcionarios[matricula_nova] = funcionarios.pop(empregado)
        elif resp == 2:
            nome = input("insira o novo nome: ")
            funcionarios[empregado][0] = nome
        elif resp == 3:
            salario = input("Insira o novo salário: ")
            funcionarios[empregado][1] = salario
        break
    return funcionarios

def excluir(funcionarios):
    print("\n---EMPREGADOS---")
    for fun in funcionarios.keys():
        print(fun)
    while True:
        empregado = input("Insira o empregado que deseja excluir: ")
        if empregado in funcionarios:
            funcionarios.pop(empregado)
            print(funcionarios)
            break
        else:
            print(f"Esse funcionario nao foi cadastrado. Você só pode escolher esses: ")
            for fun in funcionarios.keys():
                print(fun)
    funcionarios.pop(empregado)
    return funcionarios
    
def classificar_matricula(funcionarios):
    print("\n---CLASSIFICAR POR MATRICULA---")
    for key, value in (funcionarios.items()):
        print(f'{key} --> {value}')

def pesquisar_matricula(funcionarios):
    print("\n---EMPREGADOS---")
    for fun, valor in funcionarios.items():
        print(f"{fun} --> {valor[0]}")
    empregado = input("Insira a matrícula do empregado: \n")
    for matricula in funcionarios.keys():
        while True:
            if matricula == empregado:
                print(f'{matricula}')
                break
            else:
                print("Esse contato não existe. Você só pode escolher esses: ")
                for fun in funcionarios.keys():
                    print(fun)

def pesquisar_nome(funcionarios):
    list = []
    print("\n---EMPREGADOS---")
    for fun in funcionarios.keys():
        if funcionarios[fun][0]:
            list.append(fun)
            print(fun)
    empregado = input("Insira o empregado que deseja  pesquisar pelo nome: \n")
    for matricula, valor in funcionarios.items():
        while True:
            if funcionarios[fun][0] == empregado:
                print(f"{valor[0]} --> matricula: {matricula} e salario: {valor[1]}")
                break
            else:
                print("Esse contato não existe. Você só pode escolher esses: ")
                for fun in funcionarios.keys():
                    if funcionarios[fun][0]:
                        print(fun)

def ordem_salario_maior1000(funcionarios):
    for matricula, valor in sorted(funcionarios.items()):
        if valor[1] > 1000:
            print(f"{matricula} --> nome: {valor[0]} e salario: {valor[1]}")

def ordem_salario_menor1000(funcionarios):
    for matricula, valor in sorted(funcionarios.items()):
        if valor[1] < 1000:
            print(f"{matricula} --> nome: {valor[0]} e salario: {valor[1]}")

def ordem_salario_igual1000(funcionarios):
    for matricula, valor in funcionarios.items():
        if valor[1] == 1000:
            print(f"{matricula} --> nome: {valor[0]} e salario: {valor[1]}")
