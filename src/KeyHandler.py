import pygame as py
from Declaration import *

class KeyHandler():

	def __init__(self):
		self.Kstate = None

	def setKey(self, event):
		if event.type == py.KEYUP:
			self.Kstate = event.key

	def getKey(self):
		tmp = self.Kstate
		self.resetKey()
		return tmp

	def resetKey(self):
		self.Kstate = None
				