from Declaration import *

class Image():

	def __init__(self):
		self.img 	= list()
		self.name   = list()
		self.img.append('discarded')
		self.name.append('discarded')

	def loadUI(self, file, name):
		if name != None:
			self.img.append(py.image.load(const.PATH+file+name))
			self.name.append(name)
			print("{} loaded".format(name))
		else:
			self.img.append(None)
			self.name.append(None)
			print("loaded nothing")

	def resize(self, width, height, index):
		if self.img[index] != None:
			self.img[index] = py.transform.scale(self.img[index], (width, height))
		else:
			print("img is not exist")

	def rotate(self, angle, index):
		angle = angle % 360
		if self.img[index] != None:
			self.img[index] = py.transform.rotate(self.img, angle)
		else:
			print("img is not exist")

	def getImg(self, index):
		print(index)
		return self.img[index]

	def getName(self, index):
		return self.name[index]

	def PrintImg(self, surface,index,x,y):
		self.img[index].convert()
		surface.blit(self.img[index], (x, y));


