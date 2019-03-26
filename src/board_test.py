from test_level import *
from test_Board import *
from chess import *
from interface import *
from Declaration import *

py.init()


while const.GAME_LOOP:

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		test_b.event_handle(event)

	display.fill(white)

	test_level_run()


	py.display.update()
	clock.tick(60)
