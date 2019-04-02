from Declaration import *

class CharactorImage():

	def __init__(self):
		self.img  = None
		self.name = None

	def loadUI(self, file, name):
		if name != None:
			self.img = py.image.load(const.PATH+file+name+'.png').convert()
			self.name = name
			print("charactor {} loaded".format(name))
			self.resize(250, 400)
			self.img.set_colorkey(self.img.get_at((0,0)), py.RLEACCEL)

	def resize(self, width, height):
		if self.img != None:
			self.img = py.transform.scale(self.img, (width, height))
		else:
			print("img is not exist")

	def draw(self, display, pos, talking=True):
		tmp = self.img
		if talking:
			display.blit(tmp, pos)
		else:
			tmp.set_alpha(128)
			display.blit(tmp, pos)


	def getImg(self):
		print(index)
		return self.img

	def getName(self):
		return self.name