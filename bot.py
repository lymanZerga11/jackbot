import operator
from functools import reduce
import os
import math
import pyautogui
from PIL import Image
import fileinput
import time


l={}
p={}
p['30nn']=["ak","aa","qq","kk"]
p['30nns']=[]
p['20nn']=["aa","ak","kk","aq","qq","jj","tt"]
p['20nns']=[]
p['100n']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","22","ak","aq","aj","at","9a","8a","7a","6a","5a","4a","kq","jk","kt","jq"]
p['100ns']=["3a","2a","9k","tq","jt"]
p['101n']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","22","ak","aq","aj","at","9a","8a","7a","6a","5a","4a","3a","2a","kq","jk","kt","9k","jq"]
p['101ns']=["8k","7k","qt","jt"]
p['102n']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","22","ak","aq","aj","at","9a","8a","7a","6a","5a","4a","3a","2a","kq","jk","kt","9k","8k","7k","6k","5k","4k","3k","jq","qt","9q","8q","jt","9j","9t"]
p['102ns']=["2k","7q","6q","5q","8j","7j","8t"]
p['21nn']=["aa","ak","kk","aq","qq","jj","tt"]
p['21nns']=[]
p['111n']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","ak","aq","aj","at","9a","8a","7a","kq","jk"]
p['111ns']=["6a","5a","4a","3a","kt","jq"]
p['112n']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","ak","aq","aj","at","9a","8a","7a","6a","5a","kq","jk","kt"]
p['112ns']=["4a","3a","2a","9k","jq","qt","jt"]
p['01nn']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","22","ak","aq","aj","at","9a","8a","7a","6a","5a","4a","3a","2a","kq","jk","kt","9k","8k","7k","6k","5k","4k","3k","2k","jq","qt","9q","8q","7q","6q","5q","4q","3q","jt","9j","8j","7j","9t","8t","7t","89","79","78"]
p['01nns']=["2q","6j","5j","4j","3j","2j","6t","5t","4t","69","59","68","58","67","57","47","46","56","35","45"]
p['12nn']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","ak","aq","aj","at","9a","kq","jk"]
p['12nns']=["8a","7a"]
p['02nn']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","22","ak","aq","aj","at","9a","8a","7a","6a","5a","4a","3a","2a","kq","jk","kt","9k","jq","qt","jt"]
p['02nns']=["8k","7k","6k","5k","4k","3k","9q","8q","9j","8j","7j","9t","8t","7t","89","79","78","68","67","56"]
p['02nb']=["aa","kk","qq","jj","tt","99","88","77","66","55","44","33","22","ak","aq","aj","at","9a","8a","7a","6a","5a","4a","3a","kq","jk","kt","jq","jt"]
p['02nbs']=["2a","9k","8k","7k","qt","9q","8q","9j","8j","8t","9t","89","78"]


locationOfTest="C:/Users/Sree/tester1/"
#create database
filelocation=["","","",""]
filelocation[0]=locationOfTest+"p0.png"
filelocation[1]=locationOfTest+"p1.png"
#filelocation[2]=locationOfTest+"p2.png"
#filelocation[3]=locationOfTest+"p3.png"
filelocationforAllins=[locationOfTest+"allin1.png",locationOfTest+"allin2.png",locationOfTest+"allin3.png"]
filelocationforMyPos=locationOfTest+"mypos.png"
deck=["2","3","4","5","6","7","8","9","t","j","q","k","a"]
####not required
c1=["GREEN","BLUE","RED","GREY"]
ccode=["c","d","h","s"]

GREEN=(32, 137, 28)
BLUE=(21, 89, 153)
RED=(203, 63, 63)
GREY=(82, 82, 82)
DEALT=(180,46,46)
NOTDEALT=(140,125,103)
BUTTON=(233, 184, 108)
NOTBUTTON=(93,34,34)
TURN=(253, 244, 170)
NOTTURN1=(73, 73, 73)
NOTTURN2=(42,43,45)
class Table(object):
    def __init__(self):
        self.myCards = []
        self.allinCount=0 #can be 0,1,2,3
        self.myPosition=0 #0=big 1=small 2=none
        self.curDecision=2 #0=fold 1=allin 2=new
        self.tableno=-1
        self.guyAllin='n'
        self.button='n'
    buttonPixelPosition=()
    yellowPixelPosition=()
    allinClickPosition = ()
    allinPixelPosition  =()
    foldClickPosition= ()
    player1Pos=()
    player2Pos=()
    player3Pos=()
    myPos=()
    rightguy1=()
    rightguy2=()
    def buttonIsMine(self):
        print('Checking if dealt')
        color1=pyautogui.pixel(self.buttonPixelPosition[0],self.buttonPixelPosition[1])
        color2=NOTBUTTON
        Diff=[0,0]
        Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        color2=BUTTON
        Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        print(Diff[0])
        print(Diff[1])
        c=Diff.index(min(Diff))
        return c
    def analyse(self):
        #card1
        print('Analysing')
        pyautogui.screenshot(filelocation[0],region=self.myCards[0].position)
        pixels=pyautogui.pixel(self.myCards[0].pixelposition[0],self.myCards[0].pixelposition[1])
        col=findCardColor(pixels)
        val=findCardDeck(col,filelocation[0],0)
        self.myCards[0].suit=col
        self.myCards[0].value=val
        print('Card1 done')
        #card2
        pyautogui.screenshot(filelocation[1],region=self.myCards[1].position)
        pixels=pyautogui.pixel(self.myCards[1].pixelposition[0],self.myCards[1].pixelposition[1])
        col=findCardColor(pixels)
        val=findCardDeck(col,filelocation[1],1)
        self.myCards[1].suit=col
        self.myCards[1].value=val
        print('Card2 done')
        #myposition
        pyautogui.screenshot(filelocationforMyPos,region=self.myPos)
        self.getMyPosition()
        print('MyPos done ')
        #allins
        #pyautogui.screenshot(filelocationforAllins[0],region=self.player1Pos)
        #pyautogui.screenshot(filelocationforAllins[1],region=self.player2Pos)
        #pyautogui.screenshot(filelocationforAllins[2],region=self.player3Pos)
        #compare and decide
        self.countAllins()
        print('Allin done ')
    def hasNothing(self,g):
        if(g==0):
            print('Checking if hasNothing')
            Diff=[0,0]
            color1=pyautogui.pixel(self.nothing1PixelPos[0],self.nothing1PixelPos[1])
            color2=SOMETHING
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=NOTHING
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            c=Diff.index(min(Diff))
            if(c==1):
                print('NOTHING')
                return True
            else:
                print('SOMETHING')
                return False
        if(g==1):
            print('Checking if hasNothing')
            Diff=[0,0]
            color1=pyautogui.pixel(self.nothing2PixelPos[0],self.nothing2PixelPos[1])
            color2=SOMETHING
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=NOTHING
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            c=Diff.index(min(Diff))
            if(c==1):
                print('NOTHING')
                return True
            else:
                print('SOMETHING')
                return False
        if(g==2):
            print('Checking if hasNothing')
            Diff=[0,0]
            color1=pyautogui.pixel(self.nothing3PixelPos[0],self.nothing3PixelPos[1])
            color2=SOMETHING
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=NOTHING
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            c=Diff.index(min(Diff))
            if(c==1):
                print('NOTHING')
                return True
            else:
                print('SOMETHING')
                return False
        return True
    def hasButton(self,g):
        if(g==0):
            print('Checking if hasButton')
            Diff=[0,0]
            color1=pyautogui.pixel(self.button1PixelPos[0],self.button1PixelPos[1])
            color2=NOTBUTTON
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=BUTTON
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            c=Diff.index(min(Diff))
            if(c==1):
                print('BUTTON')
                return True
            else:
                print('NO BUTTON')
                return False
        if(g==1):
            print('Checking if hasButton')
            Diff=[0,0]
            color1=pyautogui.pixel(self.button2PixelPos[0],self.button2PixelPos[1])
            color2=NOTBUTTON
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=BUTTON
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            c=Diff.index(min(Diff))
            if(c==1):
                print('BUTTON')
                return True
            else:
                print('NO BUTTON')
                return False
        if(g==2):
            print('Checking if hasButton')
            Diff=[0,0]
            color1=pyautogui.pixel(self.button3PixelPos[0],self.button3PixelPos[1])
            color2=NOTBUTTON
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=BUTTON
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            c=Diff.index(min(Diff))
            if(c==1):
                print('BUTTON')
                return True
            else:
                print('NO BUTTON')
                return False
        return True
    def getMyPosition(self):
        im1=Image.open(filelocationforMyPos)
        h1 = im1.histogram()
        rms=[]
        for i in range(0,3):
            im2=Image.open(locationOfTest+"database/"+"myPos"+str(i)+".png")
            h2 = im2.histogram()
            rms.append(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )                   
        c=rms.index(min(rms))
        self.myPosition=c
        print('MyPos is '+str(c))
    def countAllins(self):
        n=0
        guyAllin='n'
        button='n'
        if(self.myPosition==0):#BIG BLIND   
            arr=[0,0,0]
            pyautogui.screenshot(filelocationforAllins[0],region=self.player1Pos)
            pyautogui.screenshot(filelocationforAllins[1],region=self.player2Pos)
            pyautogui.screenshot(filelocationforAllins[2],region=self.player3Pos)
            for index in range(0,len(filelocationforAllins)):
                im1=Image.open(filelocationforAllins[index])
                h1 = im1.histogram()
                im2=Image.open(locationOfTest+"database/"+"allin"+".png")
                h2 = im2.histogram()
                rms=(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )                   
                if(rms<6):
                    n=n+1
                    arr[index]=1
            if(n==3):
                print('Allin is 3')
            if(n==2):
                print('Allin is 2')
            if(n==1):
                print('Allin is 1. Checking which guy...')
                for index in range(0,len(arr)):
                    item=arr[index]
                    if(item==1):
                        print('Guy at '+str(item)+' is allin')
                        guyAllin=str(index)
                if(guyAllin==2):
                    cp='A'
                else:
                    if(not(self.hasButton(guyAllin))):
                        if(guyAllin==0):
                            cp='C'
                        if(guyAllin==1):
                            cp='A'
                    else:
                        if(self.hasNothing(guyAllin)):
                            cp='B'
                        else:
                            cp='A'
            if(n==0):
                print('Allin is 0')
            #BIG BLIND DONE. RETURN NO. OF ALLINS AND POSITION OF GUY ALLIN
        if(self.myPosition==1):#SMALL BLIND
            arr=[0,0,0]
            pyautogui.screenshot(filelocationforAllins[1],region=self.player2Pos)
            pyautogui.screenshot(filelocationforAllins[2],region=self.player3Pos)
            for index in range(0,len(filelocationforAllins)):
                if(index==0):#DON'T CHECK LEFT GUY NOW
                    continue
                im1=Image.open(filelocationforAllins[index])
                h1 = im1.histogram()
                im2=Image.open(locationOfTest+"database/"+"allin"+".png")
                h2 = im2.histogram()
                rms=(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )                   
                if(rms<6):
                    n=n+1
                    arr[index]=1
            if(n==3):#SHOULD NOT HAPPEN
                print('Allin is 3')
            if(n==2):
                print(arr)
                print('Allin is 2')
            if(n==1):
                print('Allin is 1. Checking which guy...')
                for index in range(0,len(arr)):
                    item=arr[index]
                    if(item==1):
                        print('Guy at '+str(item)+' is allin')
                        guyAllin=str(index)
                if(guyAllin==2):
                    cp='A'
                if(guyAllin==1):
                    if(self.hasButton(guyAllin)):
                        cp='A'
                    else:
                        cp='B'
            if(n==0):
                print('Allin is 0')
            #SMALL BLIND DONE. RETURN NO. OF ALLINS AND POSITION OF GUY ALLIN
        if(self.myPosition==2):#NONE
            arr=[0,0,0]
            pyautogui.screenshot(filelocationforAllins[2],region=self.player3Pos)
            if(self.buttonIsMine()):
                for index in range(0,len(filelocationforAllins)):
                    if(index==0 or index==1):#DON'T CHECK LEFT OR TOP GUY NOW
                        continue
                    im1=Image.open(filelocationforAllins[index])
                    h1 = im1.histogram()
                    im2=Image.open(locationOfTest+"database/"+"allin"+".png")
                    h2 = im2.histogram()
                    rms=(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )                   
                    if(rms<6):
                        n=n+1
                        arr[index]=1
                if(n==3):#SHOULD NOT HAPPEN
                    print('Allin is 3')
                if(n==2):#SHOULD NOT HAPPEN
                    print('Allin is 2')
                if(n==1):
                    print('Allin is 1')
                if(n==0):
                    print('Allin is 0')
            else:
                button='b'
                n=0
        print('Final allins is '+str(n))
        self.button=button
        self.allinCount=n
        self.guyAllin=str(guyAllin)
    def isDealt(self):
        #check if allin button exists in the region using rms
        print('Checking if dealt')
        color1=pyautogui.pixel(self.allinPixelPosition[0],self.allinPixelPosition[1])
        color2=NOTDEALT
        Diff=[0,0]
        Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        color2=DEALT
        Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        print(Diff[0])
        print(Diff[1])
        c=Diff.index(min(Diff))
        if(c==1):
            print('Dealt for once !!')
            print('Checking if dealt again')
            time.sleep(1)
            color1=pyautogui.pixel(self.allinPixelPosition[0],self.allinPixelPosition[1])
            color2=NOTDEALT
            Diff=[0,0]
            Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            color2=DEALT
            Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
            print(Diff[0])
            print(Diff[1])
            c=Diff.index(min(Diff))
            if(c==1):
                print('Dealt confirmed twice')
                #time.sleep(1)
                return 1
            else:
                print('Not Dealt NOT confirmed twice')
                return 0
        else:
            print('Not Dealt !!')
            return 0
    def isDealt1(self):
        #check if allin button exists in the region using rms
        print('Checking if dealt')
        Diff=[0,0,0]
        color1=pyautogui.pixel(self.yellowPixelPosition[0],self.yellowPixelPosition[1])
        color2=NOTTURN1
        Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        color2=NOTTURN2
        Diff[2]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        color2=TURN
        Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
        c=Diff.index(min(Diff))
        if(c==1):
            print('Dealt')
            return 1
        else:
            print('Not Dealt !!')
            return 0
    def curScenario(self):  #complete
        a=self.allinCount #0,1,2,3
        b=self.myPosition #0=big 1=small 2=none
        c=self.guyAllin
        d=self.button
        myScenario=str(a)+str(b)+str(c)+str(d)
        print('Scenario is '+myScenario)
        return myScenario
            
class Card(): #complete
    suit = ""
    value = ""
    position = ()
    pixelposition=()
    def compare(self,t):
        print('Comparing cards')
        if(t.suit==self.suit and t.value==self.value):
            print('Equal')
            return 1
        else:
            print('Unequal')
            return 0

    
tables=[]

################################################initialization done##############################################
table1=Table()
card1=Card()
table1.tableno=0
table1.buttonPixelPosition=(281,481)
table1.yellowPixelPosition=(484,605)
table1.myPos=(305,477,34,12)
table1.player1Pos=(35,321,45,21)
table1.player2Pos=(311, 178,45,21)
table1.player3Pos=(588, 320,45,21)
card1.position=(287,503,53,40)                                ###FILL
card1.pixelposition=(330,506)                               ###FILL
card2=Card()
card2.position=(342,503,53,40)                                ###FILL
card2.pixelposition=(383,506)                              ###FILL
table1.myCards.append(card1)
table1.myCards.append(card2)
allinPositionx=603                                        ###FILL
allinPositiony=566                                        ###FILL
table1.allinPixelPosition=(579,566)                               ###FILL
foldPositionx=469                                        ###FILL
foldPositiony=566                                        ###FILL 
table1.allinClickPosition=(allinPositionx,allinPositiony)
table1.foldClickPosition=(foldPositionx,foldPositiony)
table1.rightguy1=(538,357,38,39)
table1.rightguy2=(604,382,38,10)
table1.nothing1PixelPos=()
table1.nothing2PixelPos=()
table1.nothing3PixelPos=()
table1.button1PixelPos=(137, 326)
table1.button2PixelPos=(395, 273)
table1.button3PixelPos=(572, 405)
tables.append(table1)


#########################################################################################################################3
    
        

def findCardColor(color1):  #complete
    color2=GREEN
    Diff=[0,0,0,0]
    Diff[0]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
    color2=BLUE
    Diff[1]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
    color2=RED
    Diff[2]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
    color2=GREY
    Diff[3]=abs(color1[0] - color2[0])+abs(color1[1] - color2[1])+abs(color1[2] - color2[2])
    c=Diff.index(min(Diff))
    print('Card color is '+str(ccode[c]))
    return ccode[c]
    
    
def findCardDeck(color,fileaddress,place): #complete
    print('Finding card number....')
    if(True):
        im1=Image.open(fileaddress)
        h1 = im1.histogram()
        rms=[]
        for i in deck:
            im2=Image.open(locationOfTest+"database/c"+str(place)+"/"+color+i+".png")
            h2 = im2.histogram()
            rms.append(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )                   
        c=rms.index(min(rms))
    print('Card number is '+deck[c])
    return(deck[c])
    
def makeDecision(curCard1,curCard2,scenario):
    #Should return 0,1
    x=0
    #Choose scenario --return 1-7
    suited=0
    if(curCard1.suit==curCard2.suit):
        suited=1
    c1=curCard1.value
    c2=curCard2.value
    c=c1+c2
    c=''.join(sorted(c))
    #we have c=kk,qq,tt and suited=1or0
    print("Current scenario before decision is "+scenario)
    if(c in p[scenario]):
        x=1
        print('ALL IN')
    else:
        x=0
        print('FOLD')
    if(suited):
        if(c in p[scenario+'s']):
            x=1
            print('ALL IN')
    return x
    
    
#################MAIN CODE###################   #complete
t=0 #tableID
i=0
print(tables[0].yellowPixelPosition)
print(tables[0].tableno)
print(tables[0].myPos)
print(tables[0].player1Pos)
print(tables[0].player2Pos)
print(tables[0].player3Pos)
print(tables[0].myCards[0].position)
print(tables[0].myCards[0].pixelposition)
print(tables[0].myCards[1].position)
print(tables[0].myCards[1].pixelposition)
print(tables[0].allinPixelPosition)
print(tables[0].allinClickPosition)
print(tables[0].rightguy1)
print(tables[0].rightguy2)

print(tables[1].yellowPixelPosition)
print(tables[1].tableno)
print(tables[1].myPos)
print(tables[1].player1Pos)
print(tables[1].player2Pos)
print(tables[1].player3Pos)
print(tables[1].myCards[0].position)#
print(tables[1].myCards[0].pixelposition)#
print(tables[1].myCards[1].position)#
print(tables[1].myCards[1].pixelposition)#
print(tables[1].allinPixelPosition)
print(tables[1].allinClickPosition)#
print(tables[1].rightguy1)
print(tables[1].rightguy2)

while(True):
    #OBSERVE
    print('Table no.'+str(t))
    if(tables[t].isDealt1()):
        """
        if(i!=0):
            print('Not first')
            prevCard1=Card()
            prevCard2=Card()
            prevCard1.suit=tables[t].myCards[0].suit
            prevCard1.value=tables[t].myCards[0].value
            prevCard2.suit=tables[t].myCards[1].suit
            prevCard2.value=tables[t].myCards[1].value
        print("t  value is *************"+str(t))
        """
        tables[t].analyse() #should return success or fail
        print('Analysis done')
        curCard1=tables[t].myCards[0]
        curCard2=tables[t].myCards[1]
        if(i!=0):
            """
            print("****************************************************************")
            print(prevCard1.suit+prevCard1.value)
            print(prevCard2.suit+prevCard2.value)
            print(curCard1.suit+curCard1.value)
            print(curCard2.suit+curCard2.value)
            print("****************************************************************")
            if(not(prevCard1.compare(curCard1) and prevCard2.compare(curCard2))):
                #not visited before 
                print('not visited before')
                tables[t].curDecision=2 #reset variable
            """
        #Decide Algorithm
        print('about to make a decision')
        x=makeDecision(curCard1,curCard2,tables[t].curScenario())
        if(x==0):
            #Click Fold
            if(tables[t].curDecision!=0 or True):
                pyautogui.moveTo(tables[t].foldClickPosition[0],tables[t].foldClickPosition[1],0.2)
                pyautogui.click()
            tables[t].curDecision=0
        else:
            #Click AllIn
            if(tables[t].curDecision!=1 or True):
                pyautogui.moveTo(tables[t].allinClickPosition[0],tables[t].allinClickPosition[1],0.2)
                pyautogui.click()
            tables[t].curDecision=1
        i=i+1
    t=1-t
    #time.sleep(1)
    print('switching to table : ' + str(t))
    













































        
    
#modifications
#leftguy-allin
#topguy-allin
#rightguy-allin done     
    
#countallins - gives number of allins properly
    
    
##############################################    
    
    
#observing all in at both tables
#TRIGGER: when dealt all in button appears
#wherever first, go 
####try analysing other table all in --multiprocessing
#read from table structure the two cards
#find info 
#make decision
####compare the info from previous deck in card
#click
####save the card info for the table

#observe all in on both tables starting with second table


#########after decision of scenario is made once , should check how many people left to come to your place. else the number of people calculated to be not allin will be false 



"""
#ALLIN COUNTER FOR POSITION=2
        if(self.myPosition==2):
            pyautogui.screenshot(locationOfTest+'rightGuy1.png',region=self.rightguy1)
            im1=Image.open(locationOfTest+'rightGuy1.png')
            h1 = im1.histogram()
            im2=Image.open(locationOfTest+"database/"+str(self.tableno)+"rightGuy1"+".png")
            h2 = im2.histogram()
            rms=(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )
            if(rms<2):
                n=0
            else:
                pyautogui.screenshot(locationOfTest+'rightGuy2.png',region=self.rightguy2)
                im1=Image.open(locationOfTest+'rightGuy2.png')
                h1 = im1.histogram()
                im2=Image.open(locationOfTest+"database/"+str(self.tableno)+"rightGuy2"+".png")
                h2 = im2.histogram()
                rms=(math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1)) )
                if(rms<2):
                    n=1
                else:
                    n=0    
        """


"""
l['00']=['']
l['22']=['']
l['31']=['']
l['32']=['']
l['00s']=[""]
l['22s']=[""]
l['31s']=[""]
l['32s']=[""]
l['30']=["ak","aa","qq","kk"]
l['30s']=[""]
l['20']=["aa","ak","kk","aq","qq","jj"]
l['20s']=[""]
l['10']=["aa","ak","kk","aq","qq","jj","aj","kq","jk","kt","jq","at","9a","tt","99","88","77","66","8a","7a","6a","5a","9k","8k","7k","6k"]
l['10s']=["56","67","78","89","9t","jt"]
l['21']=["ak","aa","qq","kk","jj"]
l['21s']=[""]
l['11']=["aa","ak","kk","aq","qq","jj","aj","kq","jk","kt","qj","at","9a","tt","99","88","77","66","8a","7a","6a","5a","9k","8k","7k","6k"]
l['11s']=["56","67","78","89","9t","jt"]
l['01']=["aa","ak","kk","aq","qq","jj","aj","kq","jk","kt","jq","at","9a","tt","99","88","77","66","55","44","33","22","8a","7a","6a","5a","4a","3a","2a","9k","8k","7k","6k"]
l['01s']=["56","67","78","89","9t","45","34","23"]
l['12']=["aa","ak","kk","aq","qq","jj","aj","kq","jk","kt","jq","at","9a","tt","99","88","77","66"]
l['12s']=["56","67","78","89","9t","jt"] 
l['02']=["aa","ak","kk","aq","qq","jj","aj","kq","jk","kt","jq","at","9a","tt","99","88","77","66","55","9k","8k"]
l['02s']=["56","67","78","89","9t","45","jt"] 
"""



"""

a1=open(locationOfTest+'testres1.txt','a')
a2=open(locationOfTest+'testres2.txt','a')
a3=open(locationOfTest+'testres3.txt','a')
a4=open(locationOfTest+'testres4.txt','a')
a1.write(k1)
a2.write(k2)
a3.write(k3)
a4.write(k4)
filenames=["C:/Users/Sree/testres1.txt","C:/Users/Sree/testres2.txt","C:/Users/Sree/testres3.txt","C:/Users/Sree/testres4.txt"]
outfilename="C:/Users/Sree/h.txt"
with open(outfilename, 'a') as fout, fileinput.input(filenames) as fin:
    for line in fin:
        fout.write(line)
"""



"""
pyautogui.screenshot(filelocation[0],region=(288,502,16,17))
pyautogui.screenshot(filelocation[1],region=(342,502,16,17))
pyautogui.screenshot(filelocation[2],region=(967,502,16,17))
pyautogui.screenshot(filelocation[3],region=(1019,502,16,17))
x1=pyautogui.pixel(330,506)
x2=pyautogui.pixel(383,506)
x3=pyautogui.pixel(1007,506)
x4=pyautogui.pixel(1063,506)
k1=findCardColor(x1)
k2=findCardColor(x2)
k3=findCardColor(x3)
k4=findCardColor(x4)
"""
"""
os.system('tesseract.exe '+filelocation[0]+' '+locationOfTest+'testres1 -psm 10 nobatch poker')
os.system('tesseract.exe '+filelocation[1]+' '+locationOfTest+'testres2 -psm 10 nobatch poker')
os.system('tesseract.exe '+filelocation[2]+' '+locationOfTest+'testres3 -psm 10 nobatch poker')
os.system('tesseract.exe '+filelocation[3]+' '+locationOfTest+'testres4 -psm 10 nobatch poker')
"""
"""
os.system('tesseract.exe C:/Users/Sree/p0.png C:/Users/Sree/testres1 -psm 10 nobatch poker')
os.system('tesseract.exe C:/Users/Sree/p1.png C:/Users/Sree/testres2 -psm 10 nobatch poker')
os.system('tesseract.exe C:/Users/Sree/p2.png C:/Users/Sree/testres3 -psm 10 nobatch poker')
os.system('tesseract.exe C:/Users/Sree/p3.png C:/Users/Sree/testres4 -psm 10 nobatch poker')
"""
"""
im1=Image.open("C:/Users/Sree/p1.png")
im2=Image.open("C:/Users/Sree/p2.png")
h1 = im1.histogram()
h2 = im2.histogram()
rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
"""
