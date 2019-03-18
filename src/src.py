from Declaration import *
from soundHandler import SoundHandler
from interface import *
from Image import *

test = interface()
testImg = Image()

def game_loop():

	testImg.loadUI(const.UIFILE, "11.png")
	test.loadUI(testImg.getImg())
	test.set_botton(const.INFO)
	while const.GAME_LOOP:
		
		for event in py.event.get():
			if event.type == py.QUIT:
				py.quit()
				quit()

		test.update(True)
		#test.writeText("hi", black, 300, 300, const.MENU_START_BUTTON_FONT, 50)
		py.display.update()


if __name__ == "__main__":
	py.init()
	game_loop()