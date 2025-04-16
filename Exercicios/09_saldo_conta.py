'''
Faça um programa que receba uma quantidade indefinida de valores correspondentes 
a “saldo em conta”, mas quando o usuário apertar “enter” sem digitar valor algum, 
o programa para de receber valores, e exibe a soma de todos os valores digitados anteriormente.
'''

saldo_total = 0 # Saldo Final

while True:
    saldo = input('Entre com o saldo: ')
    if saldo == '':
        break
    saldo_total += float(saldo) # Soma do Saldo total mais o saldo informado

print('Saldo Total =',saldo_total)
