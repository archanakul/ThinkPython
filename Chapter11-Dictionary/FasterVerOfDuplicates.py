#PROGRAM - 42
"""
    1. FROMKEYS(seq[values]): Create a new dictionary with keys from seq & 
       values set to value. "value" defaults to None  
                        dict.fromkeys(seq[values])                       
"""

def remove_duplicates(lst):
    """ Takes a list & returns a new list with only the unique elements from the 
        original """    
    none_dup = dict().fromkeys(lst)
    return none_dup.keys()
	
print remove_duplicates([1,2,3,2,1,4,2])