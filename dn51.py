dict = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
dict2 = {}
for i,j in dict.items():
    k=0
    list2=[]
    while k<len(j):
        if j[k]%2==0:
            list2.append(j[k])
        k+=1
    dict2[i]=list2
print(dict2)
    