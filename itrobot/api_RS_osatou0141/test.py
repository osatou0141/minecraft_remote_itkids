from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)


# 正方形
def square(x, y, z, s, mate):
    if mate == 0:
        mate = param.GOLD_BLOCK
    scale = s - 1
    mc.setBlocks(x, y, z, x + scale, y + scale, z + scale, mate)


# 長方形 #
def rectangle(x, y, z, xs, zs, h, mate):
    if mate == 0:
        mate = param.IRON_BLOCK
    xsize = xs - 1
    zsize = zs - 1
    high = h - 1
    mc.setBlocks(x, y, z, x + xsize, y + high, z + zsize, mate)


# ひし形 #
def rhombus(x, y, z, s, j, d, mate):
    if mate == 0:
        mate = param.DIAMOND_BLOCK
    s = d
    d = s
    h = 1
    n = h - 1
    length = j - 1
    mc.setBlocks(x, y, z - n, x + length, y, z + n, mate)


rectangle(0, 63, 0, 5, 10, 7, 0)
