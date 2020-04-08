def canHavePairs(amount):
    if amount % 2 == 0:
        print("Sim")
    else:
        print("Nao")

(n, m) = list(map(int,input().split()))
a = list(map(int,input().split()))

i = 0
while i < m:
    (l,r) = tuple(map(int,input().split()))
    if r > l:
        people = sum(a[l-1:r])
        canHavePairs(people)
    elif r == l:
        people = a[r]
        canHavePairs(people)
    else:
        fp = a[l-1:len(a)]
        sp = a[0:r]
        firstPart = sum(fp)        
        secondPart = sum(sp)
        canHavePairs(firstPart + secondPart)
    i += 1