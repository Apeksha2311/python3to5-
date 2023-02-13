

# Ex 1 take user input and give randon value to print
# a = int(input("Enter a value:"))
# for i in range(a):
#     print(i)
# print()

#Ex 2 using for loop print 10 to 1
# for i in range(10,0,-1):
#     print(i)
# print()


# # ex-3print even no using for loop
# s=int(input("Enter a value:"))
# for i in range(2,s+1,2):
#     print(i)

# Ex 4print odd no using for loop
# d = int(input("Enter a value:"))
# for i in range(d-1,1,-1):
#     print(i) 

#Ex -5 print ur name using for loop

# for i in range(0,11,2):
#     print(i,"Apeksha") 



#ex-7 factorial of no using for loop

# n=int(input("Enter a value:"))
# fact = 1
# for i in range(n,0,-1):
#     fact=fact*i
# print(fact)











# n=int(input("Enter a value:"))
# for row in range(0,n,1):
#     for col in range(0,row,1):
#         print(" ",end =" ")
#     for col1 in range(0,n-row,1):
#         print("*",end = " ")
#     print()





# n=int(input("Enter a value:"))
# for row in range(0,n-1):
#     for col in range(0,row):
#         print(" ",end =" ")
#     for col1 in range(0,row+1-n,-1):
#         print("*",end = " ")
#     print()


#Write a program to print first 10 even number

# #a = int(input("Enter a value:"))
# for i in range(18,-1,-1):
#     if i%2==0:
#         print(i)

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

# for i in range(0,5,1):
#     for j in range(0,5-i,1):
#         print(5-i,end=" ")
#     print() 


#convert the following loop into for loop
# x = 4
# while(x<=8):
#     print(x*10)
#     x+=2

# x=4
# for i in range(4,9,2):
#     print(i*10)


# #sum of no in given list without for loop
# ls=[1,2,3,4,5,6,7,8,9,10]
# print(sum(ls))

##sum of no in given list using for loop
# s=[1,2,3,4,5,6,7,8,9,10]
# c=0
# for i in s:
#     c+=i
# print(c)

##sum of no in given list without using for loop
# s=[1,2,3,4,5,6,7,8,9,10]
# c=0
# i=0
# while (s):
#     c+=1
# print(c)




# n=int(input("Enter no:"))
# for row in range(0,n+1,1):
#     for col in range(0,row,1):
#         print("*",end=" ")
#     print() 

# n=int(input("Enter no:"))
# for row in range(0,n+1,1):
#     for col in range(0,n+1,1):
#         print("*",end=" ")
#     print()

# n=int(input("Enter no:"))
# for row in range(0,n,1):
#     for col in range(0,n-row,1):
#         print("*",end=" ")
#     print()



# n=int(input("Enter no:"))
# for row in range(1,n+1,1):
#     for col in range(1,row,1):
#         print(col,end=" ")
#     print() 

# n=int(input("Enter no:"))
# for row in range(0,n+1,1):
#     for col in range(0,row,1):
#         print("*",end=" ")
#     print()

# for row1 in range():
#     for col1 in range()

# n=int(input("Enter no:"))
# for row in range(0,n+1,1):
#     for col in range(row):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()

# n=int(input("Enter no:"))
# for i in range(0,n,1):
#     for j in range(n-i-1):
#         print("-",end=" ")
    
#     for j1 in range(i+1):
#         print("*",end=" ")
#     print()



# n=int(input("enter no:"))
# for i in range(n):
#     for j in range(i-1+1):
#         print("-",end=" ")
#     print()    
#     for j1 in range(n-i):
#         print(i,end=" ")


# n=1
# for i in range(1,20,2):
#     print(i)

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1): 
#         print(j,end='')
#     print()


# for i in range(n):
#     for j in range(n-i):
#         print(j,end='')
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(n,end='')
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(i,end='')
#     print()    

# for i in range(n):
#     for j in range(n-i):
#         print(n-j,end='')
#     print() 


# d={1:'asd',2:'dfg',3:'ert'}
# for k,v in d.items():
#     print(k,v)


# #print 1,3,5,9,11,15
# n=15
# for i in range(1,n+1,2):
#     if i==7 or i==13:
#         continue 
#     print(i)


# color=['yellow','black','green','purple']
# for x in color:
#     print(x)
#     if x=='green':
#         break   
# else:
#     print("Done!")        


# list_num=[2,4,6,5,8,10]
# for i in list_num:
#     if i%2 !=0 :
#         print('odd numbers are also there')
#         break
# else:
#     print('all are even')




#exception handling




# a=int(input('Enter a value:'))  
# b=int(input('Enter b value:')) 
# d=[9,6,7,8]
# try:
#     c=a/b
#     print(c)
#     print(d[0])
#     print(d[10])



# except IndexError as e:
#     print('IndexError')   

    
# except ZeroDivisionError :
#     print('ZeroDivisionError: division by zero')    



# #to do:
# #file handling
# duck typing
# decorator
# built in module
# function
# oops
# regex
#comprehension
#mysql

#file handling
import os
from unittest import FunctionTestCase

file=open('demoFile.txt',"r")
print(file)
print(file.read())
file.close()


with open('demoFile.txt',"r") as f:
    print(f.read()) 

# with open('demoFile.txt',"w") as f:
    
#     print(f.write('sal:23000')) 
print('s')

# with open('demoFile.txt',"a") as f:
    
#     f.writelines('\nsal:23000')    

# print('a')

# with open('demoFile3.txt',"a") as f:
#     print(f.tell())
    

#     f.writelines('\nsal:23000')   
#     print(f.tell())


#duck typing
def snap(func):
    def inner():
        print('Apply filters and click pic')


        return func 



    return inner

@snap
def camera():
    print('click pic')

camera()


def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a



        return func(a,b)

    return inner




@smartdiv
def div(a,b):
    return a/b

print(div(4,12))    


#duck typing
class train:
    def runs_on(self):
        print('Runs on track')

class car:
    def runs_on(self):
        print('Runs on Road') 

class Airoplane:
    def runs_on(self):
        print('Fly in Air')


def asd(vehicle):
    vehicle.runs_on()



local=train()
nano=car()
AirIndia=Airoplane()    


asd(local)
asd(nano)
asd(AirIndia)








      



  
       