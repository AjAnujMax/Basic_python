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


