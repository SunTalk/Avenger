import pygame as py
import time
import random
import const
import numpy as np
import os

## const variable

const.WIDTH 	 = 1200
const.HEIGHT 	 = 600

const.PATH       = os.getcwd()
const.MUSICFILE  = '\\data\\music\\'
const.UIFILE     = '\\data\\UI\\'

const.GAME_LOOP  = True
##

## rgb
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
##

## display

display = py.display.set_mode((const.WIDTH, const.HEIGHT))

##