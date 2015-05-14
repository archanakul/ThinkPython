#PROGRAM - 36
"""
    Sometime its easier to link the answers to a question rather then always 
    trying to link questions to answers. 
    Best example is my version of the code which also works but is much harder
"""
def two_way_interlocked_words(words):
    """ Finds all pairs of interlocked words i.e
        "shoe" + "cold" are interlocked to form "schooled"    """
    paired_list = list()
    for word in words:
        split1 = word[::2] #Choosing every other letter starting at index 0
        split2 = word[1::2] #Choosing every other letter starting at index 1
        if (split1 in words) and (split2 in words): 
            paired_list.append([split1,split2, word])
    return paired_list         

def three_way_interlocked_words(words):
    """ Finds all three-way interlocked words i.e every 3rd letter forms a word,   
        starting from the 1st, 2nd or 3rd"""
    paired_list = list()
    for word in words:
        split1 = word[::3] #Choosing every 3rd letter starting at index 0
        split2 = word[1::3] #Choosing every 3rd letter starting at index 2
        split3 = word[2::3] #Choosing every 3rd letter starting at index 3
        if (split1 in words) and (split2 in words) and (split3 in words): 
            paired_list.append([split1,split2, split3, word])
    return paired_list  
    
def gen_word_list(filename):
    """ Create word list using append() """
    fh = open(filename)
    word_list = list()
    for word in fh:
        word =  word.rstrip()
        word_list.append(word)
    fh.close()    
    return word_list
        
filename = raw_input("Enter the name of a file to be searched: ")
if len(filename) < 1:
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt"   
words = gen_word_list(filename)  
#print two_way_interlocked_words(word_list)
print three_way_interlocked_words(words)

# my initial version
"""def gen_word_pairs_list(word_list):
    word_pairs_list = list()
    
    for i in range(len(word_list)):
        for j in range(i+1,len(word_list)):
            if len(word_list[i]) == len(word_list[j]):
                interlocked, new_word = check_interlocked(word_list[i],
                                                      word_list[j],
                                                      word_list)
                new_word = word_list[i][                                      
                if interlocked:
                    word_pairs_list.append([word_list[i],word_list[j],new_word])   
                    print word_pairs_list
    return word_pairs_list

def check_interlocked(word1,word2,word_list):
    new_word = ''
    for i in range(len(word1)):
        new_word += (word1[i] + word2[i]) 
    if new_word in word_list:
        return True, new_word
    return False, None """  