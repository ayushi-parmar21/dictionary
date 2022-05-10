# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# for d in student:
#     print(sum(d['id']))
# print(sum(d['success'] for d in student))
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d2:
    if i in d1:
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)


    


