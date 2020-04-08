def xor(n1, n2):
    return n1 ^ n2

n = int(input())
array = list(map(int,input().split()))

if n > 1:
    consecutive_sets = []
    consecutive = []
    i = 0
    while i < n - 1:
        if array[i+1] > array[i]:
            if len(consecutive) != 0:
                consecutive.append(array[i+1])
                if i == n - 2:
                    consecutive_sets.append(consecutive)
                    consecutive = []
            else:
                consecutive.append(array[i])
                consecutive.append(array[i+1])
                if i == n - 2:
                    consecutive_sets.append(consecutive)
                    consecutive = []
        else:
            if array[i] not in consecutive:
                consecutive.append(array[i])
                consecutive_sets.append(consecutive)
                consecutive = []
            else:
                consecutive_sets.append(consecutive)
                consecutive = []
        i += 1

    max_xor = 0
    for conj in consecutive_sets:
        if len(conj) > 2:
            i = 0
            max_insider_xor = 0
            insider_xor = 0
            while i < len(conj):
                insider_xor = xor(insider_xor,conj[i])
                max_insider_xor = max(max_insider_xor,insider_xor)
                i += 1
            max_xor = max(max_xor,max_insider_xor)
            max_xor = max(max_xor,max(conj))                
        elif len(conj) == 2:
            max_xor = max(max_xor,xor(conj[0],conj[1]))
        else:
            max_xor = max(max_xor,conj[0])
        
    print(max_xor)
else:
    print(array[0])