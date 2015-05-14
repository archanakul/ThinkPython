#PROGRAM - 29

def is_sorted(num_list):
    """ Takes a list as a parameter & returns True if the list is sorted in    
        ascending order & False otherwise. """
        
    for i in range(len(num_list)):
        if (i != 0) and (num_list[i] < num_list[i-1]):
            return False
    return True        
    
print is_sorted([1,3,2])        
print is_sorted(['b','a'])        