#PROGRAM - 41

"""
    1. HISTOGRAM is a statistical word for set COUNTERS/FREQUENCIES
    2. SORTED() is a DICTIONARY function that returns sorted(Ascending order 
       when 'reversed' parameter is False) list of KEYS in a dictionary
    3. SORT() is a LIST method that sorts the list used on & returns None    
    
"""
def histogram(word):
    my_dict = dict()
    for c in word:
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1       
    return my_dict       
hist = histogram('Archana Raghavendra Kulkarni')
print hist  # Dictionary in no particular order

indeces =  hist.keys() # return a list of keys
indeces.sort() #Sorts a list
print indeces  #Sorted list of keys

print sorted(hist) # LIST of sorted keys alphabetically
print sorted(hist, reverse = True) #LIST of sorted keys alphabetically reversed
print sorted(hist.values()) #LIST of sorted value in ascending order  

def lookup(diction, index):
    for key in diction:
        if key == index:
            return diction[key] # return value associated with the key
    raise KeyError, 'Key not Found!!'     

print lookup(hist,'a')
#print lookup(hist,'s') #KeyError

def reverse_lookup(diction, val):
    for key in diction:
        if diction[key] == val:
            return key #return key associated with the value
    raise ValueError, 'Value not Found!!' 
print reverse_lookup(hist,6)
#print reverse_lookup(hist, 5) #ValueError     

def reverse_lookup_list(diction, val):
    my_list = list()
    for key in diction:
        if diction[key] == val:
             my_list.append(key)       
    if my_list == []:
        raise ValueError, 'Value not Found!!' 
    else:
        return my_list #return a list of keys associated with the value
print reverse_lookup_list(hist,1)
#print reverse_lookup_list(hist,4) #ValueError 