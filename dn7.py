dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic3.update(dic1)
dic3.update(dic2)
print(dic3)

# method second 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)
