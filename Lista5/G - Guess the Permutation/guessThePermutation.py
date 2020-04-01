n = int(input())
#nums = list(range(1,n+1))
nums = [0 for i in range(1,n+1)]
i = 0
while i < n:
    permutation = list(map(int,input().split()))
    j = 0
    for p in permutation:
        nums[j] = max(nums[j],p)
        j += 1
    i += 1
maximumNums = max(nums)
for num in nums:
    if maximumNums == num:
        idx = nums.index(num)
        nums[idx] = n
        break
print(*nums)