from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange


r = randrange(1,16)
while True:
    hits = mc.events.pollBlockHits() 

    if len(hits) > 0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data == r:
            mc.postToChat("恭喜你找到我 >///<")
            mc.setBlock(hit.pos,57)
            break
        elif data < r:
            mc.postToChat("找錯瞜！ 試試看更大的 子ID吧")
        elif data > r:
            mc.postToChat("找錯瞜！ 試試看更小的 子ID吧")
