#PROGRAM - 20

"""
    1. Abecedarian words are those in which each letter in the word appears in 
       alphabetical order(Double letters are ok)
"""
def is_abecedarian(word):
    last = word[0]
    for c in word:
        if c < last:
            return False
        last = c    
    return True
    
 def is_not_abecedarian(word):
    i = 0
    while (i < len(word)):
        if word[i + 1] < word[i]:
            return False
        i += 1    
    return True   
           
fin = open('words.txt')
print "List of all the words with character in alphabetical order:"
for line in fin:
    word = line.rstrip()
    if is_abecedarian(word):
        print word
    continue              