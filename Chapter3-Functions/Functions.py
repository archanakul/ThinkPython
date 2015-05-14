#PROGRAM - 6

"""
    1. Function definition - Like recording an operation for later use, takes in 
       arguments & returns result
    2. def - marks definition of a function
    3. : - marks end of function header & beginning of indentation (body)
    4. Defining a function creates a variable with a same name whose value is         
       FUNCTION OBJECT & type is 'function'
"""

# lang - input parameter based on which behaviour of function is decided; this is the name used within the function to refer to a value passes in as argument by function call
def greet(lang): # VOID FUNCTION - has no return value
    if lang == 'es':
        print "Hola\n"
    elif lang == 'fr':
        print "Bonjour\n" 
    else: 
        print "Hello\n"  
    
language = raw_input("Enter a language - es,fr,en :\n")
greet(language)  #Function invokation with an argument 'language'
print greet, type(greet)


# Once any one of multiple returns is hit, called function terminates
def greeting(lang): # FRUITFUL FUNCTION - has a return value
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour" 
    else: 
        return "Hello"  
    
language = raw_input("Enter a language - es,fr,en :\n")
print greeting(language), 'Glenn' # function must be defines before being used else we get a NameError message.