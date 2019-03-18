from Declaration import *

class interface():

	def __init__(self):
		pass
	
	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def loadUI(self, img):
		self.backgroundImg = img
		print("img set")

	def update(self, drawBotton):
		self.draw()

		if drawBotton:
			self.draw_botton()

		## better write in game loop
		py.display.update()
		##

	def draw(self):
		display.blit(self.backgroundImg, (0, 0))

	def draw_botton(self):
		if self.start_type != None:
			self.draw_start_botton()
			self.write()
		
		if self.back_type != None:
			self.draw_back_botton()
			self.write()

	def draw_start_botton(self):
		py.draw.rect(display, self.start_botton_color, [self.start_botton_x, self.start_botton_y, self.start_botton_width, self.start_botton_height])

	def draw_back_botton(self):
		py.draw.rect(display, self.back_botton_color, [self.back_botton_x, self.back_botton_y, self.back_botton_width, self.back_botton_height])

	def write(self):
		if self.start_type == 'start':
			self.message(self.start_botton_text, self.start_botton_font, self.start_botton_font_size)
			display.blit(self.textSurface_st, self.textRec_st)
		
		if self.back_type == 'back':
			self.message(self.back_botton_text, self.back_botton_font, self.back_botton_font_size)
			display.blit(self.textSurface_bc, self.textRec_bc)

	def message(self, text, font, size):
		self.textFont    	= py.font.Font(const.PATH+const.FONTFILE+font, size)
		
		if self.start_type == 'start':
			self.textSurface_st    = self.textFont.render(text, True, red)
			self.textRec_st        = self.textSurface_st.get_rect()
			self.textRec_st.center = ((self.start_botton_x+(self.start_botton_width/2), (self.start_botton_y+(self.start_botton_height/2))))
		else:
			pass

		if self.back_type == 'back':
			self.textSurface_bc    = self.textFont.render(text, True, red)
			self.textRec_bc        = self.textSurface_bc.get_rect()
			self.textRec_bc.center = ((self.back_botton_x+(self.back_botton_width/2), (self.back_botton_y+(self.back_botton_height/2))))
		else:
			pass

	def set_botton(self, type):
		self.set_start_botton(start_type=type)
		self.set_quit_botton(back_type=type)

	def set_start_botton(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, start_type=0):
		if start_type == const.MENU:
			print("start_type = MENU")
			self.start_botton_x 	 	= const.MENU_START_BUTTON_X
			self.start_botton_y 	 	= const.MENU_START_BUTTON_Y
			self.start_botton_width  	= const.MENU_START_BUTTON_WIDTH
			self.start_botton_height 	= const.MENU_START_BUTTON_HEIGHT
			self.start_botton_color  	= white
			self.start_botton_text   	= "Start"
			self.start_botton_font   	= const.MENU_START_BUTTON_FONT
			self.start_botton_font_size = const.MENU_START_BUTTON_SIZE
			self.start_type             = 'start'
		
		elif start_type == const.GAME_PAUSE:
			print("start_type = GAME_PAUSE")
			self.start_botton_x 	 	= const.GAME_PAUSE_CONTINUE_BUTTON_X
			self.start_botton_y 	 	= const.GAME_PAUSE_CONTINUE_BUTTON_Y
			self.start_botton_width  	= const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH
			self.start_botton_height 	= const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT
			self.start_botton_color  	= white
			self.start_botton_text   	= "Continue"
			self.start_botton_font   	= const.GAME_PAUSE_CONTINUE_BUTTON_FONT
			self.start_botton_font_size = const.GAME_PAUSE_CONTINUE_BUTTON_SIZE
			self.start_type             = 'start'

		elif start_type == const.OTHER:
			print("start_type = CUSTOM")
			self.start_botton_x 	 	= x
			self.start_botton_y 	 	= y
			self.start_botton_width  	= width
			self.start_botton_height 	= height
			self.start_botton_color  	= color
			self.start_botton_text   	= text
			self.start_botton_font   	= font
			self.start_botton_font_size = size
			self.type                   = 'start'

		else:
			self.start_type                   = None
			print("pass")
			pass

	def set_quit_botton(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, back_type=0):
		if back_type == const.MENU:
			print("back_type = MENU")
			self.back_botton_x         = const.MENU_QUIT_BUTTON_X
			self.back_botton_y         = const.MENU_QUIT_BUTTON_Y
			self.back_botton_width     = const.MENU_QUIT_BUTTON_WIDTH
			self.back_botton_height    = const.MENU_QUIT_BUTTON_HEIGHT
			self.back_botton_color     = white
			self.back_botton_text      = "Quit"
			self.back_botton_font      = const.MENU_QUIT_BUTTON_FONT
			self.back_botton_font_size = const.MENU_QUIT_BUTTON_SIZE
			self.back_type            = 'back'

		elif back_type == const.INFO:
			print("back_type = INFO")
			self.back_botton_x         = const.INFO_BACK_BUTTON_X
			self.back_botton_y         = const.INFO_BACK_BUTTON_Y
			self.back_botton_width     = const.INFO_BACK_BUTTON_WIDTH
			self.back_botton_height    = const.INFO_BACK_BUTTON_HEIGHT
			self.back_botton_color     = white
			self.back_botton_text      = "MENU"
			self.back_botton_font      = const.INFO_BACK_BUTTON_FONT
			self.back_botton_font_size = const.INFO_BACK_BUTTON_SIZE
			self.back_type             = 'back'
		
		elif back_type == const.GAME_PAUSE:
			print("back_type = GAME_PAUSE")
			self.back_botton_x         = const.GAME_PAUSE_LEFT_BUTTON_X
			self.back_botton_y         = const.GAME_PAUSE_LEFT_BUTTON_Y
			self.back_botton_width     = const.GAME_PAUSE_LEFT_BUTTON_WIDTH
			self.back_botton_height    = const.GAME_PAUSE_LEFT_BUTTON_HEIGHT
			self.back_botton_color     = white
			self.back_botton_text      = "MENU"
			self.back_botton_font      = const.GAME_PAUSE_LEFT_BUTTON_FONT
			self.back_botton_font_size = const.GAME_PAUSE_LEFT_BUTTON_SIZE
			self.back_type             = 'back'

		elif back_type == const.OTHER:
			print("back_type = CUSTOM")
			self.back_botton_x         = x
			self.back_botton_y         = y
			self.back_botton_width     = width
			self.back_botton_height    = height
			self.back_botton_color     = color
			self.back_botton_text      = text
			self.back_botton_font      = font
			self.back_botton_font_size = size
			self.back_type             = 'back'
		
		else:
			self.back_type             = None
			pass
