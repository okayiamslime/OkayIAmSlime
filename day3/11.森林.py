from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z=mc.player.getTilePos()


def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
time.sleep(2)                             #延遲開始的時間
for i in range(10):
    time.sleep(0.5)                       #延遲x軸的時間  
    for j in range(5):
        time.sleep(0.5)                   #延遲z軸的時間
        plantTree(x+ i*5 ,y,z+j*6)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


          
        
        