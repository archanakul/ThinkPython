# Program 9

"""
    Fermat’s Last Theorem says that there are no integers a, b, and c such that
            a**n + b**n = c**n
    for any values of n greater than 2.
"""

def check_fremont(a,b,c,n):
    RHS = c ** n
    LHS = (a ** n) + (b ** n)
    if (n > 2) and (RHS == LHS):
        print "Fermat was Wrong!"
    else:
        print "Fermat was Right"
            
input_a = raw_input("Enter value of A in Fremat last Theorem :\n")
input_b = raw_input("Enter value of B in Fremat last Theorem :\n")    
input_c = raw_input("Enter value of C in Fremat last Theorem :\n")
input_n = raw_input("Enter value of n in Fremat last Theorem :\n")
try:
    a = int(input_a)
    b = int(input_b)
    c = int(input_c)
    n = int(input_n) 
except:
    print "Non- integer value is illegal"
    quit()
check_fremont(a, b, c, n)