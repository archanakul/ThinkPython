#PROGRAM - 16

"""
    1. Suppose we need to compute square root of A with an estimate of x then a 
       new better estimate for root of A would be determined by Newtons formula:
                y = (x + A/x)/2
    2. Floating point values rae only approximately right; hence rational 1/3 & 
       irrational number root(2) can not be represented directly using floats.
    3. abs() -> Buil-in function to compute the absolute value or magnitude of 
       difference between floating point values. 
    4. COMMA at the end of a print statement enable the result of next line also 
       to be printed on the same line which other wise comes on the new line as 
       each print statement introduces a new line at the end of it.   
                    
"""
import math
x = 1.0
epsilon = 0.0000001
def NewtonRoot(num):
    global x, epsilon
    while (True):
        y = (x + num/x)/2
        if (abs(y - x) < epsilon):
            break
        x = y
    return y    

while(True):
    num = raw_input("Enter a number to compute Square Root: ")
    try:
        num = float(num)
        break
    except:
        print "Enter a number!!"
        continue

print str(num) + '    ',
print str(NewtonRoot(num)) + '    ',
print str(math.sqrt(num)) + '    ',
print str(abs(NewtonRoot(num) - math.sqrt(num))) 
        
           