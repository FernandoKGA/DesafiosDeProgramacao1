#v = quantidade de numeros no vetor
#ai elevado a 2
#formula: 2^v - 1 = x
#soma dos numeros elevados ao que tem no vetor

def calculateFormula(sommatory):
    return pow(2,sommatory) - 1

n = int(input())
numbers = list(dict.fromkeys(list(map(int,input().split()))).keys())

##v = len(numbers)
##for i in numbers:
##    sommatory += i
##    powedNumbers += pow(2,i)
##res = calculateFormula(sommatory)

maximum = max(numbers)
count = len(numbers)

print(maximum - count + 1)

##print(powedNumbers)
##print(res)

##if powedNumbers == res:
##    print(0)
##else:
##    i = 0
##    sumOfMissing = 0
##    nums = 0
##    while i < sommatory:
##        if i not in numbers:
##            nums += 1
##            sumOfMissing += pow(2,i)
##            if sumOfMissing+powedNumbers >= res:
##                if sumOfMissing == res:
##                    print(nums)
##        i += 1
