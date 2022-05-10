# a={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(*(list(a.keys())))
# c=(list(a.values()))
# for i in range(len(c)):
#     print(*(c[i]))


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(arr)
#     # arr.sort()
#     # arr.reverse()
#     # i=0
#     # while i<len(arr):
#     #     if arr[0]==arr[i]:
#     #         pass
#     #     else:
#     #         max=arr[i]
#     #         break
#     #     i+=1
#     # print(max)


# def solve(s):
#     if 0<len(s)<1000:
#         i=0
#         while i<len(s):
#             if s[i]==s[0]:
#                 s=s[0].upper()+s[1:]
#             elif s[i]==" ":
#                 s=s[:i]+" "+s[i+1].upper()+s[i+2:]
#             i+=1
#         print(s)
# solve("ayushi parmar")



# def is_leap(year):
#     leap = False
#     if year%4==0:
#         return True
#     elif year%100!=0 and year%400==0:
#         return True

#     return leap
# year = int(input())
# print(is_leap(year))



# user=int(input())
# arr=list(map(int,input().split()))
# i=0
# while i<len(arr):
#     j=0
#     count=0
#     while j<len(arr):
#         if arr[i]==arr[j]:
#             count+=1
#         j+=1
#     if count==1:
#         max=arr[i]
#     i+=1
# print(max)


# # k,arr = int(input()),list(map(int, input().split()))

# # myset = set(arr)
# # print(arr)


# # print(((sum(myset)*k)-(sum(arr)))//(k-1))
# list=[2,2,3,3,4,5,4,3,]
# # list2=set(list)
# # print(list2)

# import re

# count=int(input().strip())
# for _ in range(count):
#     ans=False
#     try:
#         string=input().strip()
#         number=float(string)
#         ans=True
#         number=int(string)
#         ans=False
#     except:
#         pass
#     print(ans)


# if __name__ == '__main__':
# #     python_student=[]
# #     m=int(input())
# #     for _ in range(m):
# #         list=[]
# #         name = input()
# #         score = float(input())
# #         list.append(name)
# #         list.append(score)
# #         python_student.append(list)
# #     list2=[]
# #     i=0
# #     while i<len(python_student):
# #         if int!=type(python_student[i][1]):
# #             list2.append(python_student[i][1])
# #         i+=1
# #     list2.sort()
# #     i=0
# #     min2=0
# #     while i<len(list2):
# #         if list2[0]<list2[1]:
# #             min2=list2[1]
# #             break
# #         i+=1    
# # i=0

# T=int(input())
# for i in range(0,T):
#     C=int(input())
#     D=int(input())
#     L=int(input())
#     max2=C*4+D*4 
#     min2=(C-D)*2
#     if L%4==0:
#         if max2>=L and min2<=L:
#             print("yes")
#     else:
#         print("no")

# user=input()
# i=0
# count=0
# while i<len(user):
#     if user[i]=="+" or user[i]=="-" or user[i]=="*":
#         count+=1
#     if user[i]>="a" and user<="z" or user[i]>="A" and user<="Z":
#         max="NO"
#         break
#     else:
#         max="Yes"
#     i+=1
    
    
# count=int(input().strip())
# for _ in range(count):
#     ans=False
#     try:
#         string=input().strip()
#         number=float(string)
#         ans=True
#         number=int(string)
#         ans=False
#     except:
#         pass
#     print(ans)

# i=1
# T=int(input())
# while i<=T:
#     A,B=map(int,input().split())
#     count=0
#     j=1
#     while j<=A:
#         k=1
#         while k<=B:
#             sum=j+k
#             if sum%2==0:
#                 count+=1
#             k+=1
#         j+=1       
#     # print(count)
    
    
    
# for i in range(int(input())):
#     k=int(input())
#     ste=list(map(int,input().split()))
#     j=1
#     while j<len(ste):
#         formula=max(0,[ste[j]/2-1])
#         j+=1
# T=int(input())
# if 1<=T<=1000:
#     j=1
#     while j<=T:
#         N=int(input())
#         if 1<=N<=4:
#             C=map(int,input().split())
#             D=list(C)
#             D.sort()
#             D.reverse()
#             count1=0 
#             count2=0
#             i=0 
#             while i<len(D):
#                 if count1<=count2:
#                     count1+=D[i]
#                 else:
#                     count2+=D[i]
#                 i+=1
#             if count1>count2:
#                 print(count1)
#             else:
#                 print(count2)
#         j+=1   

from multiprocessing import Value


T=int(input())
if 1<=T<=10:
    i=1
    while i<=(T):
        N,X=map(int,input().split())
        if 1<=N<=5.10**4:
            if 1<=X<=10**9:
                output=0
                dict={}
                list=[]
                j=1
                while j<=(N):
                    S,R=map(int,input().split())
                    if 1<=S<=10**9:
                        if 1<=R<=10**9:
                            if X>=S:
                                s=S
                                r=R
                                if s<=X:
                                    list.append(s)
                                    dict[s]=r
                    j+=1
                output=max(dict.values())
                print(output)       
        i+=1
                                  
      