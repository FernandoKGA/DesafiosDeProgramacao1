import random

def transform(x):
    return int(x)

def findTwoDistinctPoints(l1,r1,l2,r2):
    if (l1 == l2 and r1 == r2):
        a = l1
        b = r2
        return [a, b]
    while True:
        a = random.randint(l1,r1-1)
        b = random.randint(l2,r2-1)
        if(a != b):
            break
    return [a, b]

queriesQuantity = int(input())
i = 0
queries = []
while(i < queriesQuantity):
    i += 1
    numeros = list(map(transform,input().split()))
    queries.insert(len(queries), numeros)
for query in queries:
    a, b = findTwoDistinctPoints(query[0],query[1],query[2],query[3])
    print(str(a) + ' ' + str(b))
