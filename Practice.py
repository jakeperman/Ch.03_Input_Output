import time
import math
# import curses
#
# stdscr = curses.initscr()
# curses.cbreak()
# print("hello\rworld")
# print("4")
# print("4+2")
# print(4 + 2)
# my_name = 'jake'
# greeting = 'hey'
# print(greeting + " " + my_name)

# bullets = 20
# mags = 3
# trigger = True
#
# while trigger is True:
#
#     if bullets >= 5:
#         print("Remaining Ammo:", bullets)
#         time.sleep(.25)
#         bullets = bullets - 1
#     elif bullets > 0 < 5:
#         print("LOW AMMO ", "Only ", bullets, "left")
#         time.sleep(.3)
#         bullets = bullets - 1
#     else:
#         trigger = False
#         print("NO AMMO, PLEASE RELOAD")
#         if mags > 0:
#             bind = 'r'
#             reload = stdscr.getch("Press R to realod")
#             if reload == bind:
#                 bullets = 20
#                 trigger = True
#                 print("Successfully Reloaded")
#             else:
#                 print("You pressed ", reload, ".", "Please press R to reload")
#         else:
#             print("ERROR No remaining magazines")
# run = True
# while run:
#
#     try:
#         def get_num(string):
#
#             num = input(string)
#
#             if '.' not in num:
#                 num = int(num)
#             elif '.' in num:
#                 print("yes")
#                 num = float(num)
#                 numchk = math.trunc(num)
#                 print(num, numchk)
#                 if numchk == num:
#                     print("true")
#                     num = int(num)
#
#             return num
#
#         b = get_num("Please enter a decimal number")
#         c = get_num("Please enter another decimal number")
#         d = c * b
#         print(d, "is a", type(d))
#
#     except KeyboardInterrupt:
#         print("whoops")


# b = float(input("Enter the length: "))
#
# h = float(input("Enter the height: "))
#
# # Calculates area and checks if the output has any decimal places
# triangle = (b * h) / 2
# rnd = round(triangle, 2)
# # trianglernd = math.trunc(triangle)
# # if triangle == trianglernd:
# #     triangle = int(triangle)
# print(rnd)
# # x = 3
# # y = 7

txt = "My name is {name}".format(name="jake")
print(txt)


# def func(x, y):

#    return x + y


# num = func(x, y)
# print(num)
# x = round(16.43534, 3)
# print(x)

# a = float(16)
#  b = float(12)
# c = a + b

# print(type(c))


# miles = input("Please enter the trip distance: ")
# gal = input("How many gallons of gas did you use: ")
# mpg = miles/gal
#
# print(mpg)


# This is explaining the end character
# i = 0
# print(i, end=" ")
# i = 1
# print(i)
# i = 2
# print(i)
