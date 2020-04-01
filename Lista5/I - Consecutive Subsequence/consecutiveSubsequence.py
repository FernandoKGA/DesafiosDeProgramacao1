n = int(input())
arr = list(map(int,input().split()))

setOfNumbers = dict.fromkeys(list(range(0,n+1)),0)

answer = 0
longest = 0
i = 0
while i < n:
    x = arr[i]
    setOfNumbers[x] = setOfNumbers[x-1] + 1
    if (answer < setOfNumbers[x]):
        answer = setOfNumbers[x]
        longest = x
    i += 1

result = []
i = n-1
while i >= 0:
    if arr[i] == longest:
        result.append(i)
        longest -= 1
    i -= 1

print(answer)

result.reverse()
string = ""
for num in result:
    string += str(num+1) + " "
print(string.strip())