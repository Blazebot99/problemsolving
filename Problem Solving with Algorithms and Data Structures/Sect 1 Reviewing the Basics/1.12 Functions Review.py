##Challenge: Make this algorithm so that it only alters letters once at a time to maximize efficiency. 
import string
letters=list(string.ascii_lowercase)
letters.append(" ")

def gen_s(target):
    from random import randint
    string=""
    for i in range(len(target)):
        key=randint(0, len(letters)-1)
        string+=(letters[key])
    return string
        
    
def score_s(s, target):
    sl=[]
    tl=[]
    score=0
    for char in s:
        sl.append(char)
    for char in target:
        tl.append(char)
    for i in range(len(target)):
        if sl[i]==tl[i]:
            score+=1
    return score      

def the_zone(target):
    tries=0
    lscore=0
    while True:
        nstring=gen_s(target)
        nscore=score_s(nstring, target)    
        if nscore>=lscore:
            lscore=nscore
            bstring=nstring
        tries+=1  
        if tries%1000==0:
            print(bstring, ":", lscore)
        if nscore==len(target):
            break          
    print("Finding a random string that matched your selected string," , target, ", took", tries, "tries.")
    
the_zone("me")