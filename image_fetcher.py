import operator
from functools import reduce
import os
import math
import pyautogui
from PIL import Image
from random import randint
import time
import fileinput
fileparent=["C:/Users/d0","C:/Users/d1","C:/Users/d2","C:/Users/d3"]
filelocation=['','','','']
while(True):
    for i in range(0,4):
        rand1=randint(0,9)
        rand2=randint(0,9)
        rand3=randint(0,9)
        rand4=randint(0,9)
        filelocation[i]=fileparent[i]+'img'+str(i)+'card'+str(rand1)+str(rand2)+str(rand3)+str(rand4)+'.png'
        print(filelocation[i])
    pyautogui.screenshot(filelocation[0],region=(287,503,53,40))
    pyautogui.screenshot(filelocation[1],region=(342,503,53,40))
    pyautogui.screenshot(filelocation[2],region=(965,503,53,40))
    pyautogui.screenshot(filelocation[3],region=(1020,503,53,40))
    time.sleep(2)

