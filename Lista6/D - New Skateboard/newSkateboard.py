#http://www.programmersought.com/article/4448691623/
answer = 0
s = list(map(int,list(input())))

for num in s:
    if num % 4 == 0:
        answer += 1

i = 1
while i < len(s):
    if ((s[i] + (s[i-1] * 2)) % 4 == 0):
        answer += i
    i += 1
print(answer)