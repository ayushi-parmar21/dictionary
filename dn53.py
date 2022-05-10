list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
dict={}
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        list1=[]
        list1.append(list[i][1])
        list1.append(list[i][2])
        dict[list[i][0]]=list1
        
        j+=1
    i+=1
print(dict)