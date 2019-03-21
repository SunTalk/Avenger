from board import *
from test_Board import *
from chess import *
from interface import *

game = interface()

py.init()

# add_obstacle(A6_x,A6_y)
# add_obstacle(B5_x,B5_y)
# add_obstacle(C2_x,C2_y)
# add_obstacle(C4_x,C4_y)
# add_obstacle(F7_x,F7_y)
# add_obstacle(G5_x,G5_y)
# add_obstacle(H4_x,H4_y)

# add_solider(A1_x,A1_y)
# add_solider(B3_x,B3_y)

# add_enemy(D1_x,D1_y)
# add_enemy(D2_x,D2_y)
# add_enemy(E3_x,E3_y)
# add_enemy(E4_x,E4_y)
# add_enemy(D5_x,D5_y)
# add_enemy(D6_x,D6_y)
# add_enemy(A7_x,A7_y)
# add_enemy(A8_x,A8_y)
# add_enemy(E5_x,E5_y)

test_r = chess(D3_x,D3_y,'solider')
test_b = testBoard()

test_b.build(game)

while const.GAME_LOOP:

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		test_b.event_handle(event)

	display.fill(white)
	test_b.display(display)

	# solider_down()
	# enemy_down()
	# defeat()
	# move_checker()
	test_b.build(game)

## ----
	
	test_r.draw(test_b.board, game)
	test_r.down()
	test_r.check()

## ---


	py.display.update()
	clock.tick(60)
