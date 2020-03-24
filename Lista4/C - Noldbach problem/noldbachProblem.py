def primeFromSumOfPrimes(k):
    if k > 1:
        firstPrime = (6*(k-1) + 1)
        secondPrime = (6*k - 1)
    else:
        firstPrime = (6*k - 1)
        secondPrime = (6*k + 1)    
    return firstPrime + secondPrime + 1

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
        

def noldbachProblem(n, k):
    if k == 0:
        print("YES")
    else:    
        i = 1
        primes = 0
        while primes != k:
            prime = primeFromSumOfPrimes(i)
            if prime > n:
                break
            else:
                if isPrime(prime): primes += 1
            i += 1
        if primes == k:
            print("YES")
        else:
            print("NO")    

#(n, k) = tuple(map(int,input().split()))
#noldbachProblem(n,k)

n = 1000
k = 1000
while k != 0:
    print(n, k)
    noldbachProblem(n, k)
    k -= 1

#k numeros primos de 2 a n podem ser expressos por uma soma de 3 inteiros
#1 e mais dois numeros primos que sao vizinhos, sem outros no meio

#2 e 3 nao entra nessa conta pq n eh possivel juntar 3 inteiros maiores q 0 sendo primos

#27 2
#5 7
#7 11
#11 13
#13 17
#17 19
#19 23
#23 27

#6k + i
#6*0 + 1
#6*1 +- 1 5 7
#6*2 +- 1 11 13
