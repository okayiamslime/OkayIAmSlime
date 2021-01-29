from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()


def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)

for i in range(10):
    for j in range(10):
        for k in range(10):
            plantTree(x+ i*5 ,y+ i*j ,z+ i*k)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


          
        
        