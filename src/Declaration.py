import pygame as py
import time
import random
import const
import numpy as np
import os
from block_center import *

## const variable

const.WIDTH 	 = 1200
const.HEIGHT 	 = 800

const.PATH       = os.getcwd()
const.MUSICFILE  = '\\data\\music\\'
const.UIFILE     = '\\data\\UI\\'

const.GAME_LOOP  = True
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
