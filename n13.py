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
        val=i
list.append(val)
for j in my_dict:
    if my_dict[j]<max:
            if my_dict[j]>smax:
                smax=my_dict[j]
                val=j
list.append(val)
for k in my_dict:
    if my_dict[k]<smax:
            if my_dict[k]>tmax:
                tmax=my_dict[k]
                val=k
list.append(val)
print(list)