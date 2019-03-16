from Declaration import *

class interface():

	def __init__(self):
		pass
	
	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def loadUI(self, path, file, name):
		self.img = py.image.load(path+file+name)
		print("{} loaded".format(name))

	def update(self, drawBotton):
		self.draw()

		if drawBotton:
			self.draw_start_botton(self.start_botton_x, self.start_botton_y, self.start_botton_width, self.start_botton_height, self.start_botton_color)

		py.display.update()

	def draw(self):
		display.blit(self.img, (0, 0))

	def draw_start_botton(self, x, y, width, height, color):
		py.draw.rect(display, color, [x, y, width, height])

	def set_start_botton(self, x=0, y=0, width=0, height=0, color=0, text=None, start_type=0):
		if start_type == const.MENU:
			print("type")
			self.start_botton_x 	 = const.MENU_START_BUTTON_X
			self.start_botton_y 	 = const.MENU_START_BUTTON_Y
			self.start_botton_width  = const.MENU_START_BUTTON_WIDTH
			self.start_botton_height = const.MENU_START_BUTTON_HEIGHT
			self.start_botton_color  = white
			self.start_botton_text   = "Start"
		
		elif start_type == const.GAME_PAUSE:
			self.start_botton_x 	 = const.GAME_PAUSE_CONTINUE_BUTTON_X
			self.start_botton_y 	 = const.GAME_PAUSE_CONTINUE_BUTTON_Y
			self.start_botton_width  = const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH
			self.start_botton_height = const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT
			self.start_botton_color  = white
			self.start_botton_text   = "Continue"

		else:
			self.start_botton_x 	 = x
			self.start_botton_y 	 = y
			self.start_botton_width  = width
			self.start_botton_height = height
			self.start_botton_color  = color
			self.start_botton_text   = text


