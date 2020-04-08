from math import floor

def digitSum(num):
    result = 0
    while num:
        result += num % 10
        num //= 10
    return result

def isReallyBigNumber(x,s):
    difference = x - digitSum(x)
    if not difference < s:
        return True
    else:
        return False

(n,s) = list(map(int,input().split()))
if n - digitSum(n) < s:
    print(0)
else:
    left = 0
    right = n

    while left < right:
        mid = floor(left + (right - left) / 2)
        if (mid - digitSum(mid) >= s):
            right = mid
        else:
            left = mid + 1
    print(n - left + 1)