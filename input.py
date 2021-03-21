#-----------------------------------------
#input
print("enter ur number")
number = input()
print(number)

#string to int type cast
print("enter ur marks")
number = int(input())
print(number)


#IF-ELSE

if (number>90):
    grade = 'A'
    
elif (number>80):
    grade = 'B'
    
else:
        grade = 'Dont know'
print("grade is",grade)