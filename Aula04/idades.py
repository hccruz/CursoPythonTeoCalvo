# %%
idades = []

while True:
    idade = input("Digite a idade: ")
    
    if idade == "":
        break
    
    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print(f"Idades: {idades}")
print(f"Média: {media}")
print(f"Idade mínima: {minimo}")
print(f"Idade maxima: {maximo}")
print(f"Quantidade de idades: {qtde}")