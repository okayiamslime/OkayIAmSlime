from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

time.sleep(5)
x,y,z=mc.player.getTilePos()

mc.setBlock(x,y,z,206)
mc.setBlock(x,y+1,z,206)
mc.setBlock(x,y+2,z,206)
mc.setBlock(x,y+3,z,206)
mc.setBlock(x,y+4,z,206)
mc.setBlock(x,y+5,z,206)
mc.setBlock(x,y+6,z,206)
mc.setBlock(x,y+7,z,206)
mc.setBlock(x,y+8,z,206)
mc.setBlock(x,y+9,z,206)