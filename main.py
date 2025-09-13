from modules import arithmetic 
from modules import menu
import sys

"""
Command-line calculator tool.

User inputs the type of calculation and the numbers to calculate
"""

# User chooses the type of calculation:
while True:
    menu.display_menu_prompt()
    calculationSelection = int(input("\nPlease select the calculation that you wish to perform:"))

    match calculationSelection:
        case 0:
            arithmetic.calculate_square_root()
        case 1:
            arithmetic.raise_to_exponent()
        case 2:
            arithmetic.calculate_cube_root()
        case 3:
            sys.exit(0)
        case _:
            print("\nERROR: Invalid Selection\n")

if __name__ == '__main__':
    main()
