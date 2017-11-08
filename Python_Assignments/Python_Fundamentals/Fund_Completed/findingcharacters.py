"""
Assignment: Find Characters
Write a program that takes a list of strings and a string containing
a single character, and prints a new list of all the strings containing that character.
Here's an example:
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
"""
#pylint: disable-msg=C0103
new_word_list = []
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
for each in word_list:
    for letter in each:
        if letter == char:
            new_word_list.append(each)
        else:
            pass
print "I checked the word list you gave me for the letter '"+char+"'."
print "I found these words with that letter: "+str(new_word_list)+"."
