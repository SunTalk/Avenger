from Declaration import *
from soundHandler import SoundHandler
from interface import *
from Image import *
from textHandler import *

soundHandler = SoundHandler()

menu   = interface()
info   = interface()
game   = interface()
finish = interface()

testText = textHandler()

music = False

def event_judge(class_object):
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		#class_object.event_handle(event)

def update(class_object):
	class_object.update()
	testText.write()
	py.display.update()


def main():

	load_built_in_UI()
	menu.loadUI(image.getImg(const.MENU))
	#info.loadUI(image.getImg(const.INFO))

	#menu.set_button(const.MENU)
	# menu.set_custom_button(const.MENU_START_BUTTON_X,
	# 					   const.MENU_START_BUTTON_Y+2*const.MENU_START_BUTTON_HEIGHT,
	# 					   const.MENU_START_BUTTON_WIDTH,
	# 					   const.MENU_START_BUTTON_HEIGHT,
	# 					   white,
	# 					   "INFO"
	# 					   )

	# info.set_button(const.INFO)

	# game.loadUI(image.getImg(const.GAME_PLAY))
	# finish.loadUI(image.getImg(const.GAME_FINISH))
	testText.setText("fuck", 100, 100)
	testText.setText("Hello", 500, 500)
	testText.printf()
	#loadMUSIC(const.MUSICNAME[const.MENU])

	while 1:

		event_judge(menu)


		update(menu)



if __name__ == "__main__":
	main()