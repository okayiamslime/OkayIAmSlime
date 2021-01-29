from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def build(x,y,z,base):
    mc.setBlocks(x,y-1,z,x+10,y-1,z+10, 2)
    mc.setBlocks(x+1,y-1,z+1,x+9,y-1,z+9, 0)
    
    mc.setBlock(x+1,y,z, 28)
    mc.setBlocks(x+2,y,z,x+3,y,z ,27)
    mc.setBlocks(x+4,y,z,x+10,y,z,66)
    mc.setBlocks(x+10,y,z+1,x+10,y,z+10,66)
    
    mc.setBlock(x+9,y,z+10, 28)
    mc.setBlocks(x+8,y,z+10,x+6,y,z+10 ,27)
    mc.setBlocks(x+5,y,z+10,x,y,z+10,66)
    mc.setBlocks(x,y,z+9,x,y,z,66)
    
    


    
x,y,z = mc.player.getTilePos()
build(x,y,z,20)