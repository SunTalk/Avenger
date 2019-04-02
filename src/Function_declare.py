from Declaration import *
import pygame as py
import time
import random
import const
import numpy as np
import os
from block_center import *
from Image import *
from KeyHandler import *
from level_one import *
from level_two import *
from level_three import *
from level_four import *
from board import *

show 	   = False
plot_index = 0


def load_built_in_UI():

	for i in range(const.MENU, const.OTHER):
		if(i == const.GAME_PAUSE or i == const.PLOT or i == const.STORY):
			image.loadUI(const.UIFILE, None)
			continue
		image.loadUI(const.UIFILE, const.UINAME[i]+'.jpg')
		image.resize(const.WIDTH, const.HEIGHT, i)

	for i in range(const.PLOT_1, const.PLOT_3_Z+1):
		plot_image.loadUI(const.UIFILE, const.PLOT_UI[i]+'.jpg')
		plot_image.resize(const.WIDTH, const.HEIGHT, i)

	mainC.loadUI(const.UIFILE, const.CHARACTOR[const.MAIN_CHARACTOR])
	actorC.loadUI(const.UIFILE, const.CHARACTOR[const.ACTOR_CHARACTOR])
	teammateC.loadUI(const.UIFILE, const.CHARACTOR[const.TEAMMATE_CHARACTOR])
	soldierC.loadUI(const.UIFILE, const.CHARACTOR[const.SOLDIER_CHARACTOR])
	enemyC.loadUI(const.UIFILE, const.CHARACTOR[const.ENEMY_CHARACTOR])