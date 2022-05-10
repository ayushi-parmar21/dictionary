dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
list = []
for i,j in dict.items():
    list2 = []
    list2.append(i)
    list2.append(j)
    list.append(list2)
print(list)