persons = ["Anna","Kevin","Amy","Robert"]
age = ['101','102','103','104']
country =['United States', 'Canada', 'Mexico', 'Russia']
language =['Python','Java','Javascript']

# print persons
# print "My age is "+ age[0]
# print "My country of birth is The "+ country[0]
# print "My favorite language is "+ language[0]

# profile = zip(persons, age, country, language)
# print profile[0]

def myName(i,persons,age,country):
  print 'My name is '+persons[i]
  print 'My age is ' +age[i]
  print "My country of birth is The "+country[i]
  print 'My favorite language is '+language[i]
  


myName(2,persons,age,country)
  
