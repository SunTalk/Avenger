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

## end blitRotate

## board
board = py.Surface((600,600))

def board_build() :
	board.fill(white)
	bound(board)
	for i in range( 0 ,len(obstacle_x) ) :
		block(board,board_x[obstacle_x[i]][obstacle_y[i]],board_y[obstacle_x[i]][obstacle_y[i]],60,cyan_blue)

obstacle_x = []
obstacle_y = []

def add_obstacle(x,y) :
	obstacle_x.append(x)
	obstacle_y.append(y)

def clean_obstacle() :
	obstacle_x.clear()
	obstacle_y.clear()
	board_build()

board_angle = 0
board_change_angle = 0
action = True
board_center_pos = (400,400)

def board_display(surface):
	global board_change_angle
	global board_angle
	global action
	if board_change_angle > 0 :
		board_angle += 2
		board_change_angle -=2
		action = False
	if board_change_angle < 0 :
		board_angle -= 2
		board_change_angle += 2
		action = False
	if board_change_angle == 0 :
		action = True
	board_angle = board_angle % 360

	blitRotate(surface,board,board_center_pos,(300,300),board_angle)

## end board_display

def board_action(event):
	global board_change_angle
	if event.type == py.KEYDOWN:
		if event.key == py.K_RIGHT:
			if action :
				board_change_angle = -90
				print('right')
		if event.key == py.K_LEFT:
			if action :
				board_change_angle = 90
				print('left')
		if event.key == py.K_DOWN :
			clean_obstacle()
			print('down')

## end board_action

## end board

## for test
add_obstacle(B5_x,B5_y)
board_build()
while const.GAME_LOOP:
	
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		board_action(event)

	display.fill(black)
	board_display(display)
	
	py.display.update()
	clock.tick(60)

## end test