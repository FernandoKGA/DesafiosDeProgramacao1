import math

def sumPerimeter(a, b, c):
    return int(4*(a + b + c))
        
(f1, f2, f3) = tuple(map(int,input().split()))
#f1 = a * c
#f2 = a * b
#f3 = b * c

a = math.sqrt((f2 * f1) / f3)
b = math.sqrt((f3 * f2) / f1)
c = math.sqrt((f3 * f1) / f2)
    
print(sumPerimeter(a,b,c))
