#PROGRAM - 21

"""
    1. OPEN built in function takes a name of a file & returns FILE OBJECT
    2. FILE OBJECT is a handle to a file. It keeps tract of where it is in the 
       file, so that any method applied on to the file object are  handled right 
    3. READLINE is a method provide by file object that reads all the characters 
       in a file till it encounters newline (\n)
    4. RSTRIP([chars])-> returns a string with 'chars' removed fromt he string, 
       if omitted then chars argument defaults to removing whitespace (/r, /n)
    5. IN/ NOT IN operators act just as their meaning goes on strings   
"""
fin = open("words.txt")
print "List of word with 20 or more Character:"
print "======================================"
for line in fin:
    word = line.rstrip()
    if(len(word) < 20):
        continue
    print word 
print "======================================\n"


def has_no_e(word):
    for c in word:
        if c == 'e':
             return False   
    return True 
print "List of word without the character 'e': "
print "======================================"
# Incase the file is not opened again, list below would be empty as the previous looping brings fin to end of the file!!
fin = open("words.txt") 
count = 0
total = 0
for line in fin:
    total += 1
    word = line.rstrip()
    if has_no_e(word):
        print word
        count += 1
    continue   
print "Percentage of word without the charater 'e':" + str((count*100)/total)                   
print "======================================\n" 


def avoids(word, forbidden):
    for c in word:
        if c in forbidden:
             return False   
    return True 
print "List of word without vowels:"
print "======================================"
fin = open("words.txt") 
for line in fin:
    word = line.rstrip()
    if avoids(word, 'aeiou'):
        print word
    continue                     
print "======================================\n"  


def use_only(word, must):
    for c in word:
        if c not in must:
             return False   
    return True 
print "List of word containing only vowels:"
print "======================================"
fin = open("words.txt") 
for line in fin:
    word = line.rstrip()
    if use_only(word, 'aeiou'):
        print word
    continue                     
print "======================================\n"  
 

def use_all(word, shall):
    for c in shall:
        if c not in word:
             return False   
    return True
print "List of word containing all vowels at least once:"
print "======================================"
fin = open("words.txt") 
for line in fin:
    word = line.rstrip()
    if use_all(word, 'aeiou'):
        print word
    continue                        