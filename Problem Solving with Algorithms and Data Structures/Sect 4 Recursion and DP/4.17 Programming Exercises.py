"ONE"
def factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n

#print(factorial(6))

"TWO"
def reverse(s):
    if len(s)==1:
        return str(s)
    else:
        return reverse(s[1:])+s[0]

#print(reverse("evil did i did live"))

"THREE"
import turtle

def tree(branchLen,t):
    import random
    rng=random.Random()
    if branchLen > 5:
        ang=rng.randrange(10,30)
        t.forward(branchLen)
        t.right(ang)
        ang=rng.randrange(30,50)
        cut=rng.randrange(10, 20)
        tree(branchLen-cut,t)
        t.left(ang)
        ang=rng.randrange(10,30)
        cut=rng.randrange(5, 15)
        tree(branchLen-cut,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

#main()

"FIVE"
def recfib(n):
    if n==1 or n==0:
        return 1
    else:
        return recfib(n-1)+recfib(n-2)

def itrfib(n):
    a=1
    b=1
    for i in range(n):
        (a,b)=(b, a+b)
    return a
        
#print(recfib(10))
#print(itrfib(10000))

"SIX"
class Stack:
    def __init__(self, name):
        self.items = []
        self.name=name
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
def moveTower(height,fp, tp, wp): 
    fromPole=Stack(fp)
    toPole=Stack(tp)
    withPole=Stack(wp)
    if height >= 1:
        for disk in range(height):
            fromPole.push(0)
        moveTower(height-1,fp,wp,tp)
        moveDisk(fromPole, toPole)
        moveTower(height-1,wp,tp,fp)
        
def moveDisk(fp,tp):
    tp.push(fp.pop())
    print("Moving disk from", fp.name, "to", tp.name)

#moveTower(3, "A", "B", "C")

"NINE"
class Jug:
    def __init__(self, size):
        self.size=size
        self.volume=0
    
    def empty(self):
        self.volume=0
    
    def fill(self):
        self.volume=size
    
    def pour(self, other):
        if self.volume>=other.size:
            self.volume-=other.size
            other.volume+=other.size
        else:
            other.volume+=self.volume
            self.volume=0

"ELEVEN"
def travel(close, n1,far, n2):
    if close.count("c")==1 and far.count("c")==close.count("m")-close.count("c"):
        close.remove("m")
        close.remove("m")
        far.append("m")
        far.append("m")
        print("Moving 2 missionaries from", n1, "to", n2+".")
    elif close.count("m")==1 and close.count("c")==1:
        close.remove("m")
        far.append("m")
        print("Moving 1 missionary from", n1, "to", n2+".")
    elif far.count("m")==1 and far.count("c")==1:
        close.remove("m")
        close.remove("c")
        far.append("m")
        far.append("c")
        print("Moving 1 missionary and 1 cannibal from", n1, "to", n2+".")        
    elif far.count("c")==1:
        close.remove("c")
        close.remove("c")
        far.append("c")
        far.append("c")
        print("Moving 2 cannibals from", n1, "to", n2+".")
    elif "m" in close:
        close.remove("m")
        close.remove("c")
        far.append("m")
        far.append("c")
        print("Moving 1 missionary and 1 cannibal from", n1, "to", n2+".")            
    elif "c" not in far:
        close.remove("c")
        far.append("c")
        print("Moving 1 cannibal from", n1, "to", n2+".")
    else:
        close.remove("c")
        far.append("c")
        close.remove("c")
        far.append("c") 
        print("Moving 2 cannibals from", n1, "to", n2+".")
        
def river_crossing(close, far):
    if close==[]:
        return
    else:
        travel(close, "starting point", far, "destination")
        travel(far, "destination", close, "starting point")
        river_crossing(close, far)
        
#river_crossing(["c"]*3+["m"]*3, [])
        
    
"THIRTEEN"
t=""
def pascal(n):
    global t
    r=[]
    if n==1:
        r.append(1)
        t+=str(r[0])+"\n"
        return r
    else:
        p=pascal(n-1)
        r.append(1)
        for i in range(n-2):
            r.append(p[i]+p[i+1])
        r.append(1)
        for n in r:
            t+=str(n)+" "
        t+="\n"
        return r
    
#pascal(200)
#print(t, end="")

"FOURTEEN"
def art_profit_proto(stolenitems, weight):
    stealpaths=[]
    for art in [w for w in stolenitems.keys() if w<=weight]:
        if art==weight:
            stealpaths.append(stolenitems[art])
        for stole in [w for w in stolenitems.keys() if w<=weight]:
            if art+stole==weight:
                stealpaths.append(stolenitems[art]+stolenitems[stole])
    if stealpaths==[]:
        return 0
    return max(stealpaths)

def art_profit(stolenitems, weight, maxprofits):
    for w in range(min(stolenitems.keys()), weight+1):
        v=stolenitems.get(w, 0)
        heavy=w
        itemstaken=[]
        if v!=0:
            itemstaken.append((w, v))
        for art in [a for a in stolenitems.keys() if a<=w]:
            if (art, stolenitems[art]) not in maxprofits[w-art][2] and maxprofits[w-art][1]+stolenitems[art]>v and maxprofits[w-art][0]+art<=w:
                itemstaken=[]
                v=maxprofits[w-art][1]+stolenitems[art]
                heavy=maxprofits[w-art][0]+art
                itemstaken.append((art, stolenitems[art]))
                for item in maxprofits[w-art][2]:
                    itemstaken.append(item)
        if maxprofits[w-1][1]>v:
            maxprofits[w]=maxprofits[w-1]
        else:
            maxprofits[w]=heavy,v,itemstaken
    return maxprofits[weight][1]

items={2:3, 3:4, 4:8, 5:8, 9:10}
maxweight=11
print(art_profit(items, maxweight, {j:(0, 0, []) for j in range(maxweight+1)}))


        
        
    
    