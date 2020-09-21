import time
'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

run = True

while run:
    try:
        print("\033[32mWelcome to trapezoid area calculator!\n")
        time.sleep(.5)
        b1 = float(input("What is base one of your trapezoid? "))
        b2 = float(input("What is base two of your trapezoid? "))
        h = float(input("What is the height of your trapezoid? "))
        a = ((b1+b2)/2)*h
        print("The area of your trapezoid is \033[94m{area}\n".format(area=a))
        again = input("\033[95mPress 'y' to calculate another trapezoid, otherwise press enter")
        if again != 'y':
            run = False
            print("Have a good day!")
    except ValueError:
        print("\033[91mERROR\033[37m The only accepted value is a number\033[32m")
