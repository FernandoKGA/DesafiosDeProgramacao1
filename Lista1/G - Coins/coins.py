# numero ilimitado de moedas de 1 a n
# voce que selecionar um conjunto que de o total de S
# eh permitido multiplas moedas com mesmo valor no conjunto
# qual eh o numero minimo para pegar a soma de S

#INPUT
# uma unica linha que contem n e S

#OUTPUT
# um inteiro com o numero minimo de moedas para obter a soma S
def transform(x):
    return int(x)

(n, S) = tuple(map(transform,input().split()))
conjuntoMoedas = list(range(1,n+1,1))
print(n, S)
