def factorNumber(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0: factors.append(i)
    return factors

def numberToArray(num):
    return [int(x) for x in str(num)]

n = int(input())
number_integers = numberToArray(n)
factors = factorNumber(n)
count = 0
for factor in factors:
    array_from_factor = numberToArray(factor)
    for integer in array_from_factor:
        if integer in number_integers:
            count += 1
            break
print(count)