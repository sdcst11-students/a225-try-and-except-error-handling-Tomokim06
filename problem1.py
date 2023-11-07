#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
#import os
#os.system('cls')
import math


#("Enter in the coefficients for a quadratic equation in the format:")
#print("  ax^2 + bx + c = 0")

while True:
  while True:
    try:
        a = float(input("enter 'a' value: "))
        b = float(input("enter 'b' value: "))
        c = float(input("enter 'c' value: "))

        d = (b**2) - (4*a*c)

        sol1 = round(((-b-math.sqrt(d))/(2*a)), 2)
        sol2 = round(((-b+math.sqrt(d))/(2*a)), 2)
        if (b**2)-(4*a*c) <0:
          print(f'The solution are {sol1} and {sol2}')
        else:  
          print("There are no real roots to the equation")
    except:
      print("Those are not valid values for a, b or c")