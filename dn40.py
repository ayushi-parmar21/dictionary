a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
dict2={}
for j in b:
    for k in c:
        dict={}
        dict[j]=k
        for i in a:
            dict2[i]=dict
            a.remove(i)
            break
        c.remove(k)
        break
print(dict2)
            
