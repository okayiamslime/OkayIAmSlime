from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()


mc.setBlocks(x+30,y-1,z   ,x,y+10,z+10      ,172)
mc.setBlocks(x+29,y,z+1   ,x+1,y+9,z+9      ,0)
mc.setBlocks(x,y,z+2      ,x,y+1,z+2        ,0)
mc.setBlocks(x+30,y+10,z  ,x,y+10,z+10      ,169)

   