import pygame as py
from Declaration import *
from KeyHandler import *
from textHandler import *

keyHandler  = KeyHandler()
choose_text = textHandler()

class PlotDisplay():
	
	def __init__(self):
		self.show         = False
		self.index        = 0
		self.context      = list()
		self.finish       = False
		self.button_color = [black, black]
		self.button_x	  = [const.WIDTH*0.3, const.WIDTH*0.3]
		self.button_y	  =	[const.HEIGHT*0.1, const.HEIGHT*0.5]
		self.button_w	  = [const.WIDTH*0.4, const.WIDTH*0.4]
		self.button_h	  = [const.HEIGHT*0.2, const.HEIGHT*0.2]
		self.press        = [False, False]
		self.draw         = False
		choose_text.setText("殺", const.WIDTH/2, const.HEIGHT/5, 'SimHei.ttf', size=100)
		choose_text.setText("不殺", const.WIDTH/2, const.HEIGHT/1.65, 'SimHei.ttf', size=100)

	def load_plot(self, WORLD_LINE, CHAPTER, ACT):

		dialogue_file = None

		load = False

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

	def event_handle(self, event):
		if self.draw:
			for i in range(2):
				if (py.mouse.get_pos()[0] > self.button_x[i]) and (py.mouse.get_pos()[0] < self.button_x[i]+self.button_w[i]):
					if (py.mouse.get_pos()[1] > self.button_y[i]) and (py.mouse.get_pos()[1] < self.button_y[i]+self.button_h[i]):
						self.button_color[i] = gray
						if event.type == py.MOUSEBUTTONDOWN:
							self.press[i] = True
							print("pressed")
							self.set_finish()
					else:
						self.button_color[i] = black
						self.press[i] = False
				else:
					self.button_color[i] = black
					self.press[i] = False

	def update(self):
		if self.draw:
			for i in range(2):
				s = py.Surface((self.button_w[i], self.button_h[i]))
				s.set_alpha(128)
				s.fill(self.button_color[i])
				display.blit(s, (self.button_x[i], self.button_y[i]))
				choose_text.write()


	def plot_display(self):

		if not self.show:
			if self.index < len(self.context):
				if self.context[self.index] == "choose":
					self.draw = True
				else:
					print(self.context[self.index])
					self.set_show()
			else:
				print("plot finish")
				self.set_finish()

		if keyHandler.getKey() == py.K_RETURN and self.context[self.index] != "choose":
			self.index += 1
			self.reset_show()
	def toChoose(self):
		for i in range(len(self.context)):
			if self.context[i] == 'choose':
				self.index = i
				self.reset_show()
				break;

	def reset_press(self):
		for i in range(2):
			self.press[i] = False

	def reset_index(self):
		self.index = 0

	def reset_draw(self):
		self.draw = False

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

	def clearContext(self):
		self.context.clear()
		self.reset_finish()
		self.reset_index()
		self.reset_show()
		self.reset_draw()
