# Sign your name:Jake Perman
# In all the short programs below, do a good job communicating with your end user!
import random
import time
import math

opn = True
while opn:

    def rtrndir():
        time.sleep(.5)
        menu = input("Press y to return to the directory. Otherwise press enter\n")
        if menu != "y":
            global opn
            print("Program terminated.")
            opn = False

    # 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
    # Greeting Program
    def greeting():
        name = input("What is your name? ")
        greetings = ["Whats up ", "Hey ", "Whats popping "]
        print(random.choice(greetings) + name + "!")
        rtrndir()

    # 2. Write a program where a user enters a base and height and you print the area of a triangle.

    # Program for triangle area
    def area():
        # Startup sequence
        print("Welcome to triangle area calculator!")
        run = True
        config = False
        save = False
        # The program will loop until the user decides to quit
        while run:
            try:
                # Configuration settings
                if config:
                    print("The program is currently set to round to", rnd, "decimal places")
                    rnd = int(input("How many decimals would you like to round to?\n"))
                    time.sleep(.25)
                    print("Program will now round to ", rnd, " decimal places")
                    config = False
                    save = True
                if save is False:
                    rnd = 2
                # Takes user input for length & height
                b = float(input("Enter the length: "))
                h = float(input("Enter the height: "))

                # Calculates area and checks if the output has any decimal places. If the only decimal is 0,
                # the 0 is dropped and the variable turns into an integer. If the decimal is any number other than zero,
                # it is rounded according to the user configuration. Or default rounding if no config is selected.
                triangle = round((b * h) / 2, rnd)
                triangleint = math.trunc(triangle)
                if triangleint == triangle:
                    triangle = int(triangle)
                # Prints the area of the triangle
                print("The area of the triangle is: ", triangle)

                # Shutdown sequence.
                # If user presses y, program restarts. if they press s, they can change config.
                # Otherwise program terminates
                run = False
                time.sleep(.5)
                restart = input("Type 'y' to calculate another triangle. Type 's' to change settings. "
                                "Press any other key to exit \n")
                if restart == "y":
                    run = True
                elif restart == "s":
                    run = True
                    config = True
                else:
                    rtrndir()

            # Exception handling
            except ValueError:
                print("Please enter a number")
            except KeyboardInterrupt:
                exit("BYE")
    # May have gotten a little carried away on this program experimenting with different things. Oh well

    # 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.

    # circle program
    def circ():
        r = float(input("what is the radius of your circle? "))
        c = (3.14 * 2 * r)
        print("The circumference of your circle is: ", c)
        rtrndir()


    # 4. Ask a user for an integer and then print the square root.

    # squaring program
    def sqr():
        nmbr = int(input("What number would you like to be squared? "))
        sqrt = math.sqrt(nmbr)
        print("The square root is: ", sqrt)
        rtrndir()


    # 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
    #    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.

    def starwars():
        try:
            m = float(input("what is the mass? "))
            a = float(input("what is the acceleration"))
            f = (m * a)
            print("The force is: ", f, "\nget it?")
            rtrndir()
        except ValueError:
            print("Please enter a number")


    prgrm = int(
        input("Welcome to the program directory! Please type the number of the program you would like to run\n 1) "
              "Greeting Program\n 2) Triangle Program\n 3) Circle Program\n"
              " 4) Squaring Program\n 5) Force Calculator\n"))
    if prgrm == 1:
        greeting()
    elif prgrm == 2:
        area()
    elif prgrm == 3:
        circ()
    elif prgrm == 4:
        sqr()
    elif prgrm == 5:
        starwars()
