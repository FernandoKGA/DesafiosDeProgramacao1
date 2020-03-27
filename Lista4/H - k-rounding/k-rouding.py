import math

(n,k) = tuple(map(int,input().split()))
i = 1
num = 1
while i <= k:
    num *= 10
    i += 1
gcd = math.gcd(num,n)
res = int((n / gcd) * num)
#print(newNum)
print(res)
#print(res)
