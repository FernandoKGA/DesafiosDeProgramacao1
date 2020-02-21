def transform(x):
    return int(x)

def checkDangerousTurn(secao1, secao2, secao3):
    (x1, y1) = secao1
    (x2, y2) = secao2
    (x3, y3) = secao3
    #secao indo para norte e vai pra oeste
    if((y1 < y2 and x1 == x2) and (x2 > x3 and y2 == y3)):
        return True
    #secao indo para leste e vai para norte
    if((y1 == y2 and x1 < x2) and (x2 == x3 and y2 < y3)):
        return True
    #secao indo para oeste e vai para sul
    if((y1 == y2 and x1 > x2) and (x2 == x3 and y2 > y3)):
        return True
    #secao indo para sul e vai para leste
    if((y1 > y2 and x1 == x2) and (x2 < x3 and y2 == y3)):
        return True
    return False

n = int(input())
par_de_secoes = []
trio_secoes = []
inicioefim = ()
quantidadeCurvasPerigosas = 0
i = 0
while(i < n+1):
    i += 1
    entrada = tuple(map(transform,input().split()))
    par_de_secoes.insert(len(par_de_secoes),entrada)
    if(i == 1):
        inicioefim = entrada

for secao in par_de_secoes:
    #deve ser pego 3 secoes para saber a direcao
    if(len(trio_secoes) == 3):
       #verifica o trio de secoes
       if(checkDangerousTurn(trio_secoes[0],trio_secoes[1],trio_secoes[2])): quantidadeCurvasPerigosas += 1
       #modifica o arranjo
       trio_secoes[0] = trio_secoes[1]
       trio_secoes[1] = trio_secoes[2]
       trio_secoes[2] = secao
       if(secao == inicioefim):
       #verifica o trio de secoes
           if(checkDangerousTurn(trio_secoes[0],trio_secoes[1],trio_secoes[2])):
               quantidadeCurvasPerigosas += 1
    else:
       trio_secoes.insert(len(trio_secoes),secao)
print(quantidadeCurvasPerigosas)
