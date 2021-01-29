from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()


x,y,z=mc.player.getPos()

while True:
    x=x+random.uniform(-10, 10)
    z=z+random.uniform(-10, 10)
    y=y+10
    mc.spawnEntity(x,y,z,99)
    time.sleep(0.1)
  
        
        
        