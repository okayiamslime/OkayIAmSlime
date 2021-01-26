from mcpi.minecraft import Minecraft
mc=Minecraft.create()




x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,206)