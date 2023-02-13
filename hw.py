# # que 1-write a python program to find cube of each and every element inside a list and return the cube on form of list.
# ls = [5,7,9,10,12,15,19,25,23]

# #cube=[0]*len(ls)

# c = []

# for i in range(len(ls)):









#     #cube[i]=ls[i]**3

#     c.append(ls[i]**3)




# print("cube=" ,c)

# #print(c)

# def sq(num):
#     return num**2

# lst=[2,3,4,5]
# square=list(map(sq,l st))
# print(square)



# #Que 2-write a python program to separate negative integer from a list.
# l = [-1,2,-5,8,7,58,-9,14,65,-88,20,35]

# positive=[]

# for i in range(len(l)):

#     if(l[i]>0):

#         positive.append(l[i])

   

# print("positive="+str(positive))




# # #question 3write a python program to find odd or even no from the list create  a new list if number is odd then add False or number is
# # even then add True inside
# # new list.

# l = [10,20,25,45,77,85,65,36,75,96,45]



# positive=[]

# for i in range(len(l)):

#     if(l[i]%2==0):

#         positive.append(True)

#     else:

#         positive.append(False)
# print("od_even=",positive)

# #8-7-22
# #que 1 repeated vowels in string.
# st ='''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
# '''
# ac = 0
# ec = 0
# ic = 0
# oc = 0
# uc = 0
# for i in st:
#     i =i.lower()
#     if i == "a":
#         ac+=1
#     elif i == "e":
#         ec+=1
#     elif i == "i":
#         ic +=1
#     elif i== "o":
#         oc+=1
#     elif i == "u":
#         uc+=1

# #print("a="+str(ac)+"," + "e="+str(ec)+","+"i="+str(ic)+","+"O="+str(oc)+","+"u="+str(uc))  

# Que 5- Write a python function to calculate the factorial of no with non-negative integer,The function accept the no as an argument.
#if the no is negative the return value is invalid.








# from curses.ascii import isdigit
# import re
# def st(text):
#     ptr=r"^a.+b$"
#     x=re.findall(ptr,text)
#     return x

# x1 =st("adsf rof afjsdb")
# x2=st("dsf rof")
# x3 =st("adsb")
# print(x1)
# print(x2)
# print(x3)


# data="hello pn python lec pythoon"
# ptr =r"^p\w*n$"
# #pt=r"p*n"
# x=re.findall(ptr,data)
# print(x)


# data1 ="hello class class"
# ptr2=r"class$"
# ptr3=r"hello$"
# x=re.findall(ptr2,data1)
# print(x)


# from functools import reduce
# ls=[2,3,4,5,6]
# add=reduce(lambda a,b:a+b,ls)
# print(add)
# gt=reduce(lambda a,b: a if a>b else b,ls)
# print(gt)








# import re
# def findno(data):
#     ptr=r"[6-9]\d{9}"
#     x=re.findall(ptr,data)
#     return x

# x1=findno("7894561230,8974563210,235467,98929965153")
# print(x1)
# c=len(x1)
# print(c)

# ###################################

 
# def count_digit(i):

#     counter = 0
#     while i>0:
#         i=i//10
#         counter = counter + 1
#     return counter
# st = '6987654320,953423151,8523121,98989231,3343534231'

# li = st.split(',')
# print(li)

# for i in li:
#     i = int(i)

#     count = count_digit(i)
#     if count==10:
#         print('valid')

#     else:
#          print('invalid')











