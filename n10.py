dict = {
'Alex': ['subj1', 'subj2', 'subj3'],
'David': ['subj1', 'subj2']}
count=0
for i in dict:
    if type(dict[i])==list:
        j=0
        while j<len(dict[i]):
            count+=1
            j+=1
    else:
        count+=1
print(count)
        
    