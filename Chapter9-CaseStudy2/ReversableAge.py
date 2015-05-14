#PROGRAM - 24

"""
    1. zfill: Return the integer (mom/son) written as a string with at least
    (len) digits"
"""

def are_reversed(son, mom, long):
    mom = str(mom).zfill(long)
    son = str(son).zfill(long)
    return mom[::-1] == son

def reversebale_instance(diff):
    count = 0
    son = 0
    
    while(True):
        mom = son + diff
        if are_reversed(mom, son, 2) :
            count += 1
            if count == 6:
                print "My current age is " + str(son)
        if mom > 120:
            break
        son += 1
    return count
    
def check_diffs():
    diff = 10 
    while (diff < 70):
        count = reversebale_instance(diff)
        if count >=8:
            print diff, count
        diff += 1 
         
check_diffs()           
       