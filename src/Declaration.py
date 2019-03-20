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
const.MENU_START_BUTTON_FONT            = 'LucidaBrightDemiBold.ttf'
const.MENU_START_BUTTON_SIZE            = 50

const.GAME_PAUSE_CONTINUE_BUTTON_X      = const.WIDTH*0.4
const.GAME_PAUSE_CONTINUE_BUTTON_Y      = const.HEIGHT*0.25
const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH  = const.WIDTH*0.2
const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT = const.HEIGHT*0.1
const.GAME_PAUSE_CONTINUE_BUTTON_FONT   = 'LucidaBrightDemiBold.ttf'
const.GAME_PAUSE_CONTINUE_BUTTON_SIZE   = 50

                                        ### TODO
const.MENU_QUIT_BUTTON_X                = const.WIDTH*0.1
const.MENU_QUIT_BUTTON_Y                = const.HEIGHT*0.5
const.MENU_QUIT_BUTTON_WIDTH            = const.WIDTH*0.1
const.MENU_QUIT_BUTTON_HEIGHT           = const.HEIGHT*0.1
const.MENU_QUIT_BUTTON_FONT             = 'LucidaBrightDemiBold.ttf'
const.MENU_QUIT_BUTTON_SIZE             = 50

const.INFO_BACK_BUTTON_X                = const.WIDTH*0.125
const.INFO_BACK_BUTTON_Y                = const.HEIGHT - 5*(const.HEIGHT*0.1)
const.INFO_BACK_BUTTON_WIDTH            = const.WIDTH*0.125
const.INFO_BACK_BUTTON_HEIGHT           = const.HEIGHT*0.1
const.INFO_BACK_BUTTON_FONT             = 'LucidaBrightDemiBold.ttf'
const.INFO_BACK_BUTTON_SIZE             = 50

const.GAME_PAUSE_LEFT_BUTTON_X          = const.WIDTH*0.4
const.GAME_PAUSE_LEFT_BUTTON_Y          = const.HEIGHT*0.75
const.GAME_PAUSE_LEFT_BUTTON_WIDTH      = const.WIDTH*0.2
const.GAME_PAUSE_LEFT_BUTTON_HEIGHT     = const.HEIGHT*0.1
const.GAME_PAUSE_LEFT_BUTTON_FONT       = 'LucidaBrightDemiBold.ttf'
const.GAME_PAUSE_LEFT_BUTTON_SIZE       = 50

###

##

## rgb
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
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

