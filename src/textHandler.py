from Declaration import *

class textHandler:

	def __init__(self):
		self.text        = list()
		self.textSurface = list()
		self.textRec     = list()
		self.index       = 0

	def write(self):

		for i in range(0, self.getIndex()):
			display.blit(self.textSurface[i], self.textRec[i])

	def setText(self, text, center_x, center_y, font='LucidaBrightDemiBold.ttf', color=(255, 0, 0), size=50):
		self.addText(text, center_x, center_y, font, color, size)

	def text_object(self, text, center_x, center_y, font, color, size):
		tmp_textFont   = py.font.Font(const.PATH+const.FONTFILE+font, size)
		tmp_texturface = tmp_textFont.render(text, True, color)
		tmp_Rec = tmp_texturface.get_rect()
		tmp_Rec.center = (center_x, center_y)
		self.textSurface.append(tmp_texturface)
		self.textRec.append(tmp_Rec)
		#print(self.textSurface)

	def getIndex(self):
		return self.index

	def addText(self, text, center_x, center_y, font, color, size):
		self.text.append(text)
		self.text_object(text, center_x, center_y, font, color, size)
		self.addIndex()

	def addIndex(self):
		self.index += 1

	def printf(self):
		print(self.text)
		print(self.textSurface)
		print(self.textRec)

	def clear(self):
		self.text        = list()
		self.textSurface = list()
		self.textRec     = list()
		self.index       = 0