from board import *

py.init()

add_obstacle(A6_x,A6_y)
add_obstacle(B5_x,B5_y)
add_obstacle(C2_x,C2_y)
add_obstacle(C4_x,C4_y)
add_obstacle(F7_x,F7_y)
add_obstacle(G5_x,G5_y)
add_obstacle(H4_x,H4_y)

add_solider(A1_x,A1_y)
add_solider(B3_x,B3_y)

add_enemy(D1_x,D1_y)
add_enemy(D2_x,D2_y)
add_enemy(E3_x,E3_y)
add_enemy(E4_x,E4_y)
add_enemy(D5_x,D5_y)
add_enemy(D6_x,D6_y)
add_enemy(A7_x,A7_y)
add_enemy(A8_x,A8_y)
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
	defeat()
	move_checker()
	board_build()
	
	py.display.update()
	clock.tick(60)
