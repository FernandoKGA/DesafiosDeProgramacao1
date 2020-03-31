n = int(input())
string = list(input())
twoGrams = {}

i = 0
while i < n-1:
    twoGram = string[i] + string[i+1]
    keys = list(twoGrams.keys())
    if twoGram not in keys:
        twoGrams[twoGram] = 1
    else:
        twoGrams[twoGram] += 1
    i += 1

maxTwoGram = max(list(twoGrams.items()),key=lambda item: item[1])
print(maxTwoGram[0])