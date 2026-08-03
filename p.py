# name="poorna"
# age=21
# height=6.5
# print(name)
# print(type(age))
# int_height=int(height)
# print(int_height)


# age=99
# if age<= 5:
#     print("ticket free")
# elif age<=12:
#     print("pay  as child")   
# elif age<=18 or age<=60 :
#     print("pay as adult")
# else:
#     print("pay full wages")

# num=int(input("enter a num"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")

# num= int(input("enter a num"))
# for i in range(1,11): 
#  print(f"{num} x {i}={num*i}")

# def add (a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# a=int(input("enter a value"))
# b=int(input("enter b value"))
# print(add(a,b))
# print(mul(a,b))
# print(sub(a,b))   

# fruits=["apple","bannana","cherry"]
# print(fruits[-3])
 
# numbers=[10,20,30,40]
# total=0
# for num in numbers:
#     total=total+num
# print(total)

# numbers=[10,20,30,40]
# double=[]   
# for num in numbers:
#     double.append(num*2)
# print("doubled",double)

# student_marks = {"poorna": 85, "chandra": 90, "tejaswi": 78}
# for student in student_marks:
#     print(student)

# students = ["Anand", "Geetha", "Kumar"]
# marks = [85, 90, 78]
# student_marks={}
# for i in range(len(students)):    
#     student_marks[students[i]]=marks[i]
# print(student_marks)

# class car:
#     def __init__ (self, brand,model) :
#        self.brand=brand
#        self.model=model
#     def dis_info(self):
#          # print(f"car:{self.brand},model:{self.model}")
#        print(f"Car Brand: {self.brand}, Model: {self.model}") 
# my_car= car("mahindra","xuv700")
# my_car.dis_info()


# class dog:
#    def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed
#    def bark(self):
#        print(f"Name:{self.name} , breed:{self.breed}")
# nayi1=dog("rocky","germanshepherd")
# nayi2=dog("chintu","pug")
# nayi1.bark()
# nayi2.bark()

# class human:
#     def __init__(self,name,age):
#           self.name=name
#           self.age=age
#     def walk (self):
#           print(f"Name:{self.name} of,age:{self.age} is walking")

# n1=human("poorna",22)
# n2=human("Alex",20)
# n1.walk()


# abstraction
# class car:
#     def startengine(self):
#         print("engine started")
#     def accelerate(self):
#         print("car started")
#     def brake(self):
#         print("The car stopped")
# c1=car()
# c1.accelerate()
# c1.startengine()

#  encapsulation

# class database:
#     def __init__(self):
#         self.storage={}                here --> if u replace it as __storage then it will be an private attribute where it cant be acessed by other methods
#     def write(self,key,value):
#         self.storage[key]=value
#     def read(self,key):
#         if key in self.storage:
#             print(self.storage[key])
#         else :
#             print("data doesnt exist")
# db=database()
# db.write("name","poorna")
# db.read("name")
# print(db.storage)

# Inheritance
# class user:
#     def __init__(self,username):
#         self.username=username
#     def login(self):
#         print(F"{self.username} logined sucessfully")
# class admin(user):
#     def delete_user(self):
#         print("user has been deleted")
# a=admin("porna")
# a.login()
# a.delete_user()

# polymorphism

# class animals:

#     # def make_sound(self):                       ----->here make_sound is an method that has many forms
#         print("animal is making sound")
# class dog(animals):
#     def make_sound(self):
#         print("bark")
# class cat(animals):
#     def make_sound(self):
#         print("meow")
# anima_l=[dog(),cat()]
# for animal in anima_l:
#     animal.make_sound()

# error and exception handling
# . SYNTAX ERROR ----> MISSING A COLON OR BRACES DURING THE EXECUTION OF THE PROGRAM
#. RUNTIME EXCEPTION --> ERROR OCCURED DURING THE EXECUTION OF THE PROGRAM
# a=int(input("a:"))
# b=int(input("b:"))
# try:
#     print(a/b)
# except Exception as e:
#                                 #  ----------> HERE Exception IS AN CLASS THAT INVOLVE ALL ERROR 
#     print(f"there is an error:{e}")
# else:
#     print("enu error illa")
# finally:
#     print("program ended, if error comes or not i dont care in your program but its executed")


# try:
#     boy= str(input("enter boy name u want to marry?"))
#     if boy!="poorna":
#         print("you shd marry only poorna")
#     else:
#         print("good u have got ur gem")
# except Exception as e:
#     print(f"error:{e}")
# finally:
#     print("make sure u have selected correct gem poorna")


# FILE HANDLING ----> used to read from or wite to a files
# and also used to store data permanently


# file = open ("notes.txt","r")
# content = file.read()
# print(content)
# file.close()
        
    
# Mode
# 'r' Read (default mode)
# 'w' Write (overwrites if file exists)
# 'a' Append (adds content at the end) Add data without deleting old
# 'x' Create (fails if file exists)
# 'b' Binary mode
# 't' Text mode (default)

# file=open("student.txt","a")
# file.write("poorna /n")
# file.write(" rani ")
# file.close()
# try:
#     file.open("employee.txt","x")
#     file.write("poorna")
# except Exception as e:
#     print("error:{e}")
# finally:
#     file.close()
 
# students=["poorna","alex","bob"]
# file=open("class.txt","w")
# for student in students:
#     file.write(f"{student}\n")
# file.close()

# Modules in python 
#  1.math module
# 1. library --> group of packages and modules
# 2. books --> group of match
# 3.paper --> modules--> python file


# name = str(input("what is ur name"))
# age = int(input ("enter ur age"))
# print(f"hello {name},you are {age} years old!")

# a=(input("enter 1st no :"))
# print(int((a)))
# print(float((a)))
# print(str((a)))
# b=int(input("enter 2nd num:"))
# c=float(input("enter one noin float:"))
# avg=(float(a+b+c))/3
# print(avg)
# # sum=(a+b)
# # diff=(a-b)
# # product=(a*b)
# # qu=(a/b)
# # print(sum)
# # print(diff)
# # print(product)
# # print(qu)
# a=int(input("enter 1 no:"))
# b =int(input("enter2nd no"))
# temp=a
# a=b
# b=temp

# print(a)
# print(b)

# a=float(input("enter a no:"))
# print(int(a))
# print((a-int(a)))

# age =int(input("enterur age"))
# if (age < 13):
#     print("u r a child")
# elif (age >=13 and age<=18):
#     print("u r teen")
# elif (age>18 and age<=60):
#     print("u r an adult")
# else:
#     print("u r senior citizen")

# def average(a,b,c):
#   avg=((a+b+c)/3)
#   return avg
   
# print(average(1,2,3))

# def factorial_cal(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# n=int(input("enter a no:"))
# print(factorial_cal(n))


# salary=int(input("enter  ur salary:"))
# if salary<30000:
#     print("tax rate is 5 %")
# elif salary>=30000 and salary<=70000:
#      print("tax is 15 %")
# elif salary>70000:
#      print("ur tax is 25%")

# def even_num(a,b):
#     i=0
#     for i in range (a,b+1):
#         if i % 2==0:
#             print(i)
#         i=i+1
#         continuec
    
# even_num(1,11)

# def print_dig(n):
#     for i in str(n):
#         print(i)
 
# n=int(input('enter a num :'))
# print_dig(n)

# def count_digit(n):
#     count=0
#     for i in str(n):
#         count+=1
#     return count
# print(count_digit(25))

# def sum_digits(n):
#     total=0
#     for digit in str(n):
#      total =total +int(digit)
#     return total
    
   
# print(sum_digits(29))

# def print_num():
#     for i in range(1,101):
#         if i%3==0 and i%5 ==0:
#           print(i)
#           i+=1

# print_num()

# while True:
#     n = input("enter a no:")
#     if n == "quit":
#         print("program end")
#         break
#     n = int(n)
#     if n > 0:
#         print("no is positive")
#     elif n < 0:
#         print("no is negative")

# def calculator(a, b, operation):

#     if operation == "add":
#         print(a + b)

#     elif operation == "sub":
#         print(a - b)

#     elif operation == "mul":
#         print(a * b)

#     elif operation == "div":
#         print(a / b)

#     else:
#         print("Invalid operation")


# calculator(8, 6, "add")

# def is_prime(n):
    
#     for i in range(2,n+1):
#         if n%i==0:
#             print("not prime")
#             return False
#         return True
# print(is_prime(7))
# num=255
# for i in range(3):
#     guess_num=int(input("guess the num"))
#     if guess_num>num:
#       print("too high")
#     elif guess_num<num:
#        print("too low")
#     elif guess_num==num:
#        print("congrats,ur guess is correct")

# nums=[1,20,30,80]
# x=20
# index=0
# for n in nums:
#     if(n==x):
#         print(f"{x} found at index {index}")
#         break
#     index+=1

# students = [
#     ("Rahul", "Maths"),
#     ("Anita", "English"),
#     ("Rahul", "English"),
#     ("Anita", "Computer"),
#     ("Arjun", "Physics"),
#     ("Rahul", "kannada"),
# ]
# dict={}
# for name,course in students:
#    if dict.get(name)==None:
#       dict.update({name:set()})
#       dict[name].add(course)
# print(dict)

# user_name=str(input("enter a string"))
# rev=""
# for i in user_name:
#     rev= i + rev
# if user_name==rev:
#     print("palindrome")
# else:
#     print("not palindrome")
      
# list_num=[10,20,30]
# for i in list_num:
#     avg=(sum(list_num))/len(list_num)
# print(int(avg))  

# list_1=list(map(int,input("enter list").split()))
# list_2=list(map(int,input("enter list2").split()))
# res= list_1+list_2
# res.sort()
# print(res)

# tup=(1,2,3,4,5)
# tup_e=()
# tup_o=()
# for n in tup:
#     if n%2==0:
#         print("even")
#         tup_e+=(n,)
#     else:
#         print("odd")
#         tup_o+=(n,)
# print("all are sorted")

# students={}
# while True:
#     print("a-add student")
#     print("b-update student")
#     print("C - Search Student")
#     print("d- Display All Students")
#     print("e - Exit")
# choice =input("enter ur choice:")
# if choice=='a':
#     name=input("enter student name:")
#     marks=int(input("enter ur marks:"))
#     student[name]=marks
#     print("student added")
# elif choice=='b':
#     name=input("enter ur name")
#     if name in students:
#         marks=int(input("enter ur marks"))
#         student[name]=marks
#         print("marks updated")
#     else:
#         print("user name not found")
# elif choice =='c':
#         name=input("enter student name to be searched:")
#         if name in students:
#             print(students[name])
#         else:
#             print("not found")
# elif choice=='d':
#      print("all items")

class employee:
    start_time='10am'
    end_time='6pm'
class admin_staff(employee):
   
    def __init__(self,name):
      self.name=name

class Teacher(admin_staff):
    def subject(self,sub):
        self.sub=sub
    def admin(self):
        print('name:',self.name)
        print('sub',self.sub)
        print('start',self.start_time)

t1=Teacher("poorna")
t1.subject("python")
t1.admin()

    hibro