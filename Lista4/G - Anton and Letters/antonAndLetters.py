letras = list(input().split(','))
letras[0] = letras[0].replace('{','')
letras[len(letras)-1] = letras[len(letras)-1].replace('}','')
if len(letras) == 1:
    if letras[0] == '':
        print(0)
    else:
        print(1)
else:
    i = 0
    while i < len(letras):
        letras[i] = letras[i].lstrip()
        i += 1
    print(len(dict.fromkeys(letras)))
