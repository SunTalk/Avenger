from test_level import *
from test_Board import *
from chess import *
from interface import *
from Declaration import *
from level_one import *

py.init()

# test_level_set()
level_one_set()

while const.GAME_LOOP:
	
	if level_one_board.get_reset() :
		level_one_set()
	# if test_b.get_reset() :
		# test_level_set()

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		# test_b.event_handle(event)
		level_one_board.event_handle(event)


	display.fill(white)

	# test_level_run()
	level_one_run()


	py.display.update()
	clock.tick(60)
