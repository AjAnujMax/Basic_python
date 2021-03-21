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
