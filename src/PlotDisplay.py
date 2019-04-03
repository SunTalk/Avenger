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
		self.write        = True
		self.line         = None
		self.name   	  = None
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

		self.draw_context()

		if self.write and self.index < len(self.context):
			if self.name != None:#wirte namw
				self.write_context(self.name, 0, 550)
			else:
				self.draw_context()#if narrator talking draw again to cover prev name
			self.write_context(self.line, 0, 600)#write context

		if self.draw:
			for i in range(2):
				s = py.Surface((self.button_w[i], self.button_h[i]))
				s.set_alpha(128)
				s.fill(self.button_color[i])
				display.blit(s, (self.button_x[i], self.button_y[i]))
				choose_text.write()

	def write_context(self, text, x, y, size=50):
		tmp_textFont   = py.font.Font(const.PATH+const.FONTFILE+'SimHei.ttf', 50)
		tmp_texturface = tmp_textFont.render(text, True, red)
		tmp_Rec = tmp_texturface.get_rect()
		tmp_Rec.x    = x
		tmp_Rec.y    = y
		tmp_Rec.left = 25
		display.blit(tmp_texturface, tmp_Rec)

	def draw_context(self):
		for i in range(len(charList)):
			if charList[i].getName() == self.name:
				#print(self.name)
				charList[i].draw(display, MiddleCharactor)

		s = py.Surface((1200, 200))
		s.set_alpha(170)
		s.fill(gray)
		display.blit(s, (0, 600))

		s = py.Surface((const.WIDTH/4, const.HEIGHT/16))
		s.set_alpha(170)
		s.fill(cyan_blue)
		display.blit(s, (0, 550))


	def checkLine(self):
		print(self.line)
		if self.line[0].encode('UTF-8').isalpha() and self.line[0] != '(':
			if self.line[4] == ':':#main
				self.line = self.line[5:]
				self.name = '亞梭爾-雪諾'

			elif self.line[5] == ':':
				if self.line[0] == 'a':#actor
					self.name = '札爾斯-契爾'

				elif self.line[0] == 'e':#enemy
					self.name = '敵方雜魚'

				self.line = self.line[6:]
			elif self.line[7] == ':':#soldier
				self.line = self.line[8:]
				self.name = '我方雜魚'

			elif self.line[8] == ':':#teammate
				self.line = self.line[9:]
				self.name = '阿斯托爾福'
		else:
			self.line = self.line
			self.name = None

	def plot_display(self):
		if not self.show:
			if self.index < len(self.context):
				if self.context[self.index] == "choose":
					self.draw = True
				else:
					self.write = True
					self.line = self.context[self.index]
					self.checkLine()

					self.set_show()
			else:
				self.write = False
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

	def get_name(self):
		return self.name

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

	def reset_write():
		self.write = False

	def clearContext(self):
		self.context.clear()
		self.reset_finish()
		self.reset_index()
		self.reset_show()
		self.reset_draw()
