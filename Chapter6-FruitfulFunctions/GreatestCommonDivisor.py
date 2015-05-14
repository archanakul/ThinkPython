#PROGRAM - 13

"""
    1. GCD of two numbers is that largets number which can divide both the     
       number with zero remainder. 
       Euclid's algorithm:
            rem = num/den
            repete until rem == 0
             num = den
             den = rem
       
"""
def gcd(x,y):
    num = x
    den = y
    if (x < y):
       return gcd(y,x)
    rem = num % den
    print rem
    if rem != 0:
        return gcd(den, rem)   
    else:
        return den
        
x = raw_input("Enter 1st Number: ")
y = raw_input("Enter 2nd Number: ")

z = gcd(int(x),int(y))  

print "GCD of " + x + " & " + y + " : " + str(z)            
    
            