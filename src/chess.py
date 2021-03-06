import const
from block_center import *
from Declaration import *

const.OBSTACLE  = 1
const.SOLDIER   = 2
const.ENEMY     = 3

const.SERVANT   = 1
const.COMMANDER = 2
const.KING      = 3

chess_image = Image()
def load_chess():
	chess_image.loadUI(const.UIFILE,'soldier_servant.jpg')
	chess_image.loadUI(const.UIFILE,'soldier_commander.jpg')
	chess_image.loadUI(const.UIFILE,'soldier_king.jpg')
	chess_image.loadUI(const.UIFILE,'enemy_servant.jpg')
	chess_image.loadUI(const.UIFILE,'enemy_commander.jpg')
	chess_image.loadUI(const.UIFILE,'enemy_king.jpg')
	for i in range(1,7):
		chess_image.resize(60,60,i)

load_chess()

class chess() :

	def __init__(self,x,y,camp,rank=0) :
		if is_board[x][y] == 0 :
			self.x         = x
			self.y         = y
			self.camp      = camp
			self.rank      = rank
			self.order     = None
			self.move      = False
			self.life      = True
			is_board[x][y] = camp
		else :
			self.life      = False

	def get_move(self) :
		if self.life == False :
			return False
		return self.move

	def draw(self, board, class_interface) :
		if self.life == False :
			return
		if self.camp == const.OBSTACLE :
			class_interface.block(board,board_x[self.x][self.y],board_y[self.x][self.y],60,cyan_blue)
		elif self.camp == const.SOLDIER :
			if self.rank == const.SERVANT :
				chess_image.PrintImg(board,1,board_x[self.x][self.y]-30,board_y[self.x][self.y]-30)
			if self.rank == const.COMMANDER :
				chess_image.PrintImg(board,2,board_x[self.x][self.y]-30,board_y[self.x][self.y]-30)
			if self.rank == const.KING :
				chess_image.PrintImg(board,3,board_x[self.x][self.y]-30,board_y[self.x][self.y]-30)
		elif self.camp == const.ENEMY :
			if self.rank == const.SERVANT :
				chess_image.PrintImg(board,4,board_x[self.x][self.y]-30,board_y[self.x][self.y]-30)
			if self.rank == const.COMMANDER :
				chess_image.PrintImg(board,5,board_x[self.x][self.y]-30,board_y[self.x][self.y]-30)
			if self.rank == const.KING :
				chess_image.PrintImg(board,6,board_x[self.x][self.y]-30,board_y[self.x][self.y]-30)

		# textFont       = py.font.Font(const.PATH+const.FONTFILE+"Regular.ttf", 25)
		# textSurface    = textFont.render(str(self.rank), True, black)
		# textRec        = textSurface.get_rect()
		# textRec.center = (board_x[self.x][self.y],board_y[self.x][self.y])
		# board.blit(textSurface, textRec)


	def whoami(self,x,y):
		if self.x == x and self.y == y :
			return self.camp
		return None
	
	def check(self, mode) :
		if self.life == False :
			return
		if mode == 0 :
			if self.x < 7 and is_board[self.x+1][self.y] == 0 :
				self.move = True
			else :
				self.move = False
		if mode == 1 :
			if self.y < 7 and is_board[self.x][self.y+1] == 0 :
				self.move = True
			else :
				self.move = False
		if mode == 2 :
			if self.x > 0 and is_board[self.x-1][self.y] == 0 :
				self.move = True
			else :
				self.move = False
		if mode == 3 :
			if self.y > 0 and is_board[self.x][self.y-1] == 0 :
				self.move = True
			else :
				self.move = False

	def down(self, mode,action) :
		if self.life == False :
			return
		if self.move and action :
			if self.camp == const.SOLDIER or self.camp == const.ENEMY :
				if mode == 0 :
					if self.x < 7 and is_board[self.x+1][self.y] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x+1][self.y] = self.camp
						self.x += 1
				if mode == 1 :
					if self.y < 7 and is_board[self.x][self.y+1] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x][self.y+1] = self.camp
						self.y += 1
				if mode == 2 :
					if self.x > 0 and is_board[self.x-1][self.y] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x-1][self.y] = self.camp
						self.x -= 1
				if mode == 3 :
					if self.y > 0 and is_board[self.x][self.y-1] == 0 :
						is_board[self.x][self.y] = 0
						is_board[self.x][self.y-1] = self.camp
						self.y -= 1


	def get_rank(self,x,y) :
		if self.life == False :
			return 0
		if self.x == x and self.y == y :
			return self.rank
		return 0

	def get_life(self) :
		return self.life

	def kill(self,x,y,rank) :
		if self.life == False :
			return False
		if self.x == x and self.y == y and rank >= self.rank :
			is_board[self.x][self.y] = 0
			print('kill: ',x,y,is_board[x][y],self.camp)
			return True
		return False

	def kill_myself(self) :
		if self.life == False :
			return
		is_board[self.x][self.y] = 0

	def defeat(self,spin,mode,move,list_soldier,list_enemy) : # let OBSTACLE be a base
		if self.life == False or move == False :
			return
		rank = 0
		if spin :
			return
		if mode == 0 :
			for i in range(7,0,-1):
				for j in range(0,8):
					if is_board[i][j] == const.SOLDIER and is_board[i-1][j] == const.ENEMY :
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].get_rank(i-1,j) != 0 :
								rank = list_enemy[k].get_rank(i-1,j)
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].kill(i,j,rank) :
								del list_soldier[k]
								break
					if is_board[i][j] == const.ENEMY and is_board[i-1][j] == const.SOLDIER :
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].get_rank(i-1,j) != 0 :
								rank = list_soldier[k].get_rank(i-1,j)
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].kill(i,j,rank) :
								del list_enemy[k]
								break

		if mode == 1 :
			for j in range(7,0,-1):
				for i in range(0,8):
					if is_board[i][j] == const.SOLDIER and is_board[i][j-1] == const.ENEMY :
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].get_rank(i,j-1) != 0 :
								rank = list_enemy[k].get_rank(i,j-1)
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].kill(i,j,rank) :
								del list_soldier[k]
								break
					if is_board[i][j] == const.ENEMY and is_board[i][j-1] == const.SOLDIER :
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].get_rank(i,j-1) != 0 :
								rank = list_soldier[k].get_rank(i,j-1)
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].kill(i,j,rank) :
								del list_enemy[k]
								break

		if mode == 2 :
			for i in range(0,7):
				for j in range(0,8):
					if is_board[i][j] == const.SOLDIER and is_board[i+1][j] == const.ENEMY :
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].get_rank(i+1,j) != 0 :
								rank = list_enemy[k].get_rank(i+1,j)
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].kill(i,j,rank) :
								del list_soldier[k]
								break
					if is_board[i][j] == const.ENEMY and is_board[i+1][j] == const.SOLDIER :
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].get_rank(i+1,j) != 0 :
								rank = list_soldier[k].get_rank(i+1,j)
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].kill(i,j,rank) :
								del list_enemy[k]
								break
		
		if mode == 3 :
			for j in range(0,7):
				for i in range(0,8):
					if is_board[i][j] == const.SOLDIER and is_board[i][j+1] == const.ENEMY :
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].get_rank(i,j+1) != 0 :
								rank = list_enemy[k].get_rank(i,j+1)
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].kill(i,j,rank) :
								del list_soldier[k]
								break
					if is_board[i][j] == const.ENEMY and is_board[i][j+1] == const.SOLDIER :
						for k in range(0,len(list_soldier)) :
							if list_soldier[k].get_rank(i,j+1) != 0 :
								rank = list_soldier[k].get_rank(i,j+1)
						for k in range(0,len(list_enemy)) :
							if list_enemy[k].kill(i,j,rank) :
								del list_enemy[k]
								break

