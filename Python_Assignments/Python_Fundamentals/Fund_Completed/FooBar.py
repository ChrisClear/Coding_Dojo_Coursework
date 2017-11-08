"""
Optional Assignment: Foo and Bar
Write a program that prints all the prime numbers
and all the perfect squares for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for
whether it is prime or a perfect square. If it is a prime number
print "Foo". If it is a perfect square print "Bar". If it is neither
print "FooBar". Do not use the python math library for this exercise.
For example, if the number you are evaluating is 25, you will have to

figure out if it is a perfect square. It is, so print "Bar".

This assignment is extra challenging! Try pair programming and pulling up a white board.

Prime numbers in this code do NOT include 1 or 0. These are automatically accounted for
at the end of the function...
"""
#pylint: disable-msg=C0103

def foobar(start, end):
    """
    This is the main foobar function that uses primeNumber and sqaureNumber functions.
    """

    currnum = start

    while currnum < end:
        if primeNumber(currnum):
            print "Currnum is a Foo: "+str(currnum)
            currnum += 1
        elif squareNumber(currnum):
            print "Currnum is a Bar: "+str(currnum)
            currnum += 1
        else:
            print "FooBar: "+str(currnum)
            currnum += 1

def primeNumber(number):
    """
    Returns true or false if the number is a prime number.
    """
    halfnum = number / 2
    if number is 1 or 0:
        return False
    for i in range(2, halfnum+1):
        if number % i is 0:
            return False
    return True

"""
#script to test the primeNumber function
if primeNumber(0):
    print "prime"
else:
    print "not prime"
"""

def squareNumber(number):
    """
    Returns true or false if the number is a perfect square.
    """
    import math
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

"""
#script to test the square function 
if squareNumber(9):
    print "square"
else:
    print "not square"
"""

foobar(100,100000)
