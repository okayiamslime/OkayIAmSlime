from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from random import choice

cool=[14,15,16,56,73,46]

r=choice(cool)

myID=mc.getPlayerEntityId("APE_35")
x,y,z=mc.entity.getTilePos(myID)

mc.setBlock(x,y,z,r)