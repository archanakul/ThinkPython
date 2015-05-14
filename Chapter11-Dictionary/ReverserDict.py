#PROGRAM - 40

"""
    creates a dictionary that maps from frequencies to letters
    1. SINGLETON is a list that contains a single element
    2. Lists can be values in a dictionary, as this example shows, but they 
      cannot be keys (TypeError: list objects are unhashable)
    3. Basically have to be hashable/immutable as they can not be changing 
       because the value are always associated with keys. Hence lists canot be 
       used as key but can be used as value. Same is with DICTIONARIES as they 
       are MUTABLE too. 
    4. DEL OPERATOR: Remove dict[key] from dictionary when key is found else 
       Raises a KeyError when not found.
                del dict[key] 
    5. Dictionary METHODS:
        - CLEAR(): Remove all items from the dictionary.
                    dict.clear() 
        - COPY(): Return a shallow copy of the dictionary. 
                    dict.copy()    
        - ITERITEMS(): Returns an iterator over the dict's key-value pairs.
                    dict.iteritems()
        - ITERKEYS(): Returns an iterator over the dict's keys.
                    dict.iterkeys()
        - ITERVALUES(): Returns an iterator over the dict's key-value pairs.
                    dict.itervalues()
          Note: Are called with no intervening changes to the Dictionary, list 
          will directly correspond/append  
           
        - POP(): If key is in the dictionary, remove it & return its value, 
                 else return default. If default is not given & key is not in         
                 the dictionary, a KeyError is raised.
                        dict.pop(key[, default]) 
       - POPITEMS(): Remove & return an arbitrary key-value pair from dict 
                     If dict is empty, calling popitem() raises a KeyError 
                            dict.popitems()                               
        - UPDATE(): Update dictionary with a key/value pairs from other, 
                    overwriting existing keys. Return None 
                    Accepts either another dictionary object or an iterable of     
                    key/value pairs  
                            dict.update([other]) 
        - SETDEFAULT(): If key is in the dictionary, return its value. If not, 
                        insert key with a value of default & return default. 
                        Default defaults to None  
                            dict.setdefault(key[, default]) 
        - GET(): Return the value for key if key is in the dictionary, else 
                 default. If default is not given, it defaults to "None" so it 
                 never raises any KeyError  
                            dict.get(key[,default])                                                      
"""
def histogram(word):
    my_dict = dict()
    for c in word:  
       my_dict[c] = my_dict.get(c,0) + 1     
    return my_dict       
hist = histogram('Archana Raghavendra Kulkarni')

def invert_dict(diction):
    inv_dict = dict()
    for key in diction:
        val = diction[key]
        if val not in inv_dict:
            inv_dict[val] = [key] # create & assign a SINGLETON
        else:
            inv_dict[val].append(key)
    return inv_dict            

#print invert_dict(hist)

def concise_invert(diction):
    inv = dict()
    for key in diction:  
        val = diction[key]
        inv.setdefault(val,[]).append(key)
    return inv  
    
print concise_invert(hist) 

hist.update(x = 4,y = 5, z = 7) # add new 3 key-value pairs
print hist 

print hist.pop('J', 10)          
#print hist.pop('J') #KeyError

print hist.popitem() # remove an entry arbitrarily

lists = []
for (k,v) in hist.iteritems():
    lists.append([k, v])
print lists

tuples = [(v,k)for (k,v) in hist.iteritems()]
print tuples