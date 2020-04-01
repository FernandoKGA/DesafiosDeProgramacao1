(n,k) = list(map(int,input().split()))
string = list(input())
substrings = []

for letter in string:
    if len(substrings) != 0:
        if substrings == 0:
            print("ha")
    else:
        substrings.append((letter,1))

qtd_a = string.count('a')
qtd_b = string.count('b')