import math

n = int(input())
luckyNums = 0
while n != 0:
  luckyNums += int(math.pow(2,n))
  n -= 1
print(luckyNums)
