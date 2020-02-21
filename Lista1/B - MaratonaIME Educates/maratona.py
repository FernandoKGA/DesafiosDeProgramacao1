import math
import functools

def transform(x):
    return int(x)

n = int(input())
qtdPessoas = map(transform,input().split())
i = 0
qtdTotal = functools.reduce(lambda x, y: x+y, qtdPessoas)
valorTotalPorCarro = 5
qtdCarros = math.ceil(qtdTotal/valorTotalPorCarro)
print(qtdCarros)
