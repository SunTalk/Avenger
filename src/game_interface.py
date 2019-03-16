from Declaration import *

py.init()

def block(center_x,center_y,size,color):
	py.draw.rect(display,color,[center_x-size/2,center_y-size/2,size,size])
	py.draw.rect(display,black,[center_x-size/2,center_y-size/2,size,size],3)

def bound():
	for i in range(0,36):
		block(boundary_x[i],boundary_y[i],60,cyan_blue)
	# block(400,400,600,cyan_blue)
	# block(400,400,480,white)


while const.GAME_LOOP:
	
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()

	display.fill(white)
	bound()
	block(B5_x,B5_y,60,red)

	py.display.update()
	clock.tick(60)