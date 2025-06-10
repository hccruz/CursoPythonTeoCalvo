# %%

def juros_compostos(aporte: int, taxa: float, ano: int)->float:
    '''
    juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para  cálculo do valor.

aporte:
    um número inteiro, que representa o valor em R$
    
taxa:
    um número float entre 0 e 1 que representa o valor taxa de juros

ano:
    um número inteiro que representa o tempo que o valor ficou rendendo
    '''
    return aporte * (1 + taxa) ** ano

# %%
juros_compostos(taxa=0.13, ano=4, aporte=1000)
# %%
juros_compostos(taxa=0.10, ano=5, aporte=1000)
# %%
