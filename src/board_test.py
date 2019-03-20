from board import *

py.init()

add_obstacle(B5_x,B5_y)
add_obstacle(G5_x,G5_y)
add_obstacle(C2_x,C2_y)
add_obstacle(F7_x,F7_y)
add_obstacle(A8_x,A8_y)

add_solider(A1_x,A1_y)
add_solider(B3_x,B3_y)
add_solider(C8_x,C8_y)

add_enemy(D8_x,D8_y)
add_enemy(E5_x,E5_y)

board_build()
while const.GAME_LOOP:

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		board_action(event)

	display.fill(white)
	board_display(display)

	solider_down()
	enemy_down()
	move_checker()
	board_build()
	
	py.display.update()
	clock.tick(60)
