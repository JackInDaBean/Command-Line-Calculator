import math

def selectSquareRoot(): # Square Root 
    squaredNum = int(input("\nPlease enter the square number to be rooted: "))
    squareRootNum = math.sqrt(squaredNum)
    print(f"\nThe square root of {squaredNum} is {squareRootNum}.")

def selectExponent(): # Exponents
    exponentialNum = int(input("\nPlease enter the number to be raised: "))
    powerNum = int(input("\nPlease enter the power to raise the number to: "))
    raisedExponent = math.pow(exponentialNum, powerNum)
    print(f"\n{exponentialNum} to the power of {powerNum} is {raisedExponent}.")

def selectCubeRoot(): # Cube Root
    cubedNum = int(input("\nPlease enter the cubed number to be rooted: "))
    cubeRootNum = math.cbrt(cubedNum)
    print(f"\nThe cube root of {cubedNum} is {cubeRootNum}.")