#PROGRAM - 31

import random
def has_duplicates(bday_list):
    """ Takes a list & returns True if there is any element that appears more 
        than once """ 
    lst = bday_list
    for bday in bday_list:
        lst.remove(bday)
        if bday in lst:
            return True
    return False                    

def bday_generator(): 
    """ generate random bdays with the randint function in random module. """
    bday = list()
    
    month = random.randint(1,12)
    year = random.randint(1900, 2000)
        
    if month in [1,3,5,7,8,10,12]:
            day = random.randint(1,31)
    elif month in [4,6,9,11]:
            day = random.randint(1,31)
    else:
        if (year % 400 == 0) or(year % 4 == 0 and year % 100 != 0):
            day = random.randint(1,28)
        else:
            day = random.randint(1,27) 
                   
    bday = [month,day,year] 
    return bday       

count = raw_input("Enter the number of students in a class: ")
count = int(count)
bdays = list()
for i in range(count+1):
    bdays.append(bday_generator())    

if has_duplicates(bdays):
    print bdays