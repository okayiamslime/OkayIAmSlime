from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from random import randrange


for i in range(100):
    x,y,z = mc.player.getTilePos()
    x = x + i
    
    for j in range(100):
        r = randrange(0,16)
        z = z + 1
        mc.setBlock(x,y,z,35,r)