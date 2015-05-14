# PROGRAM - 4

"""
    1. FLOAT is a pre-defined function which converts input parameter to floating point number, 
       Similarly we have INT() & CHAR() too
    2. VARIABLE NAMES can contain A-Z/a-z,0-9,_ characters but they must always begin with 
    either a letter or an _ but not a number
"""

no_of_hours = raw_input("Enter no of working hours:")
per_hour_rate = raw_input("Enter per hour rate:")

total_pay = float(no_of_hours) * float(per_hour_rate)

print "Your Pay is:",total_pay