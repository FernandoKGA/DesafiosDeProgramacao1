#J - Minimum Ternary String

def writeRestOfString(TS, result, indexOfFirstTwo):
    size = len(TS)
    for num in TS[indexOfFirstTwo:size]:
        result += str(num)
    return result

def removeAllOnesAfterFirstTwo(TS, indexOfFirstTwo):
    i = indexOfFirstTwo
    size = len(TS)
    beginOfTS = TS[0:indexOfFirstTwo]
    restOfTS = ""
    while i < size:
        if TS[i] != '1': restOfTS += str(TS[i])
        i += 1
    return beginOfTS + restOfTS

def countZerosAndOnes(TS, limit):
    i = 0
    zeros = 0
    ones = 0
    while i < limit:
        if TS[i] == 1: ones += 1
        else: zeros += 1
        i += 1
    return (zeros, ones)

def countOnes(TS, limit):
    i = 0
    ones = 0
    while i < limit:
        if TS[i] == 1: ones += 1
        i += 1
    return ones

def countZeros(TS, limit):
    i = 0
    zeros = 0
    while i< limit:
        if TS[i] == 0: zeros += 1
        i += 1
    return zeros

def writeZeros(result, zeros):
    i = 1
    while i <= zeros:
        result += str(0)
        i += 1
    return result

def writeOnes(result, ones):
    i = 1
    while i <= ones:
        result += str(1)
        i += 1
    return result

def checkForFirstTwo(TS):
    i = 0
    size = len(TS)
    while(i < size):
        if TS[i] == 2 or TS[i] == '2': return i
        i += 1
    return None

def changeStringWithOnlyOnesAndZeros(TS):
    size = len(TS)
    result = ""

    (zeros, ones) = countZerosAndOnes(TS, size)
    result = writeZeros(result,zeros)
    result = writeOnes(result,ones)

    return result

def changeString(TS, indexOfFirstTwo):
    result = ""
    size = len(TS)

    zeros = countZeros(TS, indexOfFirstTwo)
    ones = countOnes(TS, size)
    result = writeZeros(result,zeros)
    result = writeOnes(result,ones)
    result = writeRestOfString(TS,result,indexOfFirstTwo)
    indexOfFirstTwo = checkForFirstTwo(result)
    result = removeAllOnesAfterFirstTwo(result, indexOfFirstTwo)
    
    return result

def splitString(string):
  characters = []
  size = len(string)
  i = 0
  while(i < size):
    characters.append(int(string[i]))
    i += 1
  return characters

ternaryString = input()
#print(ternaryString)
TSArray = splitString(ternaryString)

indexOfFirstTwo = checkForFirstTwo(TSArray)
if indexOfFirstTwo != None:
    print(changeString(TSArray, indexOfFirstTwo))
else:
    print(changeStringWithOnlyOnesAndZeros(TSArray))
