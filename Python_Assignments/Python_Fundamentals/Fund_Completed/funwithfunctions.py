""" Fun with functions project
by: Troy Center troycenter1@gmail.com

Assignment: Fun with Functions
Create a series of functions based on the below descriptions.

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes 
have your program print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:
"""
#pylint: disable=E1101

def odd_even():
    """This is a function to check 1 to 1000 and print if the
    number is odd or even.
    """
    currnum = 0
    while currnum <= 1000:
        if is_even(currnum):
            print "Number is "+str(currnum)+". This is an even number."
            currnum += 1
        else:
            print "Number is "+str(currnum)+". THis is an odd number."
            currnum += 1

def is_even(number):
    """is_even will return True if the number is even
    """
    if number % 2 == 0:
        return True
    else: return False

odd_even()
def multiply(valuestomultiply):
    """ Multiply:
    Create a function called 'multiply' that iterates through each value in a list 
    and returns a list where each value has been multiplied by 5.
    The function should multiply each value in the list by the second argument.
    """
    newlist = []
    for each in valuestomultiply:
        newlist.append(each*each)
    print newlist
    return newlist

multiply([2, 4, 6, 9])


"""
#I did not finish this one. Not understanding it. The multiply
#function I built cannot handle two input types... moving on... 
Hacker Challenge:
Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional list.
Each internal list should contain the number of 1's as the number in the original list.

# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def layered_multiples(arr)



    return new_array
x = layered_multiples(multiply([2,4,5],3))


def returnones(num):

    i = 0
    temp_arr = []
    while i < num:
        temp_arr.append(1)
        i += 1
    print temp_arr
    return temp_arr

"""
