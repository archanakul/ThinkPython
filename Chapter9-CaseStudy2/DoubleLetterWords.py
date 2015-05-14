#PROGRAM - 22

"""
    3 Consecutive double letter words
         b-oo-kk-ee-per
         b-oo-kk-ee-pers
         b-oo-kk-ee-ping
         b-oo-kk-ee-pings
"""
def consecutive_letters(word):
    i = 0
    count = 0
    while ((i < len(word) - 1) and count < 3):
        if (word[i+1] == word[i]):
            count += 1
            i += 2 #otherwise would compare every consecutive letter in spite of finding to consecutive letter word.
        else:
            count = 0 #counter reset as double letters need to be consecutive   
            i += 1
    return (count >= 3)

fin = open('words.txt')
for line in fin:
    word = line.rstrip()
    if consecutive_letters(word):
        print word