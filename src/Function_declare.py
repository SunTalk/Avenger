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

show 	   = False
plot_index = 0


def load_built_in_UI():

	for i in range(const.MENU, const.OTHER):
		if(i == const.GAME_PAUSE):
			image.loadUI(const.UIFILE, None)
			continue
		image.loadUI(const.UIFILE, const.UINAME[i]+'.jpg')


def transitions(level):

	global WORLD_LINE
	global CHAPTER
	global ACT

	if GAME_STATE == const.PLOT or GAME_STATE == const.GAME_PLAY:
		
		ACT += 1
		if ACT == const.ACT_CHOOSE and CHAPTER != const.CHAPTER_2:
			ACT = const.ACT_1
			CHAPTER += 1
		
		if ACT == 4:
			ACT = const.ACT_1
			CHAPTER += 1


	if level == const.LEVEL_ONE:
		level_one_set()
	elif level == const.LEVEL_TWO:
		level_two_set()
	elif level == const.LEVEL_THREE:
		level_three_set()
