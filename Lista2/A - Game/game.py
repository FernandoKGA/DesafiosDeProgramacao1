def transform(x):
  return int(x)

(n1, n2, k1, k2) = tuple(map(transform,input().split()))

if n2 >= n1: print("Second")
else: print("First")
