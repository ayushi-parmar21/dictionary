import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
   
   

print()
# mthoed second
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(0),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)


print()
# method third
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(d)
# max=0
# for i,v in d.items():
#     if i>max:
#         max=i
#         print(max)
