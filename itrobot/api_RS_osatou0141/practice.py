from mcje.minecraft import Minecraft
import param_MCJE as param
import sheep as sh

mc = Minecraft.create(port=param.PORT_MC)

sh.spawn(0, 63, 0)
