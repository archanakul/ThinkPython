#PROGRAM - 26

"""
Takes a list & modifies it, removing the first & last elements, & returns None.
1. Pass a list to a function, the function gets a reference to the list. 
   If the function modifies a list parameter, the caller sees the change. 
"""
def chop(seq):
    #seq.pop()
    #seq.pop(0)
    
    del seq[len(seq) - 1]
    del seq[0]
    

"""
Takes a list & returns a new list that contains all but the first & last elements.
1. SLICING operator creates a new list & the assignment makes the list(seq)     
    refer to it, hence none of that has any effect on the list that was passed 
    as an argument
"""

def middle(seq):
    seq = seq[1:len(seq)-1] #Seq now refers to a new list object
    return seq
    
list1 = list('Archana')
print list1, middle(list1), list1

print list1, chop(list1), list1