from Declaration import *
import pygame as py
import const
from Image import *

show 	   = False
plot_index = 0


def load_built_in_UI():

	for i in range(const.MENU, const.OTHER):
		if(i == const.GAME_PAUSE):
			image.loadUI(const.UIFILE, None)
			continue
		image.loadUI(const.UIFILE, const.UINAME[i]+'.jpg')
		image.resize(const.WIDTH, const.HEIGHT, i)

	for i in range(const.PLOT_1, const.PLOT_3_Z+1):
		plot_image.loadUI(const.UIFILE, const.PLOT_UI[i]+'.jpg')
		plot_image.resize(const.WIDTH, const.HEIGHT, i)
