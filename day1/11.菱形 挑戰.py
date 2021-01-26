from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

time.sleep(3)
x,y,z=mc.player.getTilePos()

mc.setBlock(x-1,y,z+2,206)
mc.setBlock(x-2,y,z+1,206)
mc.setBlock(x,y,z+3,206)

mc.setBlock(x+2,y,z+1,206)
mc.setBlock(x+1,y,z+2,206)
mc.setBlock(x+3,y,z,206)

mc.setBlock(x+2,y,z-1,206)
mc.setBlock(x+1,y,z-2,206)
mc.setBlock(x,y,z-3,206)

mc.setBlock(x-2,y,z-1,206)
mc.setBlock(x-1,y,z-2,206)
mc.setBlock(x-3,y,z,206)