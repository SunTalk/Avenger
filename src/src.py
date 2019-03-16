from Declaration import *
from soundHandler import SoundHandler

def game_loop():

	while const.GAME_LOOP:
		
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
				quit()


if __name__ == "__main__":
	py.init()
	game_loop()