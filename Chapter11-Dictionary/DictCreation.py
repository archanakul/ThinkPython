#PROGRAM - 38

"""
    1. DICTIONARY like a LIST are a collection of same/different types of data 
       except that the INDECES in case of Lists are INTEGER while for dictionary 
       they can be almost of any type but typically STRINGS   
    2. Dictionaries have a MAPPING between a set of INDICES/KEYS and a set of 
       VALUE. An associated keys & values is called a KEY-VALUE PAIR or ITEMS. 
    3. EMPTY DICTIONATY i.e a dictionary with zero elements/size is created by 
       either calling a CONSTRUCTOR dict() or just a pair of CURLY BRACES ({})  
    4. Key and its associated value in a dictionary are separated by a COLON (:)
                new_dict = {'one': 1}
    5. New items can be added to dictionary with square BRACKET OPERATOR
                new_dict['two'] = 2  
    6. ORDER of the ITEMS in a dictionary need not be the order on which they 
       are added to the dictionary. the order is UNPREDICTORY. However the 
       KEY-VALUE PAIRS remain UNCHANGED & hence KEYS are used to look up the 
       corresponding VALUES 
                print new_dict['one']
       Note: When KEY is not in dictionary then we get an Exception (KeyError) 
    7. KEYS(): Return a copy of the dictionary’s list of keys 
                keys_list = dict.keys()                  
    8. VALUES(): Return a copy of the dictionary’s list of values 
                values_list = dict.values()
    9. ITEMS(): Return a copy of the dictionary’s list of (key,value) pairs 
                dict.ITEMS() -> [('one',1), ('two',2)]
       Note: Are called with no intervening changes to the Dictionary, list 
             will directly correspond/append
    
    10. HAS_KEY(): Check for presence of key in dictionary to avoid KEYERROR 
                     dict.has_key() 
       or by using a KEY() method along with & IN OPERATOR
                keys = new_dict.keys()
                'three' in keys
     
       or use : 'three' in new_dict ->looks for KEYS by DEFAULT  
       Note: KEYS have to be UNIQUE else the old value of an EXISTING KEY gets         
             OVERWRITTEN. But multiple keys can have SAME VALUES 10. LEN(dict):     
    11. Returns length of dictionary i.e number of ITEMS/Key-Value 
        pairs in a dictionary            
                            
                                  
"""
new_dict = dict()
old_dict = {'one': 'I', 'two': 2}
new_dict['one'] = 1
new_dict['two'] = 'II'
print old_dict, new_dict

print old_dict['two'], new_dict['two']
#print new_dict['three'] # KeyError
print str('three' in new_dict)
print str('two' in new_dict.keys())
print str('I' in new_dict.values())

print new_dict.items(), old_dict.items()


