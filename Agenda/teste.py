import json
from funcoes import *
import os

agenda_json = 'C:/Users/ritac/OneDrive/Documentos/GitHub/Projetos Python/Agenda/agenda.json'

if not os.path.isfile(agenda_json):
    # Se o arquivo não existe, crie-o
    with open(agenda_json, 'w') as arquivo:
        arquivo.write('{}')

with open(agenda_json,"r",encoding="utf8") as arquivo:
    agenda = {}
    arquivo_json = json.load(arquivo)
    agenda = arquivo_json


with open(agenda_json,'w') as agenda_arquivo:
    json.dump(agenda, agenda_arquivo, indent=4)