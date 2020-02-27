#little c loves 3l

#little c loves number 3 very much. he loves all things about it.
#now he has a positive integer n. he wants to split n into 3 positive integers
#a, b, c, such that a + b + c = n and none of the 3 integers is a multiple of 3
#help him to find a solution

#INPUT
#a single line containing one integer n (3 <= n <= 10^9) the integer little c has

#OUTPUT
#print 3 positive integers, a, b, c in a single line, such that a + b + c = n and
#none of them is a multiple of 3
#it can be proved that there is at least one solution if there is at least one
#solution. if there are multiple solutions print any of them

def transform(x):
  return int(x)

def printaLinhaDois(n):
  print(str(1) + ' ' + str(1) + ' ' + str(n-2))

def printaLinhaTres(n):
  print(str(1) + ' ' + str(2) + ' ' + str(n-3))

n = int(input())

if(n % 3 == 0 or n % 3 == 1):
  printaLinhaDois(n)
else:
  printaLinhaTres(n)