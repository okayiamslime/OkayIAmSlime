from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
time.sleep(3)

x,y,z=mc.player.getTilePos()

while True:
    color=random.randrange(0,16)   #玻璃為0~15
    mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,color)
    time.sleep(0.5)