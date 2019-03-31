from board import *
from chess import *
from interface import *
from Declaration import *

from test_level import *
from level_one import *
from level_two import *
from level_three import *
from level_double import *

py.init()

# test_level_set()
level_one_set()
# level_two_set()
# level_three_set()
# level_double_set()

while const.GAME_LOOP:
	
	if level_one_board.get_reset() :
		level_one_set()
	# if level_two_board.get_reset() :
	# 	level_two_set()
	# if level_three_board.get_reset() :
		# level_three_set()
	# if test_b.get_reset() :
		# test_level_set()
	# if level_double_board.get_reset() :
	# 	level_double_set()

	# if level_double_board.random_count() :
	# 	random_obstacle()

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		# test_b.event_handle(event)
		level_one_board.event_handle(event)
		# level_two_board.event_handle(event)
		# level_three_board.event_handle(event)
		# level_double_board.event_handle_two_player_mode(event)


	display.fill(white)

	# test_level_run()
	level_one_run()
	# level_two_run()
	# level_three_run()
	# level_double_run()

	print(level_one_board.get_move())

	# if level_one_WorL() != 0 :
	# 	level_one_board.end_level()

	py.display.update()
	clock.tick(60)
