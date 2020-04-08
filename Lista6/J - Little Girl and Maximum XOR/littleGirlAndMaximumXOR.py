(l,r) = list(map(int,input().split()))
p = l ^ r
x = 1
while(x<=p):
    x=x<<1
print(x-1)