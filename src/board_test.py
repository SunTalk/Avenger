from test_Board import *
from chess import *
from interface import *
from Declaration import *

from test_level import *
from level_one import *
from level_two import *
from level_three import *

py.init()

# test_level_set()
# level_one_set()
level_two_set()
# level_three_set()

while const.GAME_LOOP:
	
	# if level_one_board.get_reset() :
		# level_one_set()
	if level_two_board.get_reset() :
		level_two_set()
	# if level_three_board.get_reset() :
		# level_three_set()
	# if test_b.get_reset() :
		# test_level_set()

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		# test_b.event_handle(event)
		# level_one_board.event_handle(event)
		level_two_board.event_handle(event)
		# level_three_board.event_handle(event)
		# level_two_board.event_handle_two_player_mode(event)


	display.fill(white)

	# test_level_run()
	# level_one_run()
	level_two_run()
	# level_three_run()

	py.display.update()
	clock.tick(60)
