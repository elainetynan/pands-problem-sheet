# squareRoot.py
#
# Takes a positive floating-point number as input and outputs 
# an approximation of its square root.
# 
# Author: Elaine Tynan

def sqrt(num):
    x = num
    marginError = 0.00001
    sqRoot = 0
    while True:
        sqRoot = 0.5 * (x + (num / x))

        if abs(sqRoot - x) < marginError:
            break
        x = sqRoot
    return sqRoot

n = float(input("Please enter a positive number for the square root: "))
if n <= 0:
    print("Invalid input. The inut must be a positive number")
else:
    print("The square root of",n,"is",round(sqrt(n),2))