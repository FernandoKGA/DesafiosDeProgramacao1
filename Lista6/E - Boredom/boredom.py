#http://beautifulogic.blogspot.com/2017/04/boredom-problem-solution-codeforces.html
n = int(input())
nums = list(map(int,input().split()))
points = 0
a = [0 for i in range(1,pow(10,5)+5)]
dp = dict.fromkeys(list(range(1,pow(10,5)+5)),0)

for num in nums:
    a[num] += 1

dp[0] = 0
dp[1] = a[1]
i = 2
limit = pow(10,5)
while i <= limit:
    dp[i] = max(dp[i - 1],dp[i-2]+i*a[i])
    i += 1
print(dp[int(pow(10,5))])