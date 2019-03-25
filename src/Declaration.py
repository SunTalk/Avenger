import pygame as py
import time
import random
import const
import numpy as np
import os
from block_center import *
from Image import *
# from multipledispatch import dispatch

Font_EN = 'LucidaBrightDemiBold.ttf'

## const variable

const.WIDTH 	 = 1200
const.HEIGHT 	 = 800

const.UINAME    = [None, 'MENU', 'INFO', 'PLOT', 'STORY', 'GAME_PLAY', None, 'GAME_FINISH']
const.MUSICNAME = [None, 'MENU', None, None, 'STORY', ['battle_1_2', '3-1', '3-2'], None, 'GAME_FINISH']

const.GAME_NONE   = 0
const.MENU        = 1
const.INFO        = 2
const.PLOT        = 3
const.STORY       = 4
const.GAME_PLAY   = 5
const.GAME_PAUSE  = 6
const.GAME_FINISH = 7
const.OTHER       = 8

const.PATH       = os.getcwd()
const.MUSICFILE  = '\\data\\music\\'
const.UIFILE     = '\\data\\UI\\'
const.FONTFILE   = '\\data\\Font\\'

const.GAME_LOOP  = True

const.MENU_START_BUTTON_X               = const.WIDTH*0.1
const.MENU_START_BUTTON_Y               = const.HEIGHT*0.1
const.MENU_START_BUTTON_WIDTH           = const.WIDTH*0.1
const.MENU_START_BUTTON_HEIGHT          = const.HEIGHT*0.1
const.MENU_START_BUTTON_FONT            = Font_EN
const.MENU_START_BUTTON_SIZE            = 50

const.GAME_PAUSE_CONTINUE_BUTTON_X      = const.WIDTH*0.4
const.GAME_PAUSE_CONTINUE_BUTTON_Y      = const.HEIGHT*0.25
const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH  = const.WIDTH*0.2
const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT = const.HEIGHT*0.1
const.GAME_PAUSE_CONTINUE_BUTTON_FONT   = Font_EN
const.GAME_PAUSE_CONTINUE_BUTTON_SIZE   = 50

                                        ### TODO
const.MENU_QUIT_BUTTON_X                = const.WIDTH*0.1
const.MENU_QUIT_BUTTON_Y                = const.HEIGHT*0.5
const.MENU_QUIT_BUTTON_WIDTH            = const.WIDTH*0.1
const.MENU_QUIT_BUTTON_HEIGHT           = const.HEIGHT*0.1
const.MENU_QUIT_BUTTON_FONT             = Font_EN
const.MENU_QUIT_BUTTON_SIZE             = 50

const.INFO_BACK_BUTTON_X                = const.WIDTH*0.125
const.INFO_BACK_BUTTON_Y                = const.HEIGHT - 5*(const.HEIGHT*0.1)
const.INFO_BACK_BUTTON_WIDTH            = const.WIDTH*0.125
const.INFO_BACK_BUTTON_HEIGHT           = const.HEIGHT*0.1
const.INFO_BACK_BUTTON_FONT             = Font_EN
const.INFO_BACK_BUTTON_SIZE             = 50

const.GAME_PAUSE_LEFT_BUTTON_X          = const.WIDTH*0.4
const.GAME_PAUSE_LEFT_BUTTON_Y          = const.HEIGHT*0.75
const.GAME_PAUSE_LEFT_BUTTON_WIDTH      = const.WIDTH*0.2
const.GAME_PAUSE_LEFT_BUTTON_HEIGHT     = const.HEIGHT*0.1
const.GAME_PAUSE_LEFT_BUTTON_FONT       = Font_EN
const.GAME_PAUSE_LEFT_BUTTON_SIZE       = 50

###

##

image = Image()

## rgb
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
orangered = (255,69,0)
yellow = (255,255,0)
green = (0, 255, 0)
blue = (0,0,255)
purple = (128,0,128)
cyan_blue = (0, 255, 255)
gray      = (204, 204, 204)
##

## display

display = py.display.set_mode((const.WIDTH, const.HEIGHT))
py.display.set_caption('Avenger')

##

## clock
clock = py.time.Clock()
##


##
GAME_SATE = const.GAME_NONE
##


## function

def load_built_in_UI():

	for i in range(const.MENU, const.OTHER):
		if(i == const.GAME_PAUSE):
			image.loadUI(const.UIFILE, None)
			continue
		image.loadUI(const.UIFILE, const.UINAME[i]+'.jpg')

##

