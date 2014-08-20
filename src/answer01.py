#!/usr/bin/env python

# Use the sample code in example_01.py. Create three functions named
# func1, func2, and func3.
# 
# Make func1 print:
# "Hello World"
def func1():
    print("Hello World")
#
# Make func2 print:
# "It's nice to meet you"
def func2():
    print("It's nice to meet you")
#
# Make func3 print:
# "Howdeeeee"
def func3():
    print("Howdeeeee")
# Put your code here:


# Now, make a new function called `using_functions`.
# Make it take three arguments (name the arguments as you see fit)
# Then, execute each of the arguments that you received.
# For example, if I used arguments 'a', 'b', 'c' (don't use those in
# your answer), my code would look like this:
# 
# def using_functions(a, b, c):
#   a()
#
# You are left with the exercise of calling all three functions.

def using_functions(f1, f2, f3):
    f1()
    f2()
    f3()

if __name__ == "__main__":
    using_functions(func1, func2, func3)
