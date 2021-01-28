from mcpi.minecraft import Minecraft
mc = Minecraft.create()

list2d =[[67,41,14],[35,46,83]]

myID = mc.getPlayerEntityId("APE_35")
x,y,z=mc.entity.getTilePos(myID)
startX =x

for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        
        x=x+1
    x=startX
    z=z+1