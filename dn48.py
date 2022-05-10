dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dict2={}
for i in dict:
    j=1
    count=1
    while j<len(dict[i]):
        count+=1
        j+=1
    dict2[dict[i]]=count
print(dict2)
    
    
