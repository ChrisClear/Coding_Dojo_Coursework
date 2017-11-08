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

multiply([2,4,5],3)