#PROGRAM - 12
"""
    1. PALINDROME is a word that is spelled the same backward & forward like 
       "noon" and "redivider"
    2. RECURSIVE function is one which calls itself until the base class return 
       a value & not call itself. This process itself is called as RECURSION   
"""
def first(word):
    return word[0]
    
def last(word):
    return word[-1]  
    
def middle(word):
    return word[1:-1]      
    
def is_palindrome(word):
    if (first(word) != last(word)):
        return False
    elif (len(word) <= 2): #len is a build-in function that returns length of argument passed in
        return True
    else:
        word = middle(word)    
        return is_palindrome(word) 
word = raw_input("Enter the word for Plindrome test: ")

if is_palindrome(word):
    print word + " is a palindrome"
else: 
    print word + " is not a palindrome"                       