list=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
i=0
dict={}
while i<len(list):
    for j in list[i]:
        if list[i][j]=="#FF0000":
            print(j)  
    i+=1
# print(list)