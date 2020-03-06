def transform(x):
  return int(x)

n = int(input())
cookiesInBag = list(map(transform,input().split()))
cookiesSum = sum(cookiesInBag)
ways = 0

i = 0
while i < n:
  if (cookiesSum - cookiesInBag[i]) % 2 == 0: ways += 1
  i += 1
print(ways)
