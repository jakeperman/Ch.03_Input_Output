'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is!

'''
run = True

while run:

    try:
        f = float(input("\nEnter a temperature in degrees Fahrenheit: "))
        c = round((f-32)/1.8, 1)
        print(f, "degrees fahrenheit is", c, "degrees celsius")

    except ValueError:
        print("Please enter a number.\n")



