(n, k) = tuple(map(int,input().split()))
array = sorted(list(dict.fromkeys((map(int,input().split())),1)))
size = len(array)

i = 0
while i < k:
    if i < size:
        if i > 0:
            print(array[i] - array[i-1])
        else:
            print(array[i])
    else:
        print(0)
    i += 1
