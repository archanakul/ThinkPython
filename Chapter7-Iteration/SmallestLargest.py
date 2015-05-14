#PROGRAM - 15

"""
    1. "None" is a special value for initial value, same is returned from a 
       function in case there is no explicit return value
    2. Equality operator(==) compare two values but 'is' compares not only the     
       values of the operands but also their data types
    3. Python does not bind variables to hold only one specific data types i.e 
       they are not bound by the data type, their type changes based on the 
       value that they currently hold  
"""

largest = None 
smallest = None
print type(largest), type(smallest)

while True:
    input = raw_input("Enter a number: ") 
    if input == "done" : 
        break  
    try:    
    	num = float(input)
    except:
        print("Invalid Input")
        continue 
    
    if(smallest is None): # "is" operator compares VALUE as well as TYPE
        smallest = num
    elif(num < smallest):
        smallest = num
        
    if(largest is None):
        largest = num
    elif(num > largest):
        largest = num     

print "Maximum", largest, type(largest)
print "Minimum", smallest, type(smallest)