#PROGRAM - 17

"""
    1. STRING is a sequence of character enclosed between single/ double quotes
    2. Each element of a string can be access by a BRACKET operator-> INDEXING
    3. INDEX is an offset from the start of the string & hence the index of 
       first letter in a string is always ZERO
    4. INDEX number used to acces each element of a string can be a variable, 
       value or an expression provides it results in in INTEGER
    5. NEGATIVE INTEGERS when used as index, start counting the characer of the 
       sting from the end of the string 
            => string[-1] == string [len-1]
"""
def string_reversal(string):
    index = 0  
    while(index < len(string)) :
       print string[-(index+1)]
       index = index + 1

inp = raw_input("Enter a string to reverse : ")
string_reversal(inp) 

"""
    1. SLICE is a segment of a string
        string[m:n]-> set of characters starting from mth index to nth index     
        including the first but excluding the last
    2. Slice starts at the BEGINNING of string if FIRST index is omitted
            string[:n] -> from start
    3. Slice goes till the END of string if SECOND index is omitted
            string[:n] -> till end
    4. string[:] -> entire string
    5. When second index is GREATER than or EQUAL to first index then we get an     
       EMPTY STRING ('' -> no character & 0 length)
            string[2:2], string[4:3]  
    6. Bracket operator used in string SLICING can have a THIRD PARAMETER (STEP) 
       which indicates number of spaces between characters  
       word[::2] -> string of every other character of word 
       word[::3] -> string of every 3rd character of word 
       word[::-1] -> goes though the string backward          
"""           
print 'string'[2:4],
print 'string'[3:3], 
print 'string'[:6], 
print 'string'[0:],
print 'string'[:]

print "Reverse of string " + inp + " : ", inp[::-1]

"""
    1. Strings are IMMUTABLE objects ->Cant not change a string, the most we can 
       do is to form a new string which is a varient of the original string
"""
greeting = "hello"
# greeting[0] = 'H'
new_greeting = 'H' + greeting[1:]

"""
    1. METHODS are similar to functions i.e they take in arguments & return a     
    result except for the syntax
        find(word,letter, str_index, end_index) -> function call syntax
        word.find(letter, str_index, end_index) -> Method INVOCATION syntax
    2. FIND METHOD searches for a letter/substring starting at start index(if 
       provided else from first character) ending at end index(if provided else 
       till last character) & return index number of first appearance of the 
       character/sub-string   
    3. COUNT METHOD searches for a letter/substring starting at start index(if 
       provided else from beginning) ending at end index(if provided else 
       till end) & return number of appearance of character/sub-string     
"""
print 'banana'.find('an', 1, 6) 
print 'banana'.count('an')

"""
    1. IN BINARY OPERATOPR -> checks for presence of LHS string in RHS string & 
       returns True/False
"""
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter
in_both('apples', 'oranges')    

"""
    1. COMPARISION OPERATOR(= , >, <) work on strings also.
    2. For python all UPPER case letters comes before LOWER case letter. Hence 
       when comparing mixed capital word for arrangement in alphabetical order; 
       Convert strings to common format.   
"""        
word1 = 'apple'
word2 = 'banana'

if word1 < word2:
    print word1 + " comes before " + word2 
elif word1 > word2:
    print word2 + " comes before "+ word1
else:
    print "Both words are the same!"      