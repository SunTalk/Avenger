from Declaration import *

class interface():

	def __init__(self):
		self.textFont    = None
		self.textSurface = None
		self.textRec     = None
		self.start_type  = None
		self.back_type   = None
		self.other_type  = None
		self.press_start = False
		self.press_back  = False
		
	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def loadUI(self, img):
		self.backgroundImg = img
		print("img set")

	def update(self):
		self.draw()

		if self.textSurface != None:
			self.writeMSG()

		# drawbutton:
		self.draw_button()

	def draw(self):
		display.blit(self.backgroundImg, (0, 0))

	def draw_button(self):
		if self.start_type != None:
			self.draw_start_button()
			self.write()
		
		if self.back_type != None:
			self.draw_back_button()
			self.write()

	def draw_start_button(self):
		py.draw.rect(display, self.start_button_color, [self.start_button_x, self.start_button_y, self.start_button_width, self.start_button_height])

	def draw_back_button(self):
		py.draw.rect(display, self.back_button_color, [self.back_button_x, self.back_button_y, self.back_button_width, self.back_button_height])

	def writeMSG(self):
		display.blit(self.textSurface, self.textRec)

	def writeText(self, text, color, center_x, center_y, font, size):
		self.textFont       = py.font.Font(const.PATH+const.FONTFILE+font, size)
		self.textSurface    = self.textFont.render(text, True, color)
		self.textRec        = self.textSurface.get_rect()
		self.textRec.center = (center_x, center_y)

	def write(self):
		if self.start_type == 'start':
			self.message(self.start_button_text, self.start_button_font, self.start_button_font_size)
			display.blit(self.textSurface_st, self.textRec_st)
		
		if self.back_type == 'back':
			self.message(self.back_button_text, self.back_button_font, self.back_button_font_size)
			display.blit(self.textSurface_bc, self.textRec_bc)

	def message(self, text, font, size):
		self.textFont = py.font.Font(const.PATH+const.FONTFILE+font, size)
		
		if self.start_type == 'start':
			self.textSurface_st    = self.textFont.render(text, True, red)
			self.textRec_st        = self.textSurface_st.get_rect()
			self.textRec_st.center = ((self.start_button_x+(self.start_button_width/2), (self.start_button_y+(self.start_button_height/2))))
		else:
			pass

		if self.back_type == 'back':
			self.textSurface_bc    = self.textFont.render(text, True, red)
			self.textRec_bc        = self.textSurface_bc.get_rect()
			self.textRec_bc.center = ((self.back_button_x+(self.back_button_width/2), (self.back_button_y+(self.back_button_height/2))))
		else:
			pass

	def event_handle(self, event):
		if self.start_type != None:
			if (py.mouse.get_pos()[0] > self.start_button_x) and (py.mouse.get_pos()[0] < (self.start_button_x+self.start_button_width)):
				if (py.mouse.get_pos()[1] > self.start_button_y) and (py.mouse.get_pos()[1] <= (self.start_button_y+self.start_button_height)):
					self.start_button_color = gray
					if event.type == py.MOUSEBUTTONUP:
						self.press_start = True
						print("start pressed")
				else:
					self.start_button_color = white
					self.press_start = False
			else:
				self.start_button_color = white
				self.press_start = False

		if self.back_type != None:
			if (py.mouse.get_pos()[0] > self.back_button_x) and (py.mouse.get_pos()[0] < (self.back_button_x+self.back_button_width)):
				if (py.mouse.get_pos()[1] > self.back_button_y) and (py.mouse.get_pos()[1] <= (self.back_button_y+self.back_button_height)):
					self.back_button_color = gray
					if event.type == py.MOUSEBUTTONDOWN:
						self.press_back = True
						print("back pressed")
				else:
					self.back_button_color = white
					self.press_back = False
			else:
				self.back_button_color = white
				self.press_back = False

		# if event.type == py.KEYDOWN:

	def set_button(self, type):
		self.set_start_button(start_type=type)
		self.set_quit_button(back_type=type)

	def set_start_button(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, start_type=0):
		if start_type == const.MENU:
			print("start_type = MENU")
			self.start_button_x 	 	= const.MENU_START_BUTTON_X
			self.start_button_y 	 	= const.MENU_START_BUTTON_Y
			self.start_button_width  	= const.MENU_START_BUTTON_WIDTH
			self.start_button_height 	= const.MENU_START_BUTTON_HEIGHT
			self.start_button_color  	= white
			self.start_button_text   	= "Start"
			self.start_button_font   	= const.MENU_START_BUTTON_FONT
			self.start_button_font_size = const.MENU_START_BUTTON_SIZE
			self.start_type             = 'start'
		
		elif start_type == const.GAME_PAUSE:
			print("start_type = GAME_PAUSE")
			self.start_button_x 	 	= const.GAME_PAUSE_CONTINUE_BUTTON_X
			self.start_button_y 	 	= const.GAME_PAUSE_CONTINUE_BUTTON_Y
			self.start_button_width  	= const.GAME_PAUSE_CONTINUE_BUTTON_WIDTH
			self.start_button_height 	= const.GAME_PAUSE_CONTINUE_BUTTON_HEIGHT
			self.start_button_color  	= white
			self.start_button_text   	= "Continue"
			self.start_button_font   	= const.GAME_PAUSE_CONTINUE_BUTTON_FONT
			self.start_button_font_size = const.GAME_PAUSE_CONTINUE_BUTTON_SIZE
			self.start_type             = 'start'

		elif start_type == const.OTHER:
			print("start_type = CUSTOM")
			self.start_button_x 	 	= x
			self.start_button_y 	 	= y
			self.start_button_width  	= width
			self.start_button_height 	= height
			self.start_button_color  	= color
			self.start_button_text   	= text
			self.start_button_font   	= font
			self.start_button_font_size = size
			self.type                   = 'start'

		else:
			self.start_type             = None
			print("pass")
			pass

	def set_quit_button(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, back_type=0):
		if back_type == const.MENU:
			print("back_type = MENU")
			self.back_button_x         = const.MENU_QUIT_BUTTON_X
			self.back_button_y         = const.MENU_QUIT_BUTTON_Y
			self.back_button_width     = const.MENU_QUIT_BUTTON_WIDTH
			self.back_button_height    = const.MENU_QUIT_BUTTON_HEIGHT
			self.back_button_color     = white
			self.back_button_text      = "Quit"
			self.back_button_font      = const.MENU_QUIT_BUTTON_FONT
			self.back_button_font_size = const.MENU_QUIT_BUTTON_SIZE
			self.back_type            = 'back'

		elif back_type == const.INFO:
			print("back_type = INFO")
			self.back_button_x         = const.INFO_BACK_BUTTON_X
			self.back_button_y         = const.INFO_BACK_BUTTON_Y
			self.back_button_width     = const.INFO_BACK_BUTTON_WIDTH
			self.back_button_height    = const.INFO_BACK_BUTTON_HEIGHT
			self.back_button_color     = white
			self.back_button_text      = "MENU"
			self.back_button_font      = const.INFO_BACK_BUTTON_FONT
			self.back_button_font_size = const.INFO_BACK_BUTTON_SIZE
			self.back_type             = 'back'
		
		elif back_type == const.GAME_PAUSE:
			print("back_type = GAME_PAUSE")
			self.back_button_x         = const.GAME_PAUSE_LEFT_BUTTON_X
			self.back_button_y         = const.GAME_PAUSE_LEFT_BUTTON_Y
			self.back_button_width     = const.GAME_PAUSE_LEFT_BUTTON_WIDTH
			self.back_button_height    = const.GAME_PAUSE_LEFT_BUTTON_HEIGHT
			self.back_button_color     = white
			self.back_button_text      = "MENU"
			self.back_button_font      = const.GAME_PAUSE_LEFT_BUTTON_FONT
			self.back_button_font_size = const.GAME_PAUSE_LEFT_BUTTON_SIZE
			self.back_type             = 'back'

		elif back_type == const.OTHER:
			print("back_type = CUSTOM")
			self.back_button_x         = x
			self.back_button_y         = y
			self.back_button_width     = width
			self.back_button_height    = height
			self.back_button_color     = color
			self.back_button_text      = text
			self.back_button_font      = font
			self.back_button_font_size = size
			self.back_type             = 'back'
		
		else:
			self.back_type             = None
			print("pass")
			pass

	def start_is_press(self):
		return self.press_start
	def back_is_press(self):
		return self.press_back
	def clearFlag(self):
		self.press_start = False
		self.press_back  = False