from mcpi.minecraft import Minecraft
mc=Minecraft.create()

A=[]
B=[]
C=[]
for i in range(1,4):
    A.append(1*i)
for i in range(1,4):
    B.append(2*i)
for i in range(1,4):
    C.append(3*i)

print(A)
print(B)
print(C)

x,y,z=mc.player.getTilePos()
mc.setsign(x,y,z,63,0,str(A),str(B),str(C))