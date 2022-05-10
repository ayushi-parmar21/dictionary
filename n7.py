list=[
{"first":"1"},
{"second": "2"},
{"third": "1"},
{"four": "5"},
{"five":"5"},
{"six":"9"},
{"seven":"7"}
]
i=0
list1=[]
while i<len(list):
    for j in list[i]:
        if list[i][j] not in list1:
            list1.append(list[i][j])
    i+=1
print(list1)
    