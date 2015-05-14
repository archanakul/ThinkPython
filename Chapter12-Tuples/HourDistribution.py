#PROGRAM - 48

"""
    Number of mails receives during an hour
    1. SPLIT(delimiter) returns a list of words each separater by a "delimiter"
    2. GET(key[,default]): Returns value ofr the key in the dictionary when 
       present else return te default value provided.
"""
name = raw_input("Enter the file name: ")
if len(name) < 1:
    name = "/Volumes/AntZ/Acchu/Learnings/Notes/Excercise/Python/mbox-short.txt"
handle = open(name)

lst = list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        lst.append(line) 
               
times = list()        
for line in lst:
    # From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
    times.append(line.split()[5].split(':')[0])  #18:10:48
    
hdict = dict()    
for hour in times: 
   hdict[hour] = hdict.get(hour,0) + 1 

for k,v in sorted(hdict.items()):
    print k, v 
           