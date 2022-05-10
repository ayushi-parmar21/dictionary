dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
dict2={}
for i in dict:
    dict[i].clear()
    dict2[i]=dict[i]
print(dict2)