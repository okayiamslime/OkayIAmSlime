from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
from time import time

def BinarySearch():
    sTime = time() 
    low = 0
    upper = 100000000
 
    while low <= upper:
        mid = (low+upper) // 2 #無條件捨棄的除法 取中間值

        if mid < r:
            low = mid + 1
            
        elif mid > r:
            upper = mid - 1
            
        else :
            print("找到答案了！ 是" + str(mid))
            print("二元搜尋法：花了" + str(time()-sTime)) 
            return       

r = randrange(0,100000001)
BinarySearch()