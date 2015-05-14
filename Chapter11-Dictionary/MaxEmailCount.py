#PROGRAM - 37

"""
figure out who has sent the greatest number of mails. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = raw_input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
    
fin = open(name)
counter = dict()

for line in fin:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    counter[words[1]] = counter.get(words[1],0)+1
 
bigID = None
bigNum = None
for key,value in counter.items():
    if bigID == None or value > bigNum:
        bigID = key
        bigNum = value

print bigID, bigNum 