"""
Coin Tosses Assignment, Coding Dojo Python fundamentals.
"""
#pylint: disable=C0103
def getRandom():
    """ This function delivers a random number between 1 and 2 (heads or tails)
    """
    import random
    random_num = random.randint(1, 2)
    return random_num

def coinToss():
    """ This function gets a random number, expecting 1 or 2, and uses it for heads or tails.
    Will count the results in order to output. This is a fun science experiment!
    I expect the results to be close to 50/50.
    """
    counter = 0 #initialize variable
    headcount = 0
    tailcount = 0
    headortail = "head"
    while counter < 5000:
        nexttoss = getRandom() #get the next coin toss
        if nexttoss is 1:
            headortail = "head"
            headcount += 1
        else:
            headortail = "tail"
            tailcount += 1
        print "Attempt #"+counter+": Throwing a coin... It's a "+headortail+"! Got "+headcount+"head(s) so far and "+tailcount+" tail(s) so far..."
    print "Ending the program, thank you!"

