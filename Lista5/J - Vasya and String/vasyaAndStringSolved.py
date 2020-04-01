(n, k) = list(map(int,input().split()))
string = list(input())

a = 0
b = 0
limiter = 0
answer = 0

for letter in string:
    if letter == 'a':
        a += 1
    else:
        b += 1
    if min(a,b) > k:
        if string[limiter] == 'a':
            a -= 1
        else:
            b -= 1
        limiter += 1
    else:
        answer += 1
print(answer)