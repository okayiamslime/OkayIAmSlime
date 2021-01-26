from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()

wigth =10       #寬
height=5        #高
length=6        #長

mc.setBlocks(x,y,z,x+wigth,y+height,z+length,4) #4=建材
mc.setBlocks(x+1,y+1,z+1,x+wigth-1,y+height-1,z+length-1,0) #0=空氣