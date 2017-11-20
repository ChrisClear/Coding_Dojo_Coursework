# input
word_list = ['hello','world','my','name','is','Anna'] 
# output
new_list = []

letters = set('o')

for word in word_list:
    if letters & set(word):
        new_list.append(word)
        print new_list