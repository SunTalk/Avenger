from board import *

py.init()

add_obstacle(B5_x,B5_y)
add_solider(A1_x,A1_y)
add_solider(B3_x,B3_y)
board_build()
while const.GAME_LOOP:

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		board_action(event)

	display.fill(black)
	board_display(display)

	solider_down()
	board_build()
	
	py.display.update()
	clock.tick(60)
