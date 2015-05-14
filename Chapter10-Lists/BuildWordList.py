#PROGRAM - 33
"""
    1. time.TIME(): Returns the time as a floating point number expressed in 
       seconds since the epoch, in UTC
    2. time.CLOCK(): Returns the current CPU time as a floating-point number of 
       seconds. 
       To measure computational costs of different approaches, the value of 
       time.clock is more useful than that of time.time()   
    3. time.ASCTIME([timetuple]): Accepts a time-tuple & returns a readable 
       24-character string
                Tue Jan 13 10:17:09 2009 
    4. time.CTIME([sec]):same as ASCTIME without arguments
    5. time.SLEEP(secs): Suspends the calling thread for secs seconds.             
"""
import time

def word_list_fun1(filename):
    """ Create word list using append() """
    fh = open(filename)
    word_list = list()
    for word in fh:
        word =  word.rstrip()
        word_list.append(word)  
    fh.close()       
        
def word_list_fun2(filename):
    """ Create word list using idiom t = t + [x]"""
    fh = open(filename)
    word_list = list()
    for word in fh:
       word = word.rstrip()
       word_list += [word]  
    fh.close()    
        
filename = raw_input("Enter the word file name: ")  
if len(filename) < 1:  
    filename = "/Volumes/AntZ/Acchu/Learnings/Python/ThinkPython/Words.txt" 
start =  time.clock()
word_list_fun1(filename)
end =  time.clock()
print end
print "Elapsed time: " + str(end - start)
start =  time.clock()
word_list_fun2(filename)
end =  time.clock()
print "Elapsed time: " + str(end - start)