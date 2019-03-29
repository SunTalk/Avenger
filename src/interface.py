from Declaration import *
from block_center import *
class interface():

	def __init__(self):
		self.textFont     = None
		self.textSurface  = None
		self.textRec      = None
		self.start_type   = None
		self.back_type    = None
		self.custom_type  = None
		self.press_start  = False
		self.press_back   = False
		self.init_custom_button()
		self.custom_index = 0
		self.draw_white   = False
		
	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def init_custom_button(self):
		self.custom_button_x         = list()
		self.custom_button_y         = list()
		self.custom_button_width     = list()
		self.custom_button_height    = list()
		self.custom_button_color     = list()
		self.custom_button_text      = list()
		self.custom_button_font      = list()
		self.custom_button_font_size = list()
		self.custom_text_color       = list()
		self.press_custom            = list()

	def block(self, surface, center_x, center_y, size, color):
		py.draw.rect(surface,color,[center_x-size/2,center_y-size/2,size,size])
		py.draw.rect(surface,black,[center_x-size/2,center_y-size/2,size,size],3)

	def bound(self, surface):
		for i in range(0,36):
			self.block(surface,boundary_x[i],boundary_y[i],60,cyan_blue)
		for i in (90,150,210,270,330,390,450,510):
			for j in (90,150,210,270,330,390,450,510):
				self.block(surface,i,j,60,white)

	def loadUI(self, img):
		if img == None:
			self.draw_white = True
		else:
			self.backgroundImg = img
			print("img set")

	def update(self):
		self.draw()

		if self.textSurface != None:
			self.writeMSG()

		# drawbutton:
		self.draw_button()

	def draw(self):
		if not self.draw_white:
			display.blit(self.backgroundImg, (0, 0))
		else:
			display.fill(white)

	def draw_button(self):
		if self.start_type != None:
			self.draw_start_button()
			self.write()
		
		if self.back_type != None:
			self.draw_back_button()
			self.write()

		if self.custom_type != None:
			for i in range(0, self.custom_index):
				self.draw_bt(self.custom_button_color[i], self.custom_button_x[i], self.custom_button_y[i], self.custom_button_width[i], self.custom_button_height[i])
				self.write(self.custom_text_color[i])

	def draw_start_button(self):
		py.draw.rect(display, self.start_button_color, [self.start_button_x, self.start_button_y, self.start_button_width, self.start_button_height])

	def draw_back_button(self):
		py.draw.rect(display, self.back_button_color, [self.back_button_x, self.back_button_y, self.back_button_width, self.back_button_height])

	def draw_bt(self, color, x, y, width, height):
		py.draw.rect(display, color, [x, y, width, height])

	# def writeMSG(self):
	# 	display.blit(self.textSurface, self.textRec)

	# def writeText(self, text, center_x, center_y, font, color=(255, 0, 0),size=50):
	# 	self.textFont       = py.font.Font(const.PATH+const.FONTFILE+font, size)
	# 	self.textSurface    = self.textFont.render(text, True, color)
	# 	self.textRec        = self.textSurface.get_rect()
	# 	self.textRec.center = (center_x, center_y)

	def write(self, color=(0, 0, 0)):
		if self.start_type == 'start':
			self.message(self.start_button_text, self.start_button_font, self.start_button_font_size)
			display.blit(self.textSurface_st, self.textRec_st)
		
		if self.back_type == 'back':
			self.message(self.back_button_text, self.back_button_font, self.back_button_font_size)
			display.blit(self.textSurface_bc, self.textRec_bc)

		if self.custom_type != None:
			for i in range(0, self.custom_index):
				self.message(self.custom_button_text[i], self.custom_button_font[i], self.custom_button_font_size[i], color, i)
				display.blit(self.textSurface_ct, self.textRec_ct)

	def message(self, text, font, size, color=(0,0,0), index=0):

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

		if self.custom_type != None:
			self.textSurface_ct    = self.textFont.render(text, True, color)
			self.textRec_ct        = self.textSurface_ct.get_rect()
			self.textRec_ct.center = ((self.custom_button_x[index]+(self.custom_button_width[index]/2), (self.custom_button_y[index]+(self.custom_button_height[index]/2))))
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

		if self.custom_type != None:
			for i in range(0, self.custom_index):
				if (py.mouse.get_pos()[0] > self.custom_button_x[i]) and (py.mouse.get_pos()[0] < (self.custom_button_x[i]+self.custom_button_width[i])):
					if (py.mouse.get_pos()[1] > self.custom_button_y[i]) and (py.mouse.get_pos()[1] <= (self.custom_button_y[i]+self.custom_button_height[i])):
						self.custom_button_color[i] = gray
						if event.type == py.MOUSEBUTTONDOWN:
							self.press_custom[i] = True
							print("{} pressed".format(self.custom_button_text[i]))
					else:
						self.custom_button_color[i] = white
						self.press_custom[i] = False
				else:
					self.custom_button_color[i] = white
					self.press_custom[i] = False

		# if event.type == py.KEYDOWN:

	def set_button(self, type):
		self.set_start_button(start_type=type)
		self.set_quit_button(back_type=type)

	def set_custom_button(self, x, y, width, height, color, text, font=Font_EN, size=50, textColor=red):
		print("set custom button")
		self.custom_button_x.append(x)
		self.custom_button_y.append(y)
		self.custom_button_width.append(width)
		self.custom_button_height.append(height)
		self.custom_button_color.append(color)
		self.custom_button_text.append(text)
		self.custom_button_font.append(font)
		self.custom_button_font_size.append(size)
		self.custom_text_color.append(textColor)
		self.press_custom.append(False)
		self.custom_type = 'custom'
		self.custom_index += 1

	def set_start_button(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, size=0,start_type=0):
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

	def set_quit_button(self, x=0, y=0, width=0, height=0, color=0, text=None, font=None, size=0, back_type=0):
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
			self.back_type             = 'back'

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
	def get_custom_button_name(self, name):
		for i in range(0, self.custom_index):
			if self.custom_button_text[i] == name and self.press_custom[i]:
				return True

	def start_is_press(self):
		return self.press_start
	def back_is_press(self):
		return self.press_back
	def custom_is_press(self):
		if self.custom_type != None:
			for i in range(0, self.custom_index):
				if self.press_custom[i]:
					return self.press_custom[i]
	def clearFlag(self):
		self.press_start  = False
		self.press_back   = False
		for i in range(0, self.custom_index):
			self.press_custom[i] = False