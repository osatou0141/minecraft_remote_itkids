from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)


# 正方形
def square(x, y, z, s):
    scale = s - 1
    mc.setBlocks(x, y, z, x + scale, y + scale, z + scale, param.GOLD_BLOCK)


# 長方形 #
def rectangle(x, y, z, xs, zs, h):
    xsize = xs - 1
    zsize = zs - 1
    high = h - 1
    mc.setBlocks(x, y, z, x + xsize, y + high, z + zsize, param.IRON_BLOCK)


# ひし形 #
def rhombus(x, y, z, s, j, d):
    s = d
    d = s
    h = 1
    n = h - 1
    length = j - 1
    mc.setBlocks(x, y, z - n, x + length, y, z + n, param.DIAMOND_BLOCK)
