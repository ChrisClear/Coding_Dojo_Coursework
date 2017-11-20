"""
Typelist assignment at Coding Dojo
"""
#pylint: disable-msg=C0103
#userinput = [2, 4, 'troy', 7, 8, 9, 10]
#userinput = [2, 4, 10, 7, 8, 9, 10]
#userinput = ['chuck', "smith", 'troy', "will", "jaden", "smith", "duncan"]
userinput = ['chuck', "smith", 'troy', 9, 12, "smith", "duncan", 10, 15, "james", "jacon", 12]
isastring = False
currstring = ''
isainteger = False
currsum = 0

for each in userinput:
    if isinstance(each, str):
        isastring = True
        currstring += each+","
    if isinstance(each, (int, long, float, complex)):
        isainteger = True
        currsum += each

if isastring and isainteger:
    print "The list you gave me is a mixed bag."
    print "The numbers add up to "+str(currsum)+". The strings are '"+currstring+"'."
elif isastring and not isainteger:
    print "The list you gave me is a all strings."
    print "The strings are '"+currstring+"'."
elif not isastring and isainteger:
    print "The list you gave me is all integers."
    print "The numbers add up to "+str(currsum)+"."
else:
    pass

