dicionario = {
    '1':{
        'nome': 'gustavo',
        'idade': 17
    },
    '2':{
        'nome': 'stefany',
        'idade': 17
    },
    '3':{
        'nome': 'rita',
        'idade': 17
    },
    '4':{
        'nome': 'gilberto',
        'idade': 17
    }
}

id = '4'

print('--------------------------------------')

list_keys = list(dicionario.keys())
print(list_keys)

if id != list_keys[-1]:
    dicionario.pop(id)
    novo_dicionario = {}    
    for key, value in dicionario.items():
        if int(key) >= int(id):
            novo_dicionario[str(int(key)-1)] = value
        else:
            novo_dicionario[key] = value
    print('--------------------------------------')
    print(novo_dicionario)
    print('--------------------------------------')
else:
    dicionario.pop(id)
    print('--------------------------------------')
    print(dicionario)
    print('--------------------------------------')
