##    Is it true that y is strictly larger than number x?
##    Is it true that y is strictly smaller than number x?
##    Is it true that y is larger than or equal to number x?
##    Is it true that y is smaller than or equal to number x?
#If there isn't such value, print "Impossible".

#answer: any of y, -2*10^9 <= y <= 2*10^9

import math, random

def getNumbersLimits():
    return list([-2*int(math.pow(10,9)),2*int(math.pow(10,9))])

def getQuerie(querie):
    signal = querie[0]
    x = int(querie[1])
    answer = querie[2]
    return tuple([signal,x,answer])

def getSignal(querie):
    return querie[0]

def getX(querie):
    return querie[1]

def getAnswer(querie):
    return querie[2]

def revertSignal(signal):
    if signal == ">=":
        return "<"
    elif signal == ">":
        return "<="
    elif signal == "<":
        return ">="
    else:
        return ">"

def generateAnswer(limits):
    if limits[0] < limits[1]:
        print(random.randint(limits[0],limits[1]))
    else:
        print("Impossible")
    
limits = getNumbersLimits()
n = int(input())
i = 0
while i < n:
    querie = getQuerie(list(input().split()))
    num = getX(querie)
    signal = getSignal(querie)
    answer = getAnswer(querie)
    if answer == "N":
        signal = revertSignal(signal)
    if signal == ">=":
        if num > limits[0]:
            limits[0] = num
    elif signal == ">":
        if num+1 > limits[0]:
            limits[0] = num+1
    elif signal == "<":
        if num-1 < limits[1]:
            limits[1] = num-1
    else:
        if num < limits[1]:
            limits[1] = num
    i += 1

generateAnswer(limits)
