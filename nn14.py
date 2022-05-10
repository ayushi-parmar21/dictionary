
dict={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
dict2={}
for i in dict:
    for j in dict:
        if dict[i]<dict[j]:
            temp=dict[i]
            dict[i]=dict[j]
            dict[j]=temp
print(dict)