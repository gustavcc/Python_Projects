avaliacoes ={
    "1": {
        "altura": 70.0,
        "peso": 65.0,
        "gordura": 30.0,
        "bra\u00e7o": 20.0,
        "perna": 30.0,
        "cintura": 20.0,
        "data": "07/07/2023",
        "cliente": "1"
    }
}

clientes={
    "1": {
        "nome": "Gustavo",
        "idade": 17,
        "sexo": "M",
        "telefone": "(00)0000-0000",
        "status": "ativo"
    },
    "2": {
        "nome": "Rita",
        "idade": 45,
        "sexo": "F",
        "telefone": "(00)0000-0000",
        "status": "ativa"
    }
}

for key, value in avaliacoes.items():
    cliente = value['cliente']
    print(f"ID: {key} - CLIENTE: {cliente} - NOME: {clientes[cliente]['nome']}\n")