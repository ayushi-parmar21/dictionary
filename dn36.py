dic={'key1': 1, 'key2': 3, 'key3': 2} 
dic1={'key1': 1, 'key2': 2}
dic3={}
for i in dic:
    for j in dic1:
        if i==j and dic[i]==dic1[j]:
            print(i,":",dic[i])