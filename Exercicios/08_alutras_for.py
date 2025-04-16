# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas

soma = 0 # Valor final

quant = 4 # contador de entradas

for i in range(quant):
    altura = input('Entre com a altura: ')
    altura = float(altura)
    soma += altura

print('Soma das alturas:', soma)