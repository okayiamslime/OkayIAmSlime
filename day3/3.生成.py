from mcpi.minecraft import Minecraft
mc=Minecraft.create()



x,y,z=mc.player.getPos()
mc.spawnEntity(x,y,z,93)
  
        
        
        