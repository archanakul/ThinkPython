#PROGRAM - 18

"""
    1. ORD() -> Given a string of length one, return an integer representing the   
       value of the byte
                ord('a') -> 97
    2. CHR()-> Return a character whose ASCII code is the integer i. The 
       argument must be in the range [0..255]
                chr(97) -> 'a'
"""

def rotate_word(word, shift):
    """ To rotate a letter means to shift it through the alphabets, wrapping 
        around to the beginning if necessary, so 'A' shifted by 3 is 'D' & 'Z' 
        shifted by 1 is 'A'. """
    new_word = ''
    while(shift >= 26):
        shift = shift - 26
        
    for c in word:
        if c.islower():
            z = ord('z')
            a = ord('a')
        else:
            z = ord('Z')
            a = ord('A')
        
        if c.isalpha():
            if ((ord(c) + shift) >= a ) and ((ord(c) + shift) <= z) :
                new_word += chr(ord(c) + shift)
            elif (ord(c) + shift) < a :
                new_word += chr(z + (ord(c) - a) + shift + 1)
            elif (ord(c) + shift) > z :
                new_word += chr(ord(c) + shift - z)
        else: 
            new_word += chr(ord(c) + shift)          
      
            
    return new_word

word = raw_input("Enter a word to be rotated: ")
shift = raw_input("Enter the number of shifts: ")
try:
    shift = int(shift)
except:
    print "Shift value need to be integer" 
    quit()
    
print '"' + word + '" shifted by ' + str(shift) + ' times is "' + rotate_word(word, shift) + '"'         