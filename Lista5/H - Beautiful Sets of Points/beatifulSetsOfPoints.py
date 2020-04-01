#Pingeonhole Principle
(n,m) = list(map(int,input().split()))
minimal = min(n,m)
i = 0
print(minimal + 1)
while i <= minimal:
    print(i,minimal - i)
    i += 1