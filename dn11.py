dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={**dic1,**dic2}
print(dic3)


#method second
dic2.update(dic1)
print(dic2)


#method third 
dic4={}
for i in (dic2,dic1):
    dic4.update(i)
print(dic4)

# method 
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)