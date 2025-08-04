# %%
nome_arquivo = 'historia.txt'


open_file = open(nome_arquivo)
# %%
print(open_file)
# %%
conteudo = open_file.read()
# %%
print(conteudo)
# %%
open_file.close()
# %%
arquivo = 'data.csv'

with open(arquivo) as open_file:
    data = open_file.readlines()

for linhas in data:
    print(linhas)
    
# %%

dados = dict()

chaves = data[0].strip('\n').split(';')
for c in chaves:
    dados[c] = []

dados
# %%
for linha in data[1:]:
    valores = linha.strip('\n').split(';')
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

print(dados)
# %%
idades = []

for i in dados['idade']:
    idades.append(int(i))

media = sum(idades) / len(idades)
media