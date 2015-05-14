#PROGRAM - 45

"""
    1. TUPLES can be called as IMMUTABLE LISTS as they are mostly like lists i.e 
       they are a sequence of data elements(any type), are indexed by integers & 
       are enclosed in round brackets()
    2. Empty tuple is created by the built-in function TUPLE(). Additionally if 
       argument to this function is sequence (string/list/tuple) then the output 
       is a tuple with elements of sequence
    3. Since round brackets around are options but mostly used, SINGLE ELEMENT 
       tuple ends with a COMMA 
    4. List OPERATORS - INDEX, SLICE also operate in the same way on tuples but 
       the ASSIGNMENT operates a lil different. Since tuples are immutable, 
       assignment operator does not work on the tuple elements but works on the 
       tuple itself i.e elements cant be modifies once assigned but the tuple 
       itself can be assigned with some other tuple altogether.  
    5. In case of ASSIGNMENT, expression on the RHS is evaluated before any 
       assignment hence SWAPING to 2 variable values can be done with no 
       additional temporary variable.  
                    a,b = b,a      or      (a,b) = (b,a)
    6. Tuples enable function to RETURN MULTIPLE VALUE  
    7. GATHER/SCATTER :
        A PARAMETER name that begins with '*' GATHERS arguments into a tuple  
        Can combine GATHER operator with REQUIRED & POSITIONAL arguments:  
        
        A sequence of values can be passed to a function as multiple arguments 
        using '*' SCATTER operator  
        
    8. ZIP(*iteratable) built in function returns an iterator of tuples, where 
       the i-th tuple contains the i-th element from each of the argument 
       "iterables". Iterator stops when shortest input iterable is exhausted 
       
    9. ENUMERATE(iteratable, start = 0) returns a tuple containing a count 
       (from start which defaults to 0) & the values obtained from iterating 
       over iterable. "iterable" must be a sequence(an iterator). 
       
    10. COMPARISION OPERATORS: Starts by comparing the first element from each 
        sequence. If they are equal, it goes on to the next elements, and so on, 
        until it finds elements that differ. Subsequent elements are not 
        considered (even if they are really big).
                (0, 1, 2000000) < (0, 3, 4) -> TRUE
  
         
       
"""
t1 = (1.5,'abc',[1,2,3])
print t1, type(t1)

t2 = tuple()
print t2, type(t2)

t3 = tuple(['a','b',1])
print t3, type(t3)

t3 = tuple([t1])
print t3, type(t3)

t4 = 'a',
t5 = 'a'

print t4, type(t4), t5, type(t5)

# t1[1] = 'ABC' # TypeError
t1 = (t1[0],'ABC',t1[2],'xyz') # RHS is a tuple expression that is computed before any assignment, LHS is a tuple variable
print t1

addr = 'archanakul@gmail.com'

username, domain = addr.split('@')
print username, domain

# Function with 2 return values
def min_max(t):
    return max(t), min(t) 
max, min = min_max([3,54,6,78,3,91,2,58,6548])
print max, min

# Function with variable length arguments
def pointless(required, optional=0, *args): 
    print required, optional, args
pointless(1) # required are provided
pointless(1,2) # required & optional are provided
pointless(1,2,3) # required, optional & single arg is provided
pointless(1,2,3,4)  # required, optional & multiple args are provided 

pointless(t1) #t1 is taken as a single tuple argument -> required
pointless(*t1) # SCATTER - element of tuple are taken as multiple arguments -> required, optional & args

#GATHER version
def sum_all(*nums):
    return sum(nums)
    
print sum_all(3,54,6,78,3,91,2,58,6548)

#SCATTER version
def sum_all(*t):
    return sum(t)

t = [3,54,6,78,3,91,2,58,6548]   
print sum_all(*t)

# ZIP with lists
x = [0, 1, 2]
y = ['a', 'b', 'c']
zipped = zip(x, y)
print zipped

x2, y2 = zip(*zip(x, y))#GATHER/SCATTER
print list(x2), list(y2)

# Traversing two (or more) sequences at the same time by combine zip(), for loop & tuple assignment
for index, letter in zip(x,y):
    print index, letter

#ENUMERATE with list string

for index, letter in enumerate('abcd'):
    print index, letter
    

# ZIP with Dictionary
d = dict(zip('abcde', range(5))) # leaves out 'e' if range(4) is 2nd iterator
for key, value in d.items(): # traversing keys & values of a dictionary by combining items(), for loop & tuple assignment

    print key, value


directory = dict()
directory['Archu','Kul'] = 5104746098

for first, last in directory:
    print first, last, directory[first, last]
    