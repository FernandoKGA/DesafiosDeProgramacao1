import math

def findLargestSum(n):
    digits = digitsFromNumber(n)
    if len(digits) == 1:
        print(n)
    else:
        size = len(digits)
        numberWithNines = 0
        i = 0
        while i < size-1:
            numberWithNines += 9 * math.pow(10,i)
            i += 1
        firstDigit = int(digits[0])-1
        numberWithNines += firstDigit * math.pow(10,size-1)
        numberWithNines = int(numberWithNines)
        rest = n - numberWithNines
        print(sum(digitsFromNumber(numberWithNines)) + sum(digitsFromNumber(rest)))

def digitsFromNumber(number):
    listOfDigitsFromN = list(map(int,list(str(number))))
    return listOfDigitsFromN

n = int(input())
findLargestSum(n)
