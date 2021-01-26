from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setSign(x,y,z,68,0,"我愛","Minecraft","","也愛python")


  # 0=預設 2 北 3南 4 西 5 東    0~15
       
   