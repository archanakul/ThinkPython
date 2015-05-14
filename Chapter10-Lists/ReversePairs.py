#PROGRAM - 35
def display_reverser_pairs(word_list):
    """ Two words are a “reverse pair” if each is the reverse of the other """
    for word in word_list:
        if word[::-1] in word_list:
            print word, word[::-1] 

def word_list(filename):
    """ Create word list using append() """
    fh = open(filename)
    word_list = list()
    for word in fh:
        word =  word.rstrip() #strip off the newline character
        word_list.append(word)  
    fh.close() 
    return word_list
             
filename = raw_input("Enter the file name to be read: ")
if len(filename) < 1:
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt"  
word_list = word_list(filename)
display_reverser_pairs(word_list)