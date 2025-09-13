# --------------------------------------------------
#
#
#

import math
from modules import arithmetic 

programRunning = True

# Exploration of Python's fundamentals.

# Match Case selection for calculation selection:
while(programRunning):
    print("\nPlease select the calculation that you wish to perform:")
    print("\n-------------------------------------------------------")
    print("0 -- Square root")
    print("1 -- Exponents")
    print("2 -- Cube Root")
    print("-------------------------------------------------------")
    calculationSelection = int(input("\nPlease select the calculation that you wish to perform:"))

    match calculationSelection:
        case 0:
            arithmetic.selectSquareRoot()
        case 1:
            arithmetic.selectExponent()
        case 2:
            arithmetic.selectCubeRoot()
        case _:
            print("\nERROR: Invalid Selection\n")


