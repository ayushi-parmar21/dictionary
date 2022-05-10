a = {9:0,6:0,8:3,5:6,5:9,4:6}
val = 0
val2 = 0
for i in a:
    if a[i] > val:
        val = a[i]
print("maximum",val)
for i in a:
    if a[i] < val2:
        val2 = a[i]
print("minimum",val2)
