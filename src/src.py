from Declaration import *
from soundHandler import SoundHandler
from interface import *
from Image import *

image = Image()
menu  = interface()
info  = interface()

def init():

	global GAME_SATE

	image.loadUI(const.UIFILE, "11.png")
	menu.loadUI(image.getImg())
	menu.set_button(const.MENU)
	image.loadUI(const.UIFILE, "INFO.jpg")
	info.loadUI(image.getImg())
	info.set_button(const.INFO)


	GAME_SATE = const.MENU

def clear_screen():
	display.fill(white)

def event_judge(class_object):
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		class_object.event_handle(event)

def update(class_object):
	class_object.update()
	py.display.update()

def run_menu():

	global GAME_SATE

	event_judge(menu)
	update(menu)
	print("run menu")
	if menu.start_is_press():
		GAME_SATE = const.INFO
		menu.clearFlag()
		clear_screen()
	elif menu.back_is_press():
		exit()

def run_info():

	global GAME_SATE

	event_judge(info)
	update(info)
	print("run info")
	if info.back_is_press():
		GAME_SATE = const.MENU
		info.clearFlag()
		clear_screen()


switch = {
	
	const.MENU:
		run_menu,
	const.INFO:
		run_info,
}

def game_loop():

	global GAME_SATE

	init()

	while const.GAME_LOOP:
		
		switch.get(GAME_SATE)()


if __name__ == "__main__":
	py.init()
	game_loop()