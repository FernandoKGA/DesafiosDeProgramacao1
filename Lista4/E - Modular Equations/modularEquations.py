#ax =- b(mod n)
#a % x = b
from math import sqrt
from functools import reduce

def factorNumber(x, b):
    factors = []
    for i in range(1, int(sqrt(x))+1):
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x//i)
    count = 0
    for i in factors:
        if i > b:
            count += 1
    print(count)

##def factorNumber2(x):
##    result = 0
##    i = 1
##    while i*i <= x:
##        if x % i == 0:
##            result += 1
##            if x//i != i:
##                result += 1
##        i += 1
##    return result

(a,b) = list(map(int,input().split()))
answers = 0
if a == b:
    print("infinity")
elif a < b:
    print(0)
else:
    factorNumber(a-b,b)
    #factors = factorNumber2(a-b,b)
