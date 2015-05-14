#PROGRAM - 34
"""
    1. OPEN(): Returns a FILE OBJECT, & is most commonly used with 2 arguments:     
                    open(filename, mode)
    2. Methods of FILE OBJECTS are:
        - READ() : Reads some quantity of data & returns it as a string. 
                   When size is omitted or negative, the entire contents of the 
                   file will be read and returned 
                 fh.read(size)   
       - READLINE(): Reads a single line from the file; a newline character is 
                     left at the end of the string, & is only omitted on the 
                     last line of the file if the file doesn't end in a newline.
                 fh.readline()
         Note1: To reading lines from a file, you can loop over the file object. 
                This is memory efficient, fast, and leads to simple code  
                    for line in fh:
                        print line 
         Note2: To read all the lines of a file in a list we can use
                    list(fh)
        - WRITE(string): Writes the string onto file, returning None 
        - TELL(): Returns an integer giving the file object's current position 
                  in the file, measured in bytes from the beginning of the file 
        - SEEK(offset,from_what): Change the file object's position  
                new position = offset + reference point based on from_what 
                from_what = 0/omitted, beginning of the file as reference point
                from_what = 1, current file position as reference point
                from_what = 2, end of the file as reference point   
       - CLOSE(): closes the file & free up any system resources taken up by the 
                  open file. Any attempts made to use the file object will 
                  automatically fail after this line 
                        fh.close()                                                                   
""" 
def bisect(sorted_lst, search_word):
    """ Takes a sorted list & a target value and returns the index of the value 
        in the list, if it's there, or None if it's not.  """
    max = len(sorted_lst)
    min = 0
    count = 0
    while(count < 17):
        limit = (max+min)/2 
        if (search_word > sorted_lst[limit]):
            min = limit
        elif (search_word < sorted_lst[limit]):  
            max = limit
        else:
            return limit 
        count += 1
    print "Word not found"   
    return None               

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
word = raw_input("Enter the word to be searched: ")
if len(filename) < 1:
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt"   
word_list = list()
word_list = gen_word_list(filename)  
word_list.sort()
print bisect(word_list, word)   