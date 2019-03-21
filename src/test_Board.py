from Declaration import *
from board import *

from interface import *

game = interface()

class testBoard():

	def __init__(self):
		self.board 		  = py.Surface((600, 600))
		self.action       = True
		self.move         = False
		self.angle        = 0
		self.change_angle = 0
		self.center_pos   = (400, 400)
		self.mode         = 0

	def __setattr__(self, name, value):
		self.__dict__[name] = value

	def blitRotate(self, surf, image, pos, originPos, angle):

		# calcaulate the axis aligned bounding box of the rotated image
		self.w, self.h    = image.get_size()
		self.box          = [py.math.Vector2(p) for p in [(0, 0), (self.w, 0), (self.w, -self.h), (0, -self.h)]]
		self.box_rotate   = [p.rotate(angle) for p in self.box]
		self.min_box      = (min(self.box_rotate, key=lambda p: p[0])[0], min(self.box_rotate, key=lambda p: p[1])[1])
		self.max_box      = (max(self.box_rotate, key=lambda p: p[0])[0], max(self.box_rotate, key=lambda p: p[1])[1])
		
        # calculate the translation of the pivot 
		self.pivot        = py.math.Vector2(originPos[0], -originPos[1])
		self.pivot_rotate = self.pivot.rotate(angle)
		self.pivot_move   = self.pivot_rotate - self.pivot

		# calculate the upper left origin of the rotated image
		self.origin = (pos[0] - originPos[0] + self.min_box[0] - self.pivot_move[0], pos[1] - originPos[1] - self.max_box[1] + self.pivot_move[1])

		# get a rotated image
		self.rotated_image = py.transform.rotate(image, angle)

		# rotate and blit the image
		surf.blit(self.rotated_image, self.origin)

	def build(self, class_interface) :
		self.board.fill(white)
		class_interface.bound(self.board)

	def display(self, surface):
		if self.change_angle > 0:
			self.angle        += 2
			self.change_angle -=2
		if self.change_angle < 0:
			self.angle        -=2
			self.change_angle +=2
		if self.change_angle == 0:
			self.action = True
		self.angle %= 360

		self.blitRotate(surface, self.board, self.center_pos, (300,300), self.angle)

	def event_handle(self, event):
		if event.type == py.KEYDOWN:
			if event.key == py.K_RIGHT:
				if self.action == True: #and self.move == False :
					self.action = False
					#self.move = True
					self.change_angle = -90
					self.mode += 1
					self.mode = self.mode%4
					print('right')
					# start_move = True
			if event.key == py.K_LEFT:
				if self.action == True:# and self.move == False :
					self.action = False
					#self.move = True
					self.change_angle = 90
					self.mode -= 1
					self.mode = self.mode%4
					print('left')
					# start_move = True
			if event.key == py.K_DOWN :
				print('down')