#PROGRAM - 51
def mathematical_pairs():
    pass 
 
def bingo_words(anagramdict, size):
    """ Returns a dictionary of anagrams with size of the word equal to 8 """
    bingo_words = dict()
    for signature,anagrams in anagramdict.iteritems():
        if len(signature) == size:
            bingo_words[signature] = anagrams
    return bingo_words 
           
def gen_ordered_anagram_sets(anagramdict):
    """ 
        Returns list of all the anagrams in the wordlist arranged in ascending 
        order of the number of anagrams present.
    """
    anagramset = list()
    for anagrams in anagramdict.values():
        if len(anagrams) > 1:
            anagramset.append((len(anagrams),anagrams)) # lost of tuples
    anagramset.sort(reverse = True) # sort in descending order
    # Zip when coupled with (*)gather operator, UNZIPSPES elements into tuples
    size,anagrams = zip(*anagramset) 
    return list(anagrams)   
    
def gen_all_anagrams(filename):
    """ 
        Returns a dictionary where each key has a value of anagram set 
        Key->sorted list of letter of anagram word set joined into a new word     
    """
    anagramdict = dict()
    
    wlist = gen_word_list(filename)
    for word in wlist:
        sword = signature(word)
        anagramdict.setdefault(sword,[]).append(word)
    return anagramdict
        
def signature(word):
    """ sort the letter of the word in ascending order to form a new word"""
    letter = list(word)
    letter.sort()
    sword = ''.join(letter)
    return sword

def gen_word_list(filename):
    """Returns a list of words in the file """ 
    wlist = list()
    fhandle  = open(filename) 
    for word in fhandle:
        word = word.rstrip().lower() 
        wlist.append(word)  
    return wlist 
            
filename = raw_input("Enter the name of the file with a set of word: ")
if len(filename) < 1:
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt"

anagramdict = gen_all_anagrams(filename)

#print gen_ordered_anagram_sets(anagramdict)
bingo_words = bingo_words(anagramdict,8)
print gen_ordered_anagram_sets(bingo_words)[0]
# ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest']
