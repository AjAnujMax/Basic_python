college = ['IIT ', ' NIT', 'COLLEGE OF ENGINNERING']
print(college[2])

#   output
#   COLLEGE OF ENGINNERING

#--------------------------------------------------
#To upadate list
college[2]= "COE"

#   output
#    COE

#------------------------------------------------------
#print style
print(college[2]) # print only 2 i.e COE
print(college) # all printed 
print(college[1:3]) # this will skip 1st postion(0 index)

#=================================================
                    # list2

list2 = ['table', 'chair', 'fan', 'clothes', 'bottle' ]

#to add missing item/APPEND LIST
list2.append('microphone')
print(list2)
# OUTPUT
# 'table', 'chair', 'fan', 'clothes', 'bottle', 'microphone'


#----------------------------------------------------------
#to add missing item in mid/ INSERT LIST
list2.insert(2,'phone')
print(list2)
# OUTPUT
# 'table', 'chair', 'fan', 'phone', 'clothes', 'bottle', 'microphone'

#--------------------------------------------------
#to remove item/ REMOVE LIST
list2.remove('chair')
print(list2)
# OUTPUT
# 'table', 'fan','phone', 'clothes', 'bottle', 'microphone'


#--------------------------------------------------
#to add multiple item
print(list2 + ['pillow', 'tubelight', ' bed'] )
# OUTPUT
# 'table', 'fan','phone', 'clothes', 'bottle', 'microphone', 'pillow', 'tubelight, ' bed'

#--------------------------------------------------
#LENGTH OF LIST
print(len(list2) )
# OUTPUT
# 5
