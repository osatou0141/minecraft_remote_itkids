from mcje.minecraft import Minecraft
import param_MCJE as param
import sheep as sh

mc = Minecraft.create(port=param.PORT_MC)

x = 0
y = 63
z = 0
sh.reset(x, y, z)
