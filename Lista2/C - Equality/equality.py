def transform(x):
  return int(x)

def alphabet():
  string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return list(string)

(n, k) = tuple(map(transform,input().split()))
string = list(input())
alphabet = alphabet()

letters = {}
i = 0
while i < k:
  letters[alphabet[i]] = 0
  i += 1

for letter in string:
  letters[letter] += 1
minimun = min(letters.values())
if minimun == 0: print(0)
else: print(minimun*k)
