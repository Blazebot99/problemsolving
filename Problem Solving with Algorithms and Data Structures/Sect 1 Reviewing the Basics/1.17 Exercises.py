def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        common=gcd(top, bottom)
        if type(top)!=type(0) or type(bottom)!=type(0):
            raise ValueError("Value Error: Fractions must consist of integers")
        self.num = top//common
        self.den = bottom//common
        
    def getnum(self):
        return self.num    
        
    def getden(self):
        return self.den    

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __repr__(self):
        return "{0} over {1}".format(self.num, self.den)    

    def show(self):
        print(self.num,"/",self.den)
        
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum > secondnum     
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum < secondnum   
    
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum >= secondnum     
    
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum <= secondnum   
    
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum != secondnum        
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)    
         
    def __mul__(self, other):
        newnum=self.num*other.num
        newden=self.den*other.den
        return Fraction(newnum, newden)
    
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den -self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum, newden)    
    
    def __truediv__(self, other):
        recip=Fraction(other.den, other.num)
        return self*recip
    
    def __radd__(self, other):
        return Fraction(other*self.den+self.num, self.den)
    
    def __iadd__(self, increment):
        return Fraction(self.num+increment*self.den, self.den)

fr=Fraction(2, 4)
"ONE"
#get numerator of a fraction
def getnum(self):
    return self.num
#get denominator of a fraction
def getden(self):
    return self.den
#print(fr.getnum(), fr.getden())

"TWO"
#modified init so that fractions start in lowest terms
def __init__(self,top,bottom):
    common=gcd(top, bottom)
    self.num = top//common
    self.den = bottom//common

"THREE"
def __mul__(self, other):
    newnum=self.num*other.num
    newden=self.den*other.den
    return Fraction(newnum, newden)

def __sub__(self, otherfraction):
    newnum = self.num*otherfraction.den -self.den*otherfraction.num
    newden = self.den * otherfraction.den
    common = gcd(newnum,newden)
    return Fraction(newnum, newden)    

def __truediv__(self, other):
    recip=Fraction(other.den, other.num)
    return self*recip

"FOUR"
def __gt__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den

    return firstnum > secondnum     

def __lt__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den

    return firstnum < secondnum   

def __ge__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den

    return firstnum >= secondnum     

def __le__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den

    return firstnum <= secondnum   

def __ne__(self, other):
    firstnum = self.num * other.den
    secondnum = other.num * self.den

    return firstnum != secondnum   

"FIVE"
#integer check for fractions
def __init__(self,top,bottom):
    common=gcd(top, bottom)
    if type(top)!=type(0) or type(bottom)!=type(0):
        raise ValueError("Value Error: Fractions must consist of integers")
    self.num = top//common
    self.den = bottom//common

"SIX"
#The fraction class here already works with negative numerators and denominators perfectly well, there are no issues here.
br=Fraction(1, -2)
ar=Fraction(1, -3)
#print(br*ar)
#print(4+br)

"SEVEN"
#radd tests if a type plus another type results in an error, and then tries adding them in the other order.
def __radd__(self, other):
    return Fraction(other*self.den+self.num, self.den)

"EIGHT"
#iadd increments an object by a given value. 
def __iadd__(self, increment):
    return Fraction(self.num+increment*self.den, self.den)

br+=1
#print(br)

"NINE"
#repr is used for precision when printing objects. For example, repr would print out a string with the quotations, but str would not. repr would also show more digits of a float, but str would round it after a certain point. 
def __repr__(self):
    return "{0} over {1}".format(self.num, self.den)

#print(repr(br))

class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        elif type(self.pinA)==type(0):
            return self.pinA
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        elif type(self.pinB)==type(0):
            return self.pinB        
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        elif type(self.pin)==type(0):
            return self.pin
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    
"TEN"
#NAND gate
class NotAndGate(BinaryGate):
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1  

#NOR gate       
class NotOrGate(BinaryGate):
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 1
        else:
            return 0

#XOR gate
class XOrGate(BinaryGate):
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==0 or a==0 and b==1:
            return 1
        else:
            return 0    
    
"ELEVEN"
#A half adder adds 2 binary numbers and stores the result. The first digit result is the "sum", which is 0 when both numbers are 1 or both are 0, becoming 1 otherwise. The "carry", which is the digit that goes into the second column (like carrying from the ones column to the tens) is 1 only if both values are 1, and is 0 otherwise. Therefore, the "sum" uses the same logic as a XOR gate, while the "carry" uses the ANDgate's logic. 
def half_adder(a, b):
    g1=XOrGate("Sum")
    g2=AndGate("Carry")
    g1.pinA, g1.pinB=a, b
    g2.pinA, g2.pinB=a, b
    add=g1.getOutput()
    carry=g2.getOutput()
    return (carry, add)

#print(half_adder(1, 0))

"TWELVE"
def full_adder(a, b, c):
    half=half_adder(a, b)
    full=half_adder(half[1], c)
    if c==1 and half[0]==0 or c==1 and full[1]==0:
        return half[1], full[1]    
    return half[0], full[1]

#print(full_adder(1,1,0))
    
def eight_bit_adder(a, b):
    al=[]
    bl=[]
    for digit in str(a):
        al.append(int(digit))
    for digit in str(b):
        bl.append(int(digit))
    final=[]
    c=[]
    i=7
    result=half_adder(al[i], bl[i])
    final.append(result[1])
    c.append(result[0])
    i-=1
    while i>=0:
        result=full_adder(al[i], bl[i], c[len(c)-1])
        final.append(result[1])
        c.append(result[0])
        i-=1
    if al[0]==1 and bl[0]==1:
        final.insert(1, 0)
    #the result digits are appended in a reverse order. Therefore, the result string when printed ends up also being reversed, as a normal for loop calls them in order. The solution would be to reverse the final string before returning it.
    add=""
    for n in final:
        add+=str(n)
    return add[::-1]

n1="10101010"
n2="11111111"
print(eight_bit_adder(n1, n2))
