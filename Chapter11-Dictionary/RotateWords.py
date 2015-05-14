#PROGRAM - 43
""" 
    1. ITERATABLE: An object capable of returning its members one at a time. 
       Ex:  All sequence types LIST/STR/TUPLE and some non-sequence types like 
            DICT/FILE/OBJECTS of any classes you define with an __iter__() or 
            __getitem__() method
    2. MODULOUS OPERATOR(%): Rturns the remainder after division .
        - sign of the result is based on sign of divisor in an expression
        - since the remainder can not be greater than the divisor, it helps in 
          limiting the result be between 0-(divisor-1) --> POWERFUL TOOL   
"""            
def gen_rotate_pairs(word_list):
    """ Form a dictionary of a word and its rotated valid words as key:value 
        pairs for all the words in word.txt """
    rwords = dict()
    rlist = list()
    for word in word_list:
        rlist = gen_rotated_words(word, word_list)
        if len(rlist) > 0:
            rwords[word] = rlist  
            print word, rwords[word]
        
def gen_rotated_words(word, word_list):
    """ Forma a list of words each one formed by rotating each letter of the 
        original word n places where n range between 1-25 """
    rword = ''
    rlist = list()
    for n in range(1,26):
        rword = rotate_word(word, n)
        if rword in word_list:
            rlist.append(rword) 
    return rlist     
             
def rotate_word(word, n):
    """ Rotate each letters of the word by n places"""
    rword = ''  
    for letter in word:
        rword += rotate_letter(letter,n)
    return rword         

def rotate_letter(letter, n):
    """ Rotate a letter n places"""
    if letter.islower(): 
        start = ord('a')
    else:
        start = ord('A')
    displacement = ord(letter) - start #units away from first character   
    limited = (displacement + n) % 26 #Limits value to be with in 0-25
    return chr(start + limited)

def gen_word_list(filename):
    """ Create word list from a file """
    word_list = list()
    filehandle = open(filename)
    for word in filehandle:
        word = word.rstrip()
        word_list.append(word)
    return word_list       

filename = raw_input("Enter the file to be read: ")
if len(filename) < 1:
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt"  
word_list = gen_word_list(filename)    
gen_rotate_pairs(word_list)   