def removeDuplicates(integers):
    newIntegers = []
    duplicates = []
    for integer in integers:
        if integer not in newIntegers: newIntegers.append(integer)
        else: duplicates.append(integer)
    return newIntegers, duplicates

def factorNumber(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0: factors.append(i)
    return factors

def removeNumbersFromFactorList(integers, factors):
    newIntegers = []
    duplicates = []
    for integer in integers:
        if integer not in factors: newIntegers.append(integer)
        else: duplicates.append(integer)
    return newIntegers

def numbersAreEqual(integers, newIntegers):
    return len(newIntegers) != len(integers)/2
    #if it is half the size, it is guaranteed that is the same number
    #because it has eliminated all its duplicateds

def findNumbers(integers):
    (newIntegers, duplicates) = removeDuplicates(integers)
    if numbersAreEqual(integers, newIntegers):
        x = newIntegers.pop()
        factorsOfX = factorNumber(x)
        newIntegers = removeNumbersFromFactorList(newIntegers, factorsOfX)
        if len(newIntegers) == 0:
            y = duplicates.pop()
            print(x, y)
        else:
            y = newIntegers.pop()
            print(x, y)
    else:
        x = newIntegers.pop()
        print(x, x)

n = int(input())
integers = sorted(list(map(int,input().split())))
if n == 2: print(*integers)
else: findNumbers(integers)

