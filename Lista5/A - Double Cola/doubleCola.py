queue = ["Sheldon","Leonard","Penny","Rajesh","Howard"]
n = int(input())
i = 1
while (i * 5 < n):
    n -= i * 5
    i *= 2

print(queue[int((n-1)/i)])