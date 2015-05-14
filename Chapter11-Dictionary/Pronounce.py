#PROGRAM - 44

def read_dictionary(filename='c06d.txt'):# default value
    """ Reads from a file and builds a dictionary that maps from
        each word to a string that describes its primary pronunciation.

        Secondary pronunciations are added to the dictionary with
        a number, in parentheses, at the end of the key, so the
        key for the second pronunciation of "abdominal" is "abdominal(2)". """
        
    cmudict = dict()
    fin = open(filename)
    for line in fin:
        # skip over the comments
        if line[0] == '#': continue

        t = line.split() #list of word/letters separated by a white space
        word = t[0].lower()
        # JOIN: Returns concatenation of strings in 'iterable'. 
        # Separator between elements is the string providing this method
        pron = ' '.join(t[1:]) # Separator for JOIN() is a white spaces
        cmudict[word] = pron
    return cmudict

def gen_word_list(filename):
    """ Create word list from a file """
    word_list = list()
    filehandle = open(filename)
    for word in filehandle:
        word = word.rstrip()
        word_list.append(word)
    return word_list 

if __name__ == '__main__':
    cmudict = read_dictionary()
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt"
    word_list = gen_word_list(filename)
    for word in word_list:
        if cmudict.has_key(word):
            first = word[1:]
            second = word[0] + word[2:]
            if cmudict.has_key(first) and cmudict.has_key(second):
                if cmudict[first] == cmudict[word] == cmudict[second]:
                    print word, first, second, cmudict[word]
