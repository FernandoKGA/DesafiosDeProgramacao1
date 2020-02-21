# input n segmentos
# cada segmento tem (1 <= li <= ri <= m)
# considere todos os pontos entre 1 e m inclusive
# print todos os pontos QUE NAO PERTENCEM ao segmento
# o ponto x pertence ao segmento, SE E SOMENTE se l <= x <= r
def transform(x):
    return int(x)

(n, m) = tuple(map(transform,input().split()))
listaDeComparacao = list(range(1,m+1,1))
i = 0
inteiros = {}
numerosForaDoSegmento = []
while(i < n):
    i += 1
    (l,r) = tuple(map(transform,input().split()))
    if(l == r):
        inteiros[l] = l
    for num in list(range(l,r+1,1)):
        inteiros[num] = num

inteiros = sorted(list(inteiros.keys()))

for num in listaDeComparacao:
    if(num not in inteiros):
        numerosForaDoSegmento.append(num)
    
tamanhoLista = len(numerosForaDoSegmento)
if(tamanhoLista != 0):
    print(tamanhoLista)
    print(*numerosForaDoSegmento)
else:
    print(0)
