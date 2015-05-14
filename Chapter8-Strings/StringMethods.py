#PROGRAM - 19

"""
    1. FIND/RFIND -> Return the lowest index in 'str' where 'sub' is found 
       wholly contained in str[start:end]. Return -1 on failure 
                str.find(sub[, start[, end]])
                str.rfind(sub[, start[, end]]) -> highest index in 'str'
    2. INDEX/RINDEX -> Like find(), but raise ValueError when 'sub' is not     
       found.
                str.index(sub[, start[, end]])
                str.rindex(sub[, start[, end]])
                            
    3. COUNT-> Return number of non-overlapping occurrences of 'sub' in the  
       str[start:end]
               str.count(sub[, start[, end]])
               
    4. ISALPHA -> Return true if all characters in 'str' are alphabetic & there 
       is at least one character, false otherwise
                str.isalpha()  
    5. ISDIGIT -> Return true if all characters in 'str' are digits & there is 
       at least one character, false otherwise
                str.isdigit()         
    6. ISALNUM-> Return true if all characters in 'str' are alphanumeric & there 
       is at least one character, false otherwise
                str.isalnum() 
                
    7. ISSPACE -> Return true if there are only whitespace characters in 'str' 
        & there is at least one character, false otherwise
                str.isspace()           
                
    8. ISLOWER -> Return true if all characters in 'str' are lowercase & there 
       is at least one cased character, false otherwise
                str.islower()
    9. ISUPPER -> Return true if all characters in 'str' are uppercase & there 
       is at least one cased character, false otherwise
                str.isupper() 
    10. ISTITLE -> Return true if 'str' is a titlecased string & there is at 
        least one character, false otherwise   
                str.istitle()                           
    
                
    11. UPPER -> Return a copy of 'str' with all characters uppercased
                str.upper()
    12. LOWER -> Return a copy of 'str' with all characters lowercased
                str.lower()
    13. CAPITALIZE -> Return a copy of 'str' with its first character 
        capitalized & rest lowercased
                str.capitalize()
    14. TITLE -> Return a titlecased version of 'str' i.e first character of 
        each word is uppercased & remaining characters are lowercased
                str.title()
    15. SWAPCASE -> Return a copy of 'str' with uppercase characters converted 
        to lowercase and vice versa.
             str.swapcase()            
                
    16. LSTRIP -> Return a copy of 'str' with leading characters removed. 
        'chars' argument is a string specifying set of characters to be removed     
        If omitted or None, the chars argument defaults to removing whitespace
                str.lstrip([chars])
    17. RSTRIP -> Return a copy of 'str' with trailing characters removed. 
        Rest is same as lstrip()
                str.rstrip([chars])                     
    18. STRIP -> Return a copy of 'str' with leading & trailing characters 
        removed. 'chars' argument is neither a prefix nor a suffix but all 
        combinations of its values are stripped
                str.strip([chars]) 
                
    19. REPLACE -> Return a copy of 'str' with all occurrences of 'old' 
         replaced by 'new'. If the optional argument count is given, only the 
         first count occurrences are replaced
                str.replace(old,new[,count])
                
    20. SPLIT -> Return a list of the words in the string, using 'sep' as 
         delimiter string. 
                str.split([sep[, maxsplit]])
         'maxsplit' is given -> at most maxsplit splits are done
         'maxsplit' is not specified or -1 -> there is no limit on the splits
         'sep' is given -> consecutive delimiters are not grouped together and 
          are deemed to delimit empty strings  
              '1,,2'.split(',') -> ['1', '', '2'])
          sep is not specified or is None -> consecutive whitespace are regarded 
          as a single separator, & result will contain no empty strings at the 
          start or end if 'str' has leading or trailing whitespace
    21. RSPLIT -> Except for splitting from right, it behaves like split()
                str.rsplit([sep[, maxsplit]])
    22. SPLITLINES -> Return a list of lines in 'str', breaking at line 
        boundaries i.e universal newlines approach to splitting lines
        Line breaks are not included in the resulting list unless keepends is     
        given and is true
                str.splitlines([keepends])
                
    23. JOIN -> Return a string which is the concatenation of strings in 
        'iterable'. Separator between elements is the string providing this     
        method
                str.join(iterable)
                
    24. ZFILL -> Return the numeric string left filled with zeros in a string of 
      length width. The original string is returned if width <= len(str)
                str.zfill(width) 
    25. LJUST -> Return the string left justified in a string of length width. 
        Padding is done using the specified fillchar (default is a space). 
        original string is returned if width is less than or equal to len(s).
                str.ljust(width[, fillchar])
    26. RJUST -> Return the string right justified in a string of length width. 
        Rest is same as 'ljust()'
                str.rjust(width[, fillchar]) 
    27. CENTER -> Return centered in a string of length width. Padding is done 
        using the specified fillchar (default is a space)
                str.center(width[, fillchar])                     
                          
    28. STARTSWITH -> Return True if string starts with the prefix, else 
        return False. prefix can also be a tuple of prefixes to look for.
                str.startswith(prefix[, start[, end]])             
    29. ENDSWITH -> Return True if string ends with the suffix, else 
        return False. Rest is same as 'startswith()'
                str.startswith(prefix[, start[, end]]) 
                
    30. PARTITION -> Split 'str' at the first occurrence of sep, & return a 
        tuple containing; 1. part before the separator, 2. separator itself, & 
        3. part after the separator. 
        If the separator is not found, return a 3-tuple containing 'str' itself, 
        followed by two empty strings 
                str.rpartition(sep) 
    31. RPARTITION -> Split 'str' at the last occurrence of sep.
        If the separator is not found, return a tuple containing two empty 
        strings, followed by 'str' itself.
        Rest is same as 'partition()' 
                str.rpartition(sep)  
    32. DECODE
    33. ENCODE
    34. FORMAT
    35. TRANSLATE
    36. ISSPACE
    37. EXPANDTABS
                
"""
word = 'banana'
sub = 'an'

print "Substring is found at " + str(word.find(sub))
print "Substring is found at " + str(word.rfind(sub,0,5))
print "Substring is found at " + str(word.index(sub))
print "Substring is found at " + str(word.rindex(sub,0,5))

sub = 'am'
print "Substring is found at " + str(word.find(sub))
print "Substring is found at " + str(word.rfind(sub,0,5))
#print "Substring is found at " + str(word.index(sub)) -> ValueError
#print "Substring is found at " + str(word.rindex(sub,0,5)) -> ValueError

print "Count of substing appearance " + str(word.count('an'))

print "STing with iteratable concatenated: " + word.join('ABCDEF')

s = 'pining for the fjords'
s = s.split()
print s # use split when we need to split words in a string
delimiter = ' '
print delimiter.join(s) # join is a string method, so you have to invoke it on the delimiter and pass the list as a parameter

s = 'spam-spam-spam'
delimiter = '-'
print s.split(delimiter) # use split when we need to split words in a string


fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
for line in fin:
    line = line.rstrip() #get away with \n at the end of each line
    if not line.startswith('From '):
        continue
    words = line.split() # split a line into words separated with whitespace
    print words[2] # print the 3rd word in the list which is the day when mail was received.  
    piece = words[1].split('@') # split email ID & domain
    print piece

