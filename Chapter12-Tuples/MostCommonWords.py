#PROGRAM - 47

"""
    1. GET(key[,value]) method of a dictionary get the value of a key in a 
       dictionary if present else adds the key to dictionary with a default 
       value provided & returns this value -> This not only gets value but also 
       updates it.
    2. All the data types that can be compared can also be sorted. SORTED & 
       REVERSER are the methods that can take any data type unlike SORT which 
       works only on LISTS   
"""
filename = raw_input("Enter the file name: ")
if len(filename) < 1:
    filename = "/Volumes/AntZ/Acchu/Learnings/Notes/Excercise/Python/mbox-short.txt"
fin = open(filename)
wdict = dict()

for line in fin:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        wdict[word] = wdict.get(word,0) + 1
        
# List NON-COMPREHENSION version         
tmp = list()            
for (k,v) in wdict.items():
    tmp.append((v,k))
tmp.sort(reverse = True)# sort in descending order(highest to lowest)
for (v,k) in tmp[:10] :
    print k, v 
    
# List COMPREHENSION version      
for (v,k) in sorted([(v,k)for(k,v) in wdict.items()], reverse = True)[:10]:
    print (k,v) 
     
                   
     
