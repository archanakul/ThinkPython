#PROGRAM - 11

""" 
Ackermann function A(m,n) is defined as:
    A(m,n) = n+ 1               if  m = 0
              A(m-1,1)          if m > 0 and  n = 0    
              A(m-1,A(m,n-1))   if m > 0 and  n > 0
"""

def ackermann_fuc(m,n):
    if (m == 0):
        return (n + 1)
    elif (m > 0):
        if ( n == 0):
            return  ackermann_fuc(m-1,1)
        elif (n > 0):
             return  ackermann_fuc(m-1,ackermann_fuc(m,n-1))
             
print "Ackermann function value: ", + ackermann_fuc(3,4)             