from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

time.sleep(3)
x,y,z=mc.player.getTilePos()

mc.setBlock(x-1,y,z+1,206)
mc.setBlock(x,y,z+1,206)
mc.setBlock(x+1,y,z+1,206)
mc.setBlock(x+1,y,z,206)
mc.setBlock(x+1,y,z-1,206)
mc.setBlock(x,y,z-1,206)
mc.setBlock(x-1,y,z-1,206)
mc.setBlock(x-1,y,z,206)