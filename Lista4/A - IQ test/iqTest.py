def checkForEveness(firstNum, secondNum, thirdNum, initialIndex):
    if firstNum % 2 == 0:
        if secondNum % 2 == 0:
            print(initialIndex + 2)
        else:
            if thirdNum % 2 == 0:
                print(initialIndex + 1)
            else:
                print(initialIndex)
    else:
        if secondNum % 2 != 0:
            print(initialIndex + 2)
        else:
            if thirdNum % 2 != 0:
                print(initialIndex + 1)
            else:
                print(initialIndex)

def iqTest(n, numbers):
    initialIndex = 1
    
    firstNum = numbers[0]
    secondNum = numbers[1]
    thirdNum = numbers[2]
    if len(numbers) == 3:
        checkForEveness(firstNum, secondNum, thirdNum, initialIndex)
    else:
        evens = None
        if firstNum % 2 == 0 and secondNum % 2 == 0 and thirdNum % 2 == 0:
            evens = True
        else:
            if firstNum % 2 != 0 and secondNum % 2 != 0 and thirdNum % 2 != 0:
                evens = False
            else:
                checkForEveness(firstNum, secondNum, thirdNum, initialIndex)

        if evens != None:
            if evens:
                i = 0
                while i < len(numbers):
                    if numbers[i] % 2 != 0:
                        print(i + initialIndex)
                        break
                    i += 1
            else:
                i = 0
                while i < len(numbers):
                    if numbers[i] % 2 == 0:
                        print(i + initialIndex)
                        break
                    i += 1

n = int(input())
numbers = list(map(int,input().split()))
iqTest(n, numbers)
