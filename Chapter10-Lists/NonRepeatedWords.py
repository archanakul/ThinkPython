#PROGRAM - 27

"""
Open the file & read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When program completes, sort & print the resulting words in alphabetical order.
"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
    fname = "romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split() 
    for word in words:
        if word not in lst:
            lst.append(word) # adds in an element at the end of a list
lst.sort()            
print lst