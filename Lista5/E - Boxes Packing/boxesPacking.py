n = int(input())
sideLenghts = list(map(int,input().split()))
sides = {}
for num in sideLenghts:
    if num in sides:
        sides[num] += 1
    else:
        sides[num] = 1
nums = 0
while len(sides) != 0:
    temp = list(sides.keys())
    for num in temp:
        sides[num] -= 1
        if sides[num] == 0:
            del sides[num]
    nums += 1
print(nums)