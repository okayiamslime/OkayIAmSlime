from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()

number = 1 #一次生成的蠹魚數量

for i in range(10): #禁止打超過8

    for j in range(number): #每次生成蠹魚的數量
        mc.spawnEntity(x,y,z,60)
        
    number = number *2
    mc.postToChat("這次生成了 " + str(number) + " 隻蠹魚") 
