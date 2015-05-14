#PROGRAM - 2

# Operators are special symbols that represent computations

# There are basically two types of numeric data types - integer & floating point
# Comma separated sequence of data is printed out with spaces between each data
print 3,-5,56.98,-45.56

# Pre-defined function(type) prints out data type for the input parameters
print type(5.0), type (5)

# Python has pre-defined functions for EXPLICIT DATA TYPE CONVERSIONS - INT(truncates decimal part ),FLOAT(adds a decimal point followed by 0)
print int(56.98), float(4) 

# Floating point numbers have 15 decimal digit accuracy in python
print 3.1415926535897932384626433832795028841971 #3.141592653589793

# Arithmetic Operators in Python include - +(Addition), -(Subtraction), * (Multiplication), / (Devision-Quotient), ** (Power to), % (Modulus -remainder)
print (1+3), (5-6), (5*2), (2**4)

#P ython 2 division varies for integer division & floating point divisions
print (25/4) 
print (25.0/4), (25/4.0), (25.0/4.0) 

# Operator - // is forced integer division(FLOOR DIVISION- chops off the fractional part) in python 2 but the output type depends on the data itself!!
print  25//4, type(25//4)
print (25.0//4), type(25.0//4)

# Modulus operator divides two numbers & returns the remainder & the output type again depends on the type of input types
print 25%4, type(25%4)
print 25.0%4.0, type (25.0%4.0)

# when SIGNED integer division is done then the values are rounded up(smallest negative number is a bigger figure) otherwise they are rounder down 
print (-9/4), (9/4)

# Expression - Combination of operators & operands
# Arithmetic Operator precedence-PEMDAS or Left to Right-(),** , * & / , + & -

# Arithmetic operators that work on strings are + (concatenation) & *(repetition)
print "Arch" + "ana"
print "hola" * 2

print (4.0/3) * 3.14 * (5**3)

start_sec = (6*60+52)*60.0 # 6:52 am
easy_sec = (8*60+15)*2.0 # 2 miles, each with 8min,15 Secs
fast_sec = (7*60+12)*3.0 # 3 miles, each with 7 min, 12 secs
finish_hour = (start_sec + easy_sec + fast_sec)//(60*60)  
finish_minute  = (((start_sec + easy_sec + fast_sec)/(60*60)) - finish_hour)*60.0
print 'Finish time was', int(finish_hour) , ':', int(finish_minute) # 7:30 am return


