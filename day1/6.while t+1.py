from mcpi.minecraft import Minecraft
mc=Minecraft.create()

t=0

while True:
    t=t+1
    mc.postToChat("第"+ t +"次")
    
    #1.t是數字不是字串
    
    #2.怎麼讓數字變慢?