my_dict = {
'a':50,
'b':58,
'c':56,
'd':40,
'e':100,
'f':20
}
max,smax,tmax=0,0,0
list=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
list.append(max)
for j in my_dict:
    if my_dict[j]<max:
            if my_dict[j]>smax:
                smax=my_dict[j]
list.append(smax)
for k in my_dict:
    if my_dict[k]<smax:
            if my_dict[k]>tmax:
                tmax=my_dict[k]
list.append(tmax)
print(list)
 
 
# 2 method
list3=[]
list1=sorted(my_dict.values())
list3.append(list1[-1])
list3.append(list1[-2])
list3.append(list1[-3])
print(list3)
