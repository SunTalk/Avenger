from Declaration import *
from soundHandler import SoundHandler
from interface import *

test = interface()

def game_loop():

	test.set_start_botton(start_type = const.GAME_PAUSE)
	test.loadUI(const.PATH, const.UIFILE, "11.png")
	while const.GAME_LOOP:
		
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
				quit()

		test.update(True)


if __name__ == "__main__":
	py.init()
	game_loop()