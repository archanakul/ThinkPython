#PROGRAM - 50
"""
    1. GATHER: Using * infront of a function argument gathers all the elements 
       into a single variable from
    2. ZIP(): zip() in conjunction with * operator can be used to unzip a list   
"""

def most_frequent(word):
    """ Sorts letters in a word in reverse order of frequency."""
    letter_hist = make_histogram(word)
    letters = list()
    
    for k,v in frequency.items():
        letters.append((v,k))   
    #[(2,'h'), (2,'f'), (2,'a'), (1,'g'), (1,'e'), (1,'b')]      
    freq, letter = zip(*letters.sort(reverse = True)) 
    print list(letter)
 
def make_histogram(word):
    """Builds a histogram of letters to number of times they appear in a word"""
    hist = dict()
    for letter in word:
        hist[letter] = hist.get(letter,0)+1
    return  hist   
     
most_frequent('abefghahf')    
    