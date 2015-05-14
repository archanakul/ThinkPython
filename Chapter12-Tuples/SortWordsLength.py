#PROGRAM - 46

"""
    1. SETDEFAULT(key,default) add a new entry into the dictionary if the key is 
       not already in the dictionary with a default value provided else appends 
       the existing key's value
    2. SORTED(dict, reverse) is the sort function for dictionaries  
    3. SHUFFLE method from RANDOM module shuffles the list
    4. EXTENDS appending all the items in the given list as individual elements 
       unlike append which just add in in the type they are supplied
"""
from random import shuffle

#words with the same length appear in alphabetical
def sort_by_length(words):
    original = []
    for word in words:
        original.append((len(word),word))
    
    original.sort(reverse = True)
     
    updated = []
    for length, word in original: 
        updated.append(word)
    
    return updated 

#words with the same length appear in random order   
def sort_by_length_random(words): 
    original = {}
    updated = []
    
    for word in words:
        original.setdefault(len(word),[]).append(word)  # all words with same length are grouped together under one key length
    
    for key in sorted(original, reverse = True):
        if len(original[key]) > 1 : # key for words with same length
            shuffle(original[key])  # shuffle the list of words    
        updated.extend(original[key]) # Each word of the list is appended & not the list as a whole
    return updated     
    
names = ('archu', 'archana', 'antz', 'ananth','ants')     
 
#print sort_by_length(names)   
print sort_by_length_random(names)  