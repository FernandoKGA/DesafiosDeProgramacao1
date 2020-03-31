lado_negativo = []
lado_positivo = []
pos_inicial = 0
lado_esquerdo = 'L'
lado_direito = 'R'

def getApples(lado_negativo, lado_positivo, lado):
    total = 0
    while True:
        if lado == lado_esquerdo:
            if len(lado_negativo) > 0:
                temp = lado_negativo.pop()
                total += temp[1]
                lado = lado_direito
            else:
                break
        else:
            if len(lado_positivo) > 0:
                temp = lado_positivo.pop()
                total += temp[1]
                lado = lado_esquerdo
            else:
                break
    return total

n = int(input())
i = 0
while i < n:
    (x, a) = list(map(int, input().split()))
    if x > 0:
        lado_positivo.append((x,a))
    else:
        lado_negativo.append((x,a))
    i += 1

lado_negativo.sort(key=lambda tup: tup[0])
lado_positivo.sort(key=lambda tup: tup[0])
lado_positivo.reverse()

tam_l_n = len(lado_negativo)
tam_l_p = len(lado_positivo)

if tam_l_n == 0:
    print(lado_positivo.pop()[1])
elif tam_l_p == 0:
    print(lado_negativo.pop()[1])
else:
    if tam_l_n == tam_l_p:
        print(sum([tup[1] for tup in lado_negativo]) + sum([tup[1] for tup in lado_positivo]))
        #getApples(lado_negativo,lado_positivo,lado)
    elif tam_l_n > tam_l_p:
        lado = 'L'
        ls = getApples(lado_negativo,lado_positivo,lado)
        lado = 'R'
        rs = getApples(lado_negativo,lado_positivo,lado)
        print(max(ls,rs))
    else:
        lado = 'R'
        rs = getApples(lado_negativo,lado_positivo,lado)
        lado = 'L'
        ls = getApples(lado_negativo,lado_positivo,lado)
        print(max(ls,rs))