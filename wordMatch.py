from itertools import permutations
import os
words=[]
posibility=set()
print('Coded by Mohammad Javad Khademian mjkhonline@live.com')

def findMatch(chars,wordSize):
    make_dictionary(wordSize)
    print('searching for matches started.')
    perm = permutations(chars,wordSize)
    print('all permutations callculated.')
    i = 0
    l = calcP(len(chars),wordSize)
    for p in perm:
        printProgressBar(i,l)
        i = i + 1
        w = "".join(p)
        if w in words:
            posibility.add(w)

    print('All Possible words:')
    for w in posibility:
        print(w)

def calcP(y,x):
    out=1
    for i in range(y-x+1,y+1):
        out= out *i
    return out

def make_dictionary(wordLen):
    print('making dictionary started.')
    file = open("./words.txt", mode="r", encoding="utf-8")
    for line in file:
        endOfWord = line.index('\t')
        word = line.strip()[0:endOfWord]
        if len(word) == wordLen:
            words.append(word)
    file.close()
    print('dictionary has been made successfully. ' + str(len(words)) + " words added.")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    os.system('clear')
    # Print New Line on Complete
    if iteration == total:
        print()


charlist = []
char = input("enter chars one by one. Enter hashtag (#) for finding mathches: ")
while not char == "#":
    charlist.append(char)
    char = input("next char: ")
wsize = int(input('enter the length of the word: '))
findMatch(charlist,wsize)
