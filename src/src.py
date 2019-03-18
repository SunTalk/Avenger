from Declaration import *
from soundHandler import SoundHandler
from interface import *
from Image import *

test = interface()
testImg = Image()

def init():
	testImg.loadUI(const.UIFILE, "11.png")
	test.loadUI(testImg.getImg())
	test.set_botton(const.GAME_PAUSE)

def event_judge():
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()

def update():
	test.update()
	py.display.update()


def game_loop():

	init()

	while const.GAME_LOOP:
		
		event_judge()
		test.writeText("hi", black, 300, 300, const.MENU_START_BUTTON_FONT, 50)
		update()


if __name__ == "__main__":
	py.init()
	game_loop()