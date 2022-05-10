dict={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
user=int(input("enter a number: "))
list=[]
for i,j in dict.items():
    if j==user:
        print("true")
    else:
        print("false")
    