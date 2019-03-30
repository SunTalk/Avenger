import pygame as py
from Declaration import *
from KeyHandler import *

keyHandler = KeyHandler()

class PlotDisplay():
	
	def __init__(self):
		self.show    = False
		self.index   = 0
		self.context = list()
		self.finish  = False

	def load_plot(self, WORLD_LINE, CHAPTER, ACT):

		dialogue_file = None

		load = False

		if ACT == const.ACT_CHOOSE:
			dialogue_file = WORLD_LINE+'_'+str(CHAPTER)+'_choose.txt'
			fp = open(const.PATH+const.DIALOGUE+dialogue_file)
		else:
			dialogue_file = WORLD_LINE+'_'+str(CHAPTER)+'_'+str(ACT)+'.txt'
			fp = open(const.PATH+const.DIALOGUE+dialogue_file)

		lines = fp.readlines()
		for i in range(len(lines)):
			if lines[i] == "[dialogue]\n":
				load = True
				continue
			if load:
				self.context.append(lines[i].rstrip('\n'))
		print(dialogue_file + "loaded")
		print(self.context)

	def plot_display(self):

		if not self.show:
			if self.index < len(self.context):
				print(self.context[self.index])
				self.set_show()
			else:
				print("plot finish")
				self.set_finish()

		if keyHandler.getKey() == py.K_RETURN:
			self.index += 1
			self.reset_show()

	def reset_index(self):
		self.index = 0

	def set_show(self):
		self.show = True

	def reset_show(self):
		self.show = False

	def set_finish(self):
		self.finish = True

	def reset_finish(self):
		self.finish = False

	def isfinish(self):
		return self.finish
