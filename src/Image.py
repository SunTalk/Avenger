from Declaration import *

class Image():

	def __init__(self):
		self.img 	= None
		self.name   = None

	def loadUI(self, file, name):
		if name != None:
			self.img = py.image.load(const.PATH+file+name)
			self.name = name
			print("{} loaded".format(name))
		else:
			print("loaded fail")

	def resize(self, width, height):
		if self.img != None:
			self.img = py.image.scale(self.img, (width, height))
		else:
			print("img is not exist")

	def rotate(self, angle):
		angle = angle % 360
		if self.img != None:
			self.img = py.transform.rotate(self.img, angle)
		else:
			print("img is not exist")

	def getImg(self):
		return self.img

	def getName(self):
		return self.name



