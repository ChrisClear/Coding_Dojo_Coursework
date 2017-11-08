my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()

x = my_dict.keys()
print x

y = my_dict.values()
print y

z = zip(x,y)
print z

def tupleOut(obj):
  x = obj.keys()
  y = obj.values()
  z = zip(x,y)
  print z


tupleOut(my_dict)