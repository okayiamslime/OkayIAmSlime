from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(5)

x=236
y=64
z=236

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
x=x+2
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
x=x+2
mc.player.setTilePos(x,y,z)
