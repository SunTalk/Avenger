# from Declaration import *
from board import *

class chess() :

	def __init__(self,x,y,camp) :
		self.x = x
		self.y = y
		self.camp = camp
		self.order = None

	def draw(self) :
		if self.camp == 'obstacle' :
			block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,cyan_blue)
		elif self.camp == 'solider' :
			block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,red)
		elif self.camp == 'enemy' :
			block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,green)

	def whoami(self,x,y):
		if self.x == x and self.y == y :
			return self.camp
		return None

	def down(self) :
		if action and move :
			if self.camp == 'solider' or self.camp == 'enemy' :
				if board_mode == 0 :
					if self.x < 7 and is_board[self.x+1][self.y] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x+1][self.y] = 1
						self.x += 1
				if board_mode == 1 :
					if self.y < 7 and is_board[self.x][self.y+1] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x][self.y+1] = 1
						self.y += 1
				if board_mode == 2 :
					if self.x > 0 and is_board[self.x-1][self.y] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x-1][self.y] = 1
						self.x -= 1
				if board_mode == 3 :
					if self.y > 0 and is_board[self.x][self.y-1] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x][self.y-1] = 1
						self.y -= 1

	def kill(self,x,y) :
		if self.x == x and self.y == y :
			is_board[self.x][self.y] = 0
			return kill
		return None

	def check(self) :
		global move
		mark = False
		if board_mode == 0 :
			if self.x < 7 and is_board[self.x+1][self.y] == 0 :
				mark = True
		if board_mode == 1 :
			if self.y < 7 and is_board[self.x][self.y+1] == 0 :
				mark = True
		if board_mode == 2 :
			if self.x > 0 and is_board[self.x-1][self.y] == 0 :
				mark = True
		if board_mode == 3 :
			if self.y > 0 and is_board[self.x][self.y-1] == 0 :
				mark = True
		if start_move :
			move = mark

	def print_flag(self) :
		print('in class ---')
		print('action: ',action)
		print('move: ' , move)
		print('in class ---')