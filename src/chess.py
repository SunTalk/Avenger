import const
from board import *

const.OBSTACLE = 1
const.SOLDIER  = 2
const.ENEMY    = 3

class chess() :

	def __init__(self,x,y,camp) :
		if is_board[x][y] == 0 :
			self.x = x
			self.y = y
			self.camp = camp
			self.order = None
			self.move = False
			is_board[x][y] = camp

	def get_move(self) :
		return self.move

	def draw(self) :
		if self.camp == const.OBSTACLE :
			block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,cyan_blue)
		elif self.camp == const.SOLDIER :
			block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,red)
		elif self.camp == const.ENEMY :
			block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,green)

	def whoami(self,x,y):
		if self.x == x and self.y == y :
			return self.camp
		return None
	
	def check(self) :
		if board_mode == 0 :
			if self.x < 7 and is_board[self.x+1][self.y] == 0 :
				self.move = True
			else :
				self.move = False
		if board_mode == 1 :
			if self.y < 7 and is_board[self.x][self.y+1] == 0 :
				self.move = True
			else :
				self.move = False
		if board_mode == 2 :
			if self.x > 0 and is_board[self.x-1][self.y] == 0 :
				self.move = True
			else :
				self.move = False
		if board_mode == 3 :
			if self.y > 0 and is_board[self.x][self.y-1] == 0 :
				self.move = True
			else :
				self.move = False

	def down(self) :
		if self.move :
			if self.camp == const.SOLDIER or self.camp == const.ENEMY :
				if board_mode == 0 :
					if self.x < 7 and is_board[self.x+1][self.y] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x+1][self.y] = self.camp
						self.x += 1
				if board_mode == 1 :
					if self.y < 7 and is_board[self.x][self.y+1] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x][self.y+1] = self.camp
						self.y += 1
				if board_mode == 2 :
					if self.x > 0 and is_board[self.x-1][self.y] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x-1][self.y] = self.camp
						self.x -= 1
				if board_mode == 3 :
					if self.y > 0 and is_board[self.x][self.y-1] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x][self.y-1] = self.camp
						self.y -= 1


	def kill(self,x,y) :
		if self.x == x and self.y == y :
			is_board[self.x][self.y] = 0
			return 'kill'
		return None

### end class chess

# def delete_chess(x,y) :
# 	for i in range()


def defeat_class(list_soldier,list_enemy):
	if board_mode == 0 :
		for i in range(7,0,-1):
			for j in range(0,8):
				if is_board[i][j] == 2 and is_board[i-1][j] == 3 :
					kill(i,j)
				if is_board[i][j] == 3 and is_board[i-1][j] == 2 :
					kill(i-1,j)

	if board_mode == 1 :
		for j in range(7,0,-1):
			for i in range(0,8):
				if is_board[i][j] == 2 and is_board[i][j-1] == 3 :
					kill(i,j)
				if is_board[i][j] == 3 and is_board[i][j-1] == 2 :
					kill(i,j-1)

	if board_mode == 2 :
		for i in range(0,7):
			for j in range(0,8):
				if is_board[i][j] == 2 and is_board[i+1][j] == 3 :
					kill(i,j)
				if is_board[i][j] == 3 and is_board[i+1][j] == 2 :
					kill(i+1,j)
	
	if board_mode == 3 :
		for j in range(0,7):
			for i in range(0,8):
				if is_board[i][j] == 2 and is_board[i][j+1] == 3 :
					kill(i,j)
				if is_board[i][j] == 3 and is_board[i][j+1] == 2 :
					kill(i,j+1)