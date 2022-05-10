data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
i=0
list1=[]
while i<len(data):
    for j in data[i]:
        if data[i][j] not in list1:
            list1.append(data[i][j])
    i+=1
print(list1)