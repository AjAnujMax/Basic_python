#-----------------------------------------
#input
print("enter ur number")
number = input()
print(number)
#OUTPUT string
# 10

#string to int type cast
print("enter ur marks")
number = int(input())
print(number)
#OUTPUT int
#10


#IF-ELSE

if (number>90):
    grade = 'A'
    
elif (number>80):
    grade = 'B'
    
else:
        grade = 'Dont know'
print("grade is",grade)
#OUTPUT
#grade is Dont know

#-----------------------------------------------
#IF-ELSE WITH OR AND 

if (number>90 or number>80):
    grade = 'A'
    
elif (number>80 and number<70):
    grade = 'B'
    
else:
        grade = 'Dont know'
print("grade is",grade)
#OUTPUT
#grade is Dont know


#----------------------------------------
#LOOP

#FOR loop
print(" 1 to 10 in number")
for i in range(0,10):
    print(i)
 #OUTPUT 
 # 1 2 3 4 5 6 7 8 9 10 ()all in new lines
print("how many times u wan t to execute")
n = int(input())
for i in range(0,n):
    print(i)
 #OUTPUT 
 #  how many times u wan t to execute
 # 2
 # 0 1
    
    
#for list
list1 = ['item1', 'item2', 'item3']
for item in list1:
    print(item)
 #OUTPUT 
 #item1  item2 item3  
    
#for in for list
list1 = [[1,2,3], [4,5,6],[6,7,8]]
for item in list1:
    for i in item:
        print(item)
#OUTPUT 
# [1, 2, 3][1, 2, 3][1, 2, 3][4, 5, 6][4, 5, 6][4, 5, 6][6, 7, 8][6, 7, 8][6, 7,8]


#----------------------------------------
#while

print("enter the number")
n = int(input())
#output 
#10
while(n>4):
    print("number is greater than 4")
    # output is number is greater than 4
    number = int(input())
    if(number ==9):
        break
    if(number ==8):
        continue
    print("loop ended")
#OUTPUT
# 4 loop ended
    
#----------------------------------------
#function

def average(num1,num2):
    return ((num1+num2)/2)
print(average(2,3))
 #OUTPUT 
 # 2.5


#----------------------------------------
#STRING

string1 = "this is me"
print(string1[0:2])
 #OUTPUT th
print(string1[-2:])
#OUTPUT me
print(string1[:-2])
#OUTPUT this is
print(string1.capitalize())
#OUTPUT This is me
print(string1.find("this"))
#OUTPUT 0
print(string1.find("availabe"))
#OUTPUT -1
print(string1.replace("is","are"))
#OUTPUT thare are me


#----------------------------------------
#FILE I/O HANDLING

#to open the file in write mode
 file1 = open("anuj.txt", "wb") # wb - to write mode
 
 
 print(file1.mode)
 #OUTPUT WB
 print(file1.name)
 #OUTPUT  anuj.txt

 # to replace and write in anuj.txt
 file1.write(bytes("write this to my file","UTF-8")) #to encode in utf-8 
 
 # to close file so that other files can be open latter
file1.close() 



#FILE I/O reading
 file1 = open("anuj.txt", "r+") #  r+ to READ mode
 text_to_read = file1.read()# inbult function read used
 print(text_to_read)
 #OUTPUT :-  print the content of file



#----------------------------------------
#OBJECT ORIENTED PROGRAMMING  class/object/attribute

class Employee:     #class created
    __name = None  # underscore underscore("__") meeans its a private variable and cant access out of class
    __id = 0
    __salary = 0
    def set_name(self,name):  #funtion to check correct data and SELF : 
        self.__name = name    #set name in public variable/attribute
    
    def get_name(self,):  
        return self.__name    #return set name 
        

anuj = Employee() # object created
anuj.set_name('anuj') # set 'anuj' is class variable
print(anuj.get_name())  
#output:- anuj


#----------------------------------------
#class object full example

class Employee:     #class created
    __name = None  # underscore underscore("__") meeans its a private variable and cant access out of class
    __id = 0
    __salary = 0
    
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary
    def set_name(self, name):
       self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__id = salary

    def get_salary(self):
        return self.__salary

anuj = Employee('anuj', 420, 70000000) # object created
anuj.set_name('anuj') # set 'anuj' is class variable
anuj.set_id('01')
anuj.set_salary('80000000')
print(anuj.get_name())  
#output:- anuj
print(anuj.get_id())
#output:- 01
print(anuj.get_salary())
#output:- 8000000

