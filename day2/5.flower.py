from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getTilePos()


while True:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)