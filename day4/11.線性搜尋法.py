from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
from time import time

def LinearSearch():
    startTime=time()
    for i in range(100000001):
        if r == i:
            print("找到答案了! 是"+str(i))
            print("線性搜尋法:花了"+str(time()-startTime)+"秒")
            break
        
   
r = randrange(0,100000001)
LinearSearch()
