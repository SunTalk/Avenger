from Declaration import *

py.init()

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

board = py.Surface((600,600))
board.fill(white)
bound(board)
box = block(board,B5_x,B5_y,60,red)

while const.GAME_LOOP:
	
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		if event.type == py.KEYDOWN:
			if event.key == py.K_RIGHT:
				board = py.transform.rotate(board,90)
			if event.key == py.K_LEFT:
				board = py.transform.rotate(board,-90)

	display.fill(white)
	display.blit(board,(100,100))

	py.display.update()
	clock.tick(60)