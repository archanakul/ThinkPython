#PROGRAM - 49

"""
    1. Regular expression are a set of character that have a special meaning & 
       they are defined in a module called"re" which needs to be imported before 
       using there regular expression.
    2. Regular expression list:
        ^ -> matches the BEGINNING of a line
        $ -> matches the END of a line  
        . -> matches ANY CHARACTER
        \s -> matches WHITESPACE
        \S -> matches NON-WHITESPACE Characters
        * -> REPEATE a character ZERO or more times : LONGEST
        *? -> REPEATE a character ZERO or more times(NON-GREADY): SHORTEST
        + -> REPEATE a character ONE or more times : LONGEST
        +? -> REPEATE a character ONE or more times(NON-GREADY): SHORTEST
        [aeiou] -> match a SINGLE character IN the listed SET
        [^xyz] -> match a SINGLE character NOT IN the listed SET
        [a-z0-9] -> SET of characters can include a range
        ()-> Mark the START & END of of part of substring that matched the RE & 
        EXTRACTS only the matched part when used with FINDALL() 
     3. SEARCH()-> Scans though the string looking for any location where the RE 
        is found &  it return None
     4. FINDALL()-> finds all the substrings that match the RE & returns a list 
        of these substrings                 
"""

import re

fh = open("/Volumes/AntZ/Acchu/Learnings/Notes/Excercise/Python/mbox-short.txt")
d = dict()
for line in fh:
    line = line.rstrip()
    
# Match lines that START WITH(^) -> "From:" 
    if re.search('^From:', line): 
        pass # print line
        
# Match lines that START WITH(^) -> "From:" followed by one or more characters(.+) and then an @ sign
    if re.search('^From:.+@', line): 
        pass # print line
    
# Match substrings that have one or more NON-WHITESPACE characters(\S+), then an @ sign & followed by one or more NON-WHITESPACE characters & extracts only (\S+@\S) characters into LIST assigned to x
    x = re.findall('(\S+@\S+)',line)
    if len(x) > 0:
         pass #print x
         
# Match substrings that start with small or big letter or number followed by Zero or more NON-WHITESPACE characters(\S+), then an @ sign, followed by Zero or more NON-WHITESPACE characters, followed by small or big letter        
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    if len(x) > 0:
        pass #print x    

    if re.search('^X-.*: [0-9.]+',line):
         print line 
    if re.search('^X\S*: [0-9.]+',line):
         print line    