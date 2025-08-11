# %%

import requests
import json
from tqdm import tqdm

import pandas as pd

# %%
ceps = [
        '09270110',
        '09270100',
        '09271100',
        '01519000',
        '09656000',
        '21870370',
        '14400760',
        '21645522',
        '09271110',
        '19060100',
        '58038200',
        '09270470'
    ]


url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv('ceps.csv', sep=';')

# %%
with open('ceps.json', 'w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
# %%
