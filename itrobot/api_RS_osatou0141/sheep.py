from mcje.minecraft import Minecraft
import param_MCJE as param
import sheep_api as sa
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)

sa.spawn()
sleep(3)
sa.despawn()
