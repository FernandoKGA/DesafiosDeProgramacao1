def findShortestPath(n, sd, s, t):
    fowardPath = []
    reversePath = []
    if (s - t) < 0:
        #print("s-t < 0")
        fowardPath = sd[s-1:t-1]
        #print("fwp",fowardPath)
        if s == 1:
            reversePath = sd[t:s:-1]
            #print("rvp",reversePath)
        else:
            firstPart = sd[0:s-1]
            secondPart = sd[t-1:]
            reversePath = firstPart + secondPart
            #print("fp",firstPart)
            #print("sp",secondPart)
            #print("rvp",reversePath)
    else:
        #print("s-t > 0")
        if (s - t) == (s - 1):
            fowardPath = sd[s-1:]
            reversePath = sd[0:s-1]
            #print("fwp",fowardPath)
            #print("rvp",reversePath)
        else:
            firstPart = sd[s-1:]
            secondPart = sd[0:t-1]
            fowardPath = firstPart + secondPart
            reversePath = sd[t-1:s-1]
            #print("fwp",fowardPath)
            #print("rvp",reversePath)
            
    if len(fowardPath) == 0:
        print(sum(reversePath))
    else:
        if len(reversePath) == 0:
            print(sum(fowardPath))
        else:
            sumFowardPath = sum(fowardPath)
            sumReversePath = sum(reversePath)
            print(min(sumFowardPath,sumReversePath))

n = int(input())
stationsDistances = list(map(int,input().split()))
(s, t) = map(int,input().split())

if s != t:
    findShortestPath(n, stationsDistances, s, t)
else:
    print(0)
