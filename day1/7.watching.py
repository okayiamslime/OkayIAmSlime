from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.postToChat("I am watching you.")

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You are loacted on X:"+str(x)
                                    +",Y"+str(y)
                                    +",Z"+str(z))