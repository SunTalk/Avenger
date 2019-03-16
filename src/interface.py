from Declaration import *

class interface():

	def __init__(self):
		pass
	
	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def loadUI(self, path, file, name):
		self.backgroundImg = py.image.load(path+file+name)
		print("{} loaded".format(name))

	def update(self, drawBotton):
		self.draw()

		if drawBotton:
			self.draw_start_botton()
			self.write()

		## better write in game loop
		py.display.update()
		##

	def draw(self):
		display.blit(self.backgroundImg, (0, 0))

	def draw_start_botton(self):
		py.draw.rect(display, self.start_botton_color, [self.start_botton_x, self.start_botton_y, self.start_botton_width, self.start_botton_height])

	def write(self):
		self.message(self.start_botton_text)
		display.blit(self.textSurface, self.textRec)

	def message(self, text):
		self.textFont    	= py.font.Font(const.PATH+const.FONTFILE+self.start_botton_font, self.start_botton_font_size)
		self.textSurface 	= self.textFont.render(text, True, red)
		self.textRec     	= self.textSurface.get_rect()
		self.textRec.center = ((self.start_botton_x+(self.start_botton_width/2), (self.start_botton_y+(self.start_botton_height/2))))


	def set_start_botton(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, start_type=0):
		if start_type == const.MENU:
			print("type = MENU")
			self.start_botton_x 	 	= const.MENU_START_BUTTON_X
			self.start_botton_y 	 	= const.MENU_START_BUTTON_Y
			self.start_botton_width  	= const.MENU_START_BUTTON_WIDTH
			self.start_botton_height 	= const.MENU_START_BUTTON_HEIGHT
			self.start_botton_color  	= white
			self.start_botton_text   	= "Start"
			self.start_botton_font   	= const.MENU_START_BUTTON_FONT
			self.start_botton_font_size = const.MENU_START_BUTTON_SIZE
		
		elif start_type == const.GAME_PAUSE:
			print("type = GAME_PAUSE")
			self.start_botton_x 	 	= const.GAME_PAUSE_CONTINUE_BUTTON_X
			self.start_botton_y 	 	= const.GAME_PAUSE_CONTINUE_BUTTON_Y
			self.start_botton_width  	= const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH
			self.start_botton_height 	= const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT
			self.start_botton_color  	= white
			self.start_botton_text   	= "Continue"
			self.start_botton_font   	= const.GAME_PAUSE_CONTINUE_BUTTON_FONT
			self.start_botton_font_size = const.GAME_PAUSE_CONTINUE_BUTTON_SIZE 

		else:
			print("type = CUSTOM")
			self.start_botton_x 	 	= x
			self.start_botton_y 	 	= y
			self.start_botton_width  	= width
			self.start_botton_height 	= height
			self.start_botton_color  	= color
			self.start_botton_text   	= text
			self.start_botton_font   	= font
			self.start_botton_font_size = size
