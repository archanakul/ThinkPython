#PROGRAM - 39

"""
    1. MEMO is a previously computed value that is stored for later use
    2. Fibonacci series
        Fn = Fn-1 + Fn-2
        where F0 = 0 & F1 = 1
    3. GLOBAL VARUABLE: is the one which is defined in the __main__frame i.e 
       outside all the functions in the file. they are called global since they     
       are accessable to all the function of the program while the variables 
       defines inside a function are called LOCAL as they come into life in 
       invoking the functions and vanish when the function end.
       
    4. Thought the global variables can be accesses within any function, they     
       cannot be modified unless they have been declared under the function 
       modifies it as a global variable. This Help in differentiating global 
       variable from local variable.
       
    5. MUTALBLE GLOBAL variable (LIST/DICTIONARY) can not only be accessed by 
       all the function but can also ADD/REMOVE/REPLACE elements but if we need 
       to REASSIGN the VARIABLE itself( DICTIONARY/LIST variable & not just 
       ELEMENTS) then we will have to declare these variables in the function 
       where they are needed to be reassigned.    
    
        
"""
known = {0:0, 1:1}
count = 0
def dict_fibonacci(n):
    global count #Non-Mutable variable
    if n in known:
        count += 1
        return known[n]
    res = dict_fibonacci(n-1) + dict_fibonacci(n-2)
    known[n] = res # Dictionary is a mutable variables
    return res
        
print dict_fibonacci(500), count