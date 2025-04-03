my_set={1,2,1,3,33,3}
print(my_set)
# -------------------------------- 
mylist=[1,2,2,3,2,2]
print(mylist)

mylist=[1,3,"a","d",3,"a"]
print(mylist)

_list=[2,4,"python","e","a"]
print(_list)
# -------- mutable ------------------------ 

# my_list=[4,2,3,4,55]
# print(my_list)
# my_list[0]=44
# print(my_list)
# my_list=[1,2,3]
# print(my_list)

# ------------ indexing -------------------- 

# my_list=[1,2,3,44,55,66,77]
# print(my_list)
# print(my_list)
# print(my_list[3])
# print(my_list[-1])
# print(my_list[-6])

# ------------------- append ------------- 

my_list=[1,2,3,44,55,66]
print(my_list)
my_list.append(77)
print(my_list)

#---------------extend----------------

my_list=[1,2,3,44,55,66]
print(my_list)
my_list.extend([77,88,99])
print(my_list)

#--------------insert------------

my_list=[1,2,3,4,55,66,77]
print(my_list)
my_list.insert(3,33)
print(my_list)

#-------------remove---------

my_list=[1,2,3,44,55,66,77]
print(my_list)
my_list.remove(3)
print(my_list)

#--------------pop(index)-----

my_list=[1,2,3,44,55,66,77,3]
print(my_list)
my_list.pop()
print(my_list)   
my_list.pop(3)
print(my_list)
my_list.pop(0)
print(my_list)

# ---------clear-----
# numbers=[1,2,2,3,3]
# print(numbers)
# numbers.clear()
# print(numbers)

#---------index(item)---

# numbers=[1,2,2,3,3]
# print(numbers.index(2))
# print(numbers.index(3))

#---------count------

# numbers=[1,2,2,3,4,5,5]
# print(numbers.count(5))

#-------sort------

# numbers=[1,44,4,6,55]
# print(numbers)
# numbers.sort()
# print(numbers) 

# numbers=[1,2,55,44,3,66]
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

#--------

# a=10
# b=3
# if(a>b):
#     print("a is grater")
# else:
#     print("b is greatre ")

#---------------reverse-----------------

# num=[1,2,3,4,5]
# print(num.reverse())

# num=[1,2,3,4,5]
# copy_list=num.copy()
# print(copy_list)
# print(num)

#--------------slicing------------------

# num=[1,2,3,4,5,6,7,8,9,10]
# print(num[1:5])
# print(num[::])
# print(num[:-3])
# print(num[-3: ])
# print(num[::2])
# print(num[::-1])
# print(num[::-2])

#-------------if-elif-else-----------------

# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
# c=int(input("enter the third value"))
# if(a>b and a>c):
#     print("a  is greater")
# elif(b>a and b>c):
#     print("b is greater")  
# else(c>a and c>b):
#     print(" c is greatest")

#------------------nested if-----------------

# income=50000
# credit_score=700
# emp_status="employee" 
# if(income>=40000):
#     if(credit_score>=650):
#         if(emp_status=="employee"):
#             print("you are eligible for loan!")
#         else:
#             print("you need to be employee to get loan")
#     else:
#         print("your credit score is too low for the loan")
# else:
#     print("your income is too low to qualify for the loan")       





# income=(input("enter first value"))
# credit_score=(input("enter second value"))
# emp_status=(input("enter employed or not"))
# if(income>=40000):
#     if(credit_score>=650):
#         if(emp_status=="employee"):
#             print("you are eligible for loan!")
#         else:
#             print("you need to be employee to get loan")
#     else:
#         print("your credit score is too low for the loan")
# else:
#     print("your income is too low to qualify for the loan")    
  
     
# x=int(input("enter the value value"))
# if(x%2==0):
#     print("x is even no.")
# else:
#     print("x is odd no.")


year=int(input("enter year:"))
if(year%4==0):
    print("leap year")
else:
    print("not a leap year")


