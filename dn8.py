ayu=input("enterr a key: ")
dict={"name":"Raju","marks":56}
if ayu in dict:
    print("exist")
else:
    print("not exists")
    
# method seconde
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key(5)
key(9)