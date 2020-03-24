#http://www.programmersought.com/article/84492137924/

##import math
##import random
##
##
##array = []
##
### input
###n , k = map(int , raw_input().split())
###prime = []
## 
### judge is prime
##def isPrime(x):
##    for i in range(2,int(math.sqrt(x))+1):
##        if x%i == 0:
##           return False
##    return True
## 
### get 1~1000 prime number
##def getPrime():
##    for i in range(3,1100):
##        if isPrime(i):
##            array.append(i)
## 
### isok
##def isOk(x):
##    if array.count(x) != 0:
##       for j in range(array.index(x)+1):
##           if x-1 == array[j]+array[j+1]:
##              return True;
##    return False
## 
### get ans
##def getAns(n, k):
##    cnt = 0
##    getPrime()
##    print(array)
##    for i in range(3,n+1): 
##        if isOk(i):
##           cnt += 1
##    if cnt >= k:
##       return "YES"
##    return "NO"

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def eratosthenesSieve(n):
    numbers = list(range(2,n+1))
    primes = []
    for num in numbers:
        if isPrime(num):
            primes.append(num)
    sieve = primes
    return sieve

def noldbachProblem(n, k):
    sieve = eratosthenesSieve(n)
    sizeSieve = len(sieve)
    primes = 0
    i = 0
    while primes != k:
        if i >= sizeSieve - 1:
            break
        prime = (sieve[i] + sieve[i+1] + 1)
        if isPrime(prime) and prime in sieve:
            primes += 1
        i += 1
    if primes == k: return "YES"
    else: return "NO"

(n, k) = tuple(list(map(int,input().split())))
print(noldbachProblem(n, k))

##n = random.randint(2, 1000)
##k = 0
##while n <= 1000:
##    print(n)
##    while k <= 1000:
##        correct = getAns(n,k)
##        mine = noldbachProblem(n, k)
##        if getAns(n, k) != noldbachProblem(n, k):
##            print(n, k)
##            print correct
##            print mine
##            break
##        #print(n, k)
##        
##        #print("Expected: ",getAns(n, k))
##        #print("Got: ",noldbachProblem(n, k))
##        k += 1
##    k = 0
##    n = random.randint(2, 1000)

##
##k = 42
##print (n, k)
##print (getAns(n,k))
##print (noldbachProblem(n,k))
