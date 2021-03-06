from pygame.locals import *
import pygame as py
import time
import random
import datetime
import const
import numpy as np
import os
from block_center import *
from Image import *
from CharactorImage import *
# from board import *

# set datetime to random seed
random.seed(datetime.datetime.now())
py.HWSURFACE = True
# from multipledispatch import dispatch

Font_EN = 'LucidaBrightDemiBold.ttf'

## const variable

const.WIDTH 	 = 1200
const.HEIGHT 	 = 800

const.UINAME    = [None, 'MENU', 'INFO', None, None, 'GAME_PLAY', None, 'GAME_FINISH','LOADING', 'DOUBLEPLAYER']
const.MUSICNAME = [None, 'MENU', 'INFO', 'PLOT', 'STORY', None, None, 'GAME_FINISH', None, 'DOUBLE']
const.PLOTMX_W  = 'X_W'
const.PLOTMX_L	= 'X_L'
const.PLOTMZ_W	= 'Z_W'
const.PLOTMZ_L  = 'Z_L'
const.BATTLEM   = [None, 'N', 'X_3', 'Z_3']
const.PLOT_UI   = [None, '1', '2', 'X_3', 'Z_3']
const.CHARACTOR = [None, '亞梭爾-雪諾', '札爾斯-契爾', '阿斯托爾福', '我方雜魚', '敵方雜魚']

const.PLOT_1	= 1
const.PLOT_2	= 2
const.PLOT_3_X  = 3
const.PLOT_3_Z  = 4


const.WORLD_LINE_N = 'N'
const.WORLD_LINE_X = 'X'
const.WORLD_LINE_Z = 'Z'

const.CHAPTER_N   = 0
const.CHAPTER_1   = 1
const.CHAPTER_2   = 2
const.CHAPTER_3   = 3

const.ACT_N       = 0
const.ACT_1       = 1
const.ACT_2       = 2
const.ACT_F       = 3
const.GAME_NONE   = 0
const.MENU        = 1
const.INFO        = 2
const.PLOT        = 3
const.STORY       = 4
const.GAME_PLAY   = 5
const.GAME_PAUSE  = 6
const.GAME_FINISH = 7
const.LOADING     = 8
const.DOUBLE      = 9
const.OTHER       = 10

const.LEVEL_NONE  = 0
const.LEVEL_ONE   = 1
const.LEVEL_TWO   = 2
const.LEVEL_THREE = 3


const.PATH       = os.getcwd()
const.MUSICFILE  = '\\data\\music\\'
const.UIFILE     = '\\data\\UI\\'
const.FONTFILE   = '\\data\\Font\\'
const.DIALOGUE   = '\\data\\dialogue\\'

const.GAME_LOOP  = True

const.MENU_START_BUTTON_X               = const.WIDTH*0.1
const.MENU_START_BUTTON_Y               = const.HEIGHT*0.2
const.MENU_START_BUTTON_WIDTH           = const.WIDTH*0.2
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
const.MENU_QUIT_BUTTON_Y                = const.HEIGHT*0.6
const.MENU_QUIT_BUTTON_WIDTH            = const.WIDTH*0.2
const.MENU_QUIT_BUTTON_HEIGHT           = const.HEIGHT*0.1
const.MENU_QUIT_BUTTON_FONT             = Font_EN
const.MENU_QUIT_BUTTON_SIZE             = 50

const.INFO_BACK_BUTTON_X                = const.WIDTH*0.85
const.INFO_BACK_BUTTON_Y                = const.HEIGHT*0.75
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

const.ONE_PLAYER = 1
const.TWO_PLAYER = 2

const.MAIN_CHARACTOR     = 1
const.ACTOR_CHARACTOR    = 2
const.TEAMMATE_CHARACTOR = 3
const.SOLDIER_CHARACTOR  = 4
const.ENEMY_CHARACTOR    = 5

###

obstacle_list = []
soldier_list  = []
enemy_list    = []

const.WIN  = 1
const.LOSE = 2 
const.FLAT = 3

## display
py.init()
display = py.display.set_mode((const.WIDTH, const.HEIGHT))
py.display.set_caption('Avenger')

##
##

image      = Image()
plot_image = Image()
mainC      = CharactorImage()
actorC     = CharactorImage()
teammateC  = CharactorImage()
soldierC   = CharactorImage()
enemyC     = CharactorImage()

charList = [mainC, actorC, teammateC, soldierC, enemyC]
LeftCharactor   = (200, 250)
MiddleCharactor = (500, 250)
RightCharactor  = (800, 250)
## rgb
black     = (0, 0, 0)
white     = (255, 255, 255)
red       = (255, 0, 0)
orangered = (255,69,0)
yellow    = (255,255,0)
gold      = (255, 191, 0)
green     = (0, 255, 0)
blue      = (0,0,255)
purple    = (128,0,128)
cyan_blue = (0, 255, 255)
gray      = (204, 204, 204)

trans_white = (255, 255, 255, 0)
trans_red   = (255, 0, 0, 100)
##


## clock
clock = py.time.Clock()
##


##
GAME_STATE    = const.GAME_NONE
PLAYING_STATE = const.LEVEL_NONE
WORLD_LINE    = const.WORLD_LINE_N
CHAPTER 	  = const.CHAPTER_N
ACT 		  = const.ACT_N

fps = 60
##




