#PROGRAM - 30
""" 
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    1. list.REMOVE(x): Removes the first appearance of x in the list. 
        ValueError if x is not found in the list.
    2. list.POP([,index]): Removes an item at a specified location or at the end 
       of the list in 'index' is not provided. 
    3. LIST(): converts a string into a list of characters of the string
"""
def is_anagram(word1, word2):
    """ It takes two strings and returns True if they are anagrams """
    word1 = list(word1)
    word2 = list(word2)

    if len(word1) != len(word2):
        return False
    else:   
        for letter in word1:
             if letter not in word2: # To avoid ValueError
                return False
             word2.remove(letter)     
    return True        

print is_anagram("abcc","cbac")      