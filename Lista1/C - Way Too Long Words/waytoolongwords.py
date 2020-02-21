def checkWord(x):
    if(len(x) > 10):
        fl = x[0]
        ll = x[len(x)-1]
        return fl + str(len(x)-2) + ll
    else:
        return x

n = int(input())
i = 0
words = []
while(i < n):
    i += 1
    words.insert(len(words),checkWord(input()))
for word in words:
    print(word)
