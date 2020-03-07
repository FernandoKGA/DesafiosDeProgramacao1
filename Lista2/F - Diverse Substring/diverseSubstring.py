n = int(input())
s = input()
i = 1
diverse = False
while i < len(s):
    if s[i] != s[i-1]:
        print("YES")
        print(s[i-1] + s[i])
        diverse = True
        break
    i += 1
if not diverse: print("NO")
