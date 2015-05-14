#PROGRAM - 23

"""
    Test all the six-digit numbers and print any numbers that are palindrome
    1. 3rd parameter in SLICING specifies the distance between consecutive 
       index, when it is made -1 then it simple reverses the actual string
"""
def is_palindrome(reading, size):
    i = 0
    while i < size/2:
        if reading[i] != reading[-i - 1]: # indexing in opposite directions
            return False
        i += 1
    return True
    
def has_palindrome(reading,index,length):
    
    reading = str(reading)[index:index+length]
    return reading == reading[::-1]   
    
def check_puzzle(i):
    return (has_palindrome(i, 2, 4)   and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6)) 

size = raw_input("Enter the length of the palindrome needed: ")             
print "All the Palindromic number of length " + size + ": "

size = int(size)

lower_limit = int('1' + '0'*(size-1))#100000
upper_limit = int('9' * size) # 9999999

while(lower_limit <= upper_limit):
    if check_puzzle(lower_limit):
        print lower_limit
    lower_limit += 1    


