from Declaration import *

def block(where,center_x,center_y,size,color):
	py.draw.rect(where,color,[center_x-size/2,center_y-size/2,size,size])
	py.draw.rect(where,black,[center_x-size/2,center_y-size/2,size,size],3)

def bound(where):
	for i in range(0,36):
		block(where,boundary_x[i],boundary_y[i],60,cyan_blue)
	for i in (90,150,210,270,330,390,450,510):
		for j in (90,150,210,270,330,390,450,510):
			block(where,i,j,60,white)
	# block(400,400,600,cyan_blue)
	# block(400,400,480,white)

def blitRotate(surf, image, pos, originPos, angle):

	# calcaulate the axis aligned bounding box of the rotated image
	w, h       = image.get_size()
	box        = [py.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
	box_rotate = [p.rotate(angle) for p in box]
	min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
	max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

	# calculate the translation of the pivot 
	pivot        = py.math.Vector2(originPos[0], -originPos[1])
	pivot_rotate = pivot.rotate(angle)
	pivot_move   = pivot_rotate - pivot

	# calculate the upper left origin of the rotated image
	origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

	# get a rotated image
	rotated_image = py.transform.rotate(image, angle)

	# rotate and blit the image
	surf.blit(rotated_image, origin)
	# py.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()))

## end blitRotate

## board
board = py.Surface((600,600))

def board_build() :
	board.fill(white)
	bound(board)
	for i in range( 0 ,len(obstacle_x) ) :
		block(board,board_x[obstacle_x[i]][obstacle_y[i]],board_y[obstacle_x[i]][obstacle_y[i]],60,cyan_blue)
	for i in range( 0 ,len(solider_x) ) :
		block(board,board_x[solider_x[i]][solider_y[i]],board_y[solider_x[i]][solider_y[i]],60,red)
	for i in range( 0 ,len(enemy_x) ) :
		block(board,board_x[enemy_x[i]][enemy_y[i]],board_y[enemy_x[i]][enemy_y[i]],60,green)

board_angle = 0
board_change_angle = 0
action = True
board_center_pos = (400,400)
board_mode = 0

def board_display(surface):
	global board_change_angle
	global board_angle
	global action
	global move
	if board_change_angle > 0 :
		board_angle += 2
		board_change_angle -=2
	if board_change_angle < 0 :
		board_angle -= 2
		board_change_angle += 2
	if board_change_angle == 0 :
		action = True
	board_angle = board_angle % 360

	blitRotate(surface,board,board_center_pos,(300,300),board_angle)

## end board_display

def board_action(event):
	global board_change_angle
	global board_mode
	global action
	global move

	if event.type == py.KEYDOWN:
		if event.key == py.K_RIGHT:
			if action and move == False :
				action = False
				move = True
				board_change_angle = -90
				board_mode += 1
				board_mode = board_mode%4
				print('right')
		if event.key == py.K_LEFT:
			if action and move == False :
				action = False
				move = True
				board_change_angle = 90
				board_mode -= 1
				board_mode = board_mode%4
				print('left')
		if event.key == py.K_DOWN :
			print('down')
		if event.key == 'q' :
			add_obstacle(B5_x,B5_y)
			add_solider(A1_x,A1_y)
			board_build()

## end board_action

## end board

## chess

obstacle_x = []
obstacle_y = []

def add_obstacle(x,y) :
	obstacle_x.append(x)
	obstacle_y.append(y)
	is_board[x][y] = 1

def clear_obstacle() :
	for i in range(0,len(obstacle_x)) :
		is_board[obstacle_x[i]][obstacle_y[i]] = 0
	obstacle_x.clear()
	obstacle_y.clear()
	board_build()

solider_x = []
solider_y = []

def add_solider(x,y) :
	if is_board[x][y] == 0:
		is_board[x][y] = 1
		solider_x.append(x)
		solider_y.append(y)

def clear_solider() :
	for i in range(0,len(solider_x)) :
		is_board[solider_x[i]][solider_y[i]] = 0
	solider_x.clear()
	solider_y.clear()
	board_build()

move = False
def solider_down() :
	if action and move :
		for i in range(0,len(solider_x)) :
			if board_mode == 0 :
				if solider_x[i] < 7 and is_board[solider_x[i]+1][solider_y[i]] == 0 :
					is_board[solider_x[i]][solider_y[i]] = 0
					is_board[solider_x[i]+1][solider_y[i]] = 1
					solider_x[i] += 1	
			if board_mode == 1 :
				if solider_y[i] < 7 and is_board[solider_x[i]][solider_y[i]+1] == 0 :
					is_board[solider_x[i]][solider_y[i]] = 0
					is_board[solider_x[i]][solider_y[i]+1] = 1
					solider_y[i] += 1
			if board_mode == 2 :
				if solider_x[i] > 0 and is_board[solider_x[i]-1][solider_y[i]] == 0 :
					is_board[solider_x[i]][solider_y[i]] = 0
					is_board[solider_x[i]-1][solider_y[i]] = 1
					solider_x[i] -= 1
			if board_mode == 3 :
				if solider_y[i] > 0 and is_board[solider_x[i]][solider_y[i]-1] == 0 :
					is_board[solider_x[i]][solider_y[i]] = 0
					is_board[solider_x[i]][solider_y[i]-1] = 1
					solider_y[i] -= 1

## end solider down

enemy_x = []
enemy_y = []

def add_enemy(x,y) :
	if is_board[x][y] == 0:
		is_board[x][y] = 1
		enemy_x.append(x)
		enemy_y.append(y)

def clear_enemy() :
	for i in range(0,len(enemy_x)) :
		is_board[enemy_x[i]][enemy_y[i]] = 0
	enemy_x.clear()
	enemy_y.clear()
	board_build()

move = False
def enemy_down() :
	if action and move :
		for i in range(0,len(enemy_x)) :
			if board_mode == 0 :
				if enemy_x[i] < 7 and is_board[enemy_x[i]+1][enemy_y[i]] == 0 :
					is_board[enemy_x[i]][enemy_y[i]] = 0
					is_board[enemy_x[i]+1][enemy_y[i]] = 1
					enemy_x[i] += 1	
			if board_mode == 1 :
				if enemy_y[i] < 7 and is_board[enemy_x[i]][enemy_y[i]+1] == 0 :
					is_board[enemy_x[i]][enemy_y[i]] = 0
					is_board[enemy_x[i]][enemy_y[i]+1] = 1
					enemy_y[i] += 1
			if board_mode == 2 :
				if enemy_x[i] > 0 and is_board[enemy_x[i]-1][enemy_y[i]] == 0 :
					is_board[enemy_x[i]][enemy_y[i]] = 0
					is_board[enemy_x[i]-1][enemy_y[i]] = 1
					enemy_x[i] -= 1
			if board_mode == 3 :
				if enemy_y[i] > 0 and is_board[enemy_x[i]][enemy_y[i]-1] == 0 :
					is_board[enemy_x[i]][enemy_y[i]] = 0
					is_board[enemy_x[i]][enemy_y[i]-1] = 1
					enemy_y[i] -= 1

## end enemy down

def move_checker():
	global move
	check_move = False
	for i in range(0,len(solider_x)) :
		if board_mode == 0 :
			if solider_x[i] < 7 and is_board[solider_x[i]+1][solider_y[i]] == 0 :
				check_move = True
		if board_mode == 1 :
			if solider_y[i] < 7 and is_board[solider_x[i]][solider_y[i]+1] == 0 :
				check_move = True
		if board_mode == 2 :
			if solider_x[i] > 0 and is_board[solider_x[i]-1][solider_y[i]] == 0 :
				check_move = True
		if board_mode == 3 :
			if solider_y[i] > 0 and is_board[solider_x[i]][solider_y[i]-1] == 0 :
				check_move = True
	for i in range(0,len(enemy_x)) :
		if board_mode == 0 :
			if enemy_x[i] < 7 and is_board[enemy_x[i]+1][enemy_y[i]] == 0 :
				check_move = True
		if board_mode == 1 :
			if enemy_y[i] < 7 and is_board[enemy_x[i]][enemy_y[i]+1] == 0 :
				check_move = True
		if board_mode == 2 :
			if enemy_x[i] > 0 and is_board[enemy_x[i]-1][enemy_y[i]] == 0 :
				check_move = True
		if board_mode == 3 :
			if enemy_y[i] > 0 and is_board[enemy_x[i]][enemy_y[i]-1] == 0 :
				check_move = True
	move = check_move
## end chess

