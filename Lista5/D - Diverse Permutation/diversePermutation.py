(n, k) = list(map(int,input().split()))
counter = n - k
diverse = True

i = 1
nums = []
while i <= counter:
    nums.append(i)
    i += 1

i = k
while i >= 1:
    if diverse:
        nums.append(counter + i)
        counter += i
        diverse = False
    else:
        nums.append(counter - i)
        counter -= i
        diverse = True
    i -= 1
print(*nums)