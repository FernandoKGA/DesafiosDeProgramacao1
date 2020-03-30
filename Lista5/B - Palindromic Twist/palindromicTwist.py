def palindromicTwist(size, string):
    isPalindromicTwist = True
    halfSize = int(size/2)
    firstHalf = string[0:halfSize]
    secondHalf = string[halfSize:size][::-1]

    i = 0
    while i < halfSize and isPalindromicTwist:
        res = abs(ord(firstHalf[i]) - ord(secondHalf[i]))
        if res >= 3 or res == 1:
            isPalindromicTwist = False
        i += 1
    #ord('c') -> 99

    if isPalindromicTwist:
        print("YES")
    else:
        print("NO")

t = int(input())
i = 0
while(i < t*2):
    size = int(input())
    string = input()
    palindromicTwist(size, string)
    i += 2