import math

def calculate_square_root(): 
    """
    Calculate and display the square root of a squared number.

    Returns:
        int: The square root of the squared number.
    """
    squaredNum = get_squared_number()
    squareRootNum = math.sqrt(squaredNum)
    if(squareRootNum % 1 == 0):
        print(f"\nThe square root of {squaredNum} is {squareRootNum}.")
    else:
        print(f"The number {squaredNum} is not a square number.")

def raise_to_exponent():
    """
    Raise an inputted number to an inputted power.
    
    Returns:
        int: The exponent of the raised base"""
    exponentialNum = int(input("\nPlease enter the number to be raised: "))
    powerNum = int(input("\nPlease enter the power to raise the number to: "))
    raisedExponent = math.pow(exponentialNum, powerNum)
    print(f"\n{exponentialNum} to the power of {powerNum} is {raisedExponent}.")

def calculate_cube_root():
    """
    Calculate and display the cubed root of a cubed number.
    
    Returns:
        int: The cube root of the cubed number.
    """
    cubedNum = get_cubed_number()
    cubeRootNum = math.cbrt(cubedNum)
    print(f"\nThe cube root of {cubedNum} is {cubeRootNum}.")

def get_squared_number():
    """
    Get a squared number from the user.
    
    Returns:
        int: The squared number.
    """
    squaredNum = int(input("\nPlease enter the square number to be rooted: "))
    while(squaredNum <= 0):
        print("ERROR: Negative or 0 value entered.")
        squaredNum = int(input("\nPlease enter the square number to be rooted: "))
    return squaredNum

def get_cubed_number():
    """
    Get a cubed number from the user.
    
    Returns:
        int: The cubed number.
    """
    cubedNum = int(input("\nPlease enter the cubed number to be rooted: "))
    while(cubedNum <= 0):
        print("ERROR: Negative or 0 value entered.")
        cubedNum = int(input("\nPlease enter the cubed number to be rooted: "))
    return cubedNum
