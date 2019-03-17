import pygame as py
import time
import random
import const
import numpy as np
import os
from block_center import *
# from multipledispatch import dispatch

## const variable

const.WIDTH 	 = 1200
const.HEIGHT 	 = 800

const.MENU        = 1
const.INFO        = 2
const.PLOT        = 3
const.STORY       = 4
const.GAME_PLAY   = 5
const.GAME_PAUSE  = 6
const.GAME_FINISH = 7

const.PATH       = os.getcwd()
const.MUSICFILE  = '\\data\\music\\'
const.UIFILE     = '\\data\\UI\\'
const.FONTFILE   = '\\data\\Font\\'

const.GAME_LOOP  = True

const.MENU_START_BUTTON_X 	   			= const.WIDTH/10
const.MENU_START_BUTTON_Y 	   			= const.HEIGHT/10
const.MENU_START_BUTTON_WIDTH  			= const.WIDTH/10
const.MENU_START_BUTTON_HEIGHT 			= const.HEIGHT/10
const.MENU_START_BUTTON_FONT   			= 'LucidaBrightDemiBold.ttf'
const.MENU_START_BUTTON_SIZE   			= 50
const.GAME_PAUSE_CONTINUE_BUTTON_X		= const.WIDTH*0.4
const.GAME_PAUSE_CONTINUE_BUTTON_Y		= const.HEIGHT*0.25
const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH	= const.WIDTH/5
const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT = const.HEIGHT/10
const.GAME_PAUSE_CONTINUE_BUTTON_FONT   = 'LucidaBrightDemiBold.ttf'
const.GAME_PAUSE_CONTINUE_BUTTON_SIZE   = 50
##

## rgb
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
cyan_blue = (0, 255, 255)
##

## display

display = py.display.set_mode((const.WIDTH, const.HEIGHT))
py.display.set_caption('Avenger')

##

## clock
clock = py.time.Clock()
##

## dictionary



##

