#PROGRAM - 10

"""
    If any of the three lengths is greater than the sum of the other two, then 
    you cannot form a triangle. Otherwise, you can.
"""
def is_triangle(side1,side2,side3):
    cond1 = side1 > (side2 + side3)
    cond2 = side2 > (side3 + side1)
    cond3 = side3 > (side1 + side2)
    
    if (cond1 or cond2 or cond3):
        print "Trinagle can not be formed"
    else:
        print "Trinagle can be formed"
        
input1 = raw_input("Enter length of Stick1: ")
input2 = raw_input("Enter length of Stick1: ")        
input3 = raw_input("Enter length of Stick1: ")

try:
    side1 = int(input1)
    side2 = int(input2)
    side3 = int(input3)
except:
    print "invalid value for Stick length"
    quit()
    
is_triangle(side1, side2, side3)        