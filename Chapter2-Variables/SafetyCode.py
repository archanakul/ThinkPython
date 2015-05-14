# PROGRAM - 5

"""
    1. TRY/EXCEPT block is one way of safe programming - when anticipate/expect errors             
       from  other users. They are like buying insurance to life guard program execution 
       to continue even when there is an error which you had anticipated. 
"""    
try:
    hours = raw_input("Enter total hours worked:") # return value of raw_input is a string
    ihours = float(hours) # Error could occur is the user into is not a number
    rate = raw_input("Enter per hour pay:")
    irate = float(rate) # Error could occur is the user into is not a number
except:
    print "Incorrect inputs!! \nEnter Numeric inputs please"
    quit() #STOPS further execution of program
    
if (ihours <= 40):
    payment = ihours * irate
else:
    payment = (40 * irate) + (ihours-40) * irate * 1.5
print "Your payment is:", payment    
  
        
    