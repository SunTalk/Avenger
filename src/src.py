from Declaration import *
from soundHandler import SoundHandler
from interface import *
from Image import *

soundHandler = SoundHandler()

menu   = interface()
info   = interface()
game   = interface()
finish = interface()

Font = Font_EN

music = False

def init():

	global GAME_SATE

	load_built_in_UI()

	menu.loadUI(image.getImg(const.MENU))
	info.loadUI(image.getImg(const.INFO))

	menu.set_button(const.MENU)
	menu.set_custom_button(const.MENU_START_BUTTON_X,
						   const.MENU_START_BUTTON_Y+2*const.MENU_START_BUTTON_HEIGHT,
						   const.MENU_START_BUTTON_WIDTH,
						   const.MENU_START_BUTTON_HEIGHT,
						   white,
						   "INFO"
						   )

	info.set_button(const.INFO)

	game.loadUI(image.getImg(const.GAME_PLAY))
	finish.loadUI(image.getImg(const.GAME_FINISH))

	GAME_SATE = const.MENU
	loadMUSIC(const.MUSICNAME[const.MENU])

def clear_screen():
	display.fill(white)

def loadMUSIC(name):

	if music:
		if soundHandler.isPlaying():
			soundHandler.stop()

		soundHandler.loadMUSIC(name)
		py.time.delay(500)

def play_music():
	if music:
		if not soundHandler.isPlaying():
			soundHandler.play()

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

	play_music()
	
	event_judge(menu)
	update(menu)
	if menu.start_is_press():
		print("play game")
		GAME_SATE = const.GAME_PLAY
		menu.clearFlag()
		clear_screen()
		loadMUSIC(const.MUSICNAME[const.STORY])

	elif menu.custom_is_press():
		if menu.get_custom_button_name('INFO'):
			print('INFO')
			GAME_SATE = const.INFO
		menu.clearFlag()
		clear_screen()

	elif menu.back_is_press():
		exit()

def run_info():

	global GAME_SATE

	event_judge(info)
	update(info)
	
	if info.back_is_press():
		GAME_SATE = const.MENU
		info.clearFlag()
		clear_screen()

def run_plot():

	global GAME_SATE

	pass

def run_story():

	global GAME_SATE

	pass

def run_game_play():

	global GAME_SATE

	play_music()

	event_judge(finish)
	update(game)
	clear_screen()


	pass

def run_game_pause():

	global GAME_SATE

	pass

def run_game_finish():

	global GAME_SATE

	event_judge(finish)
	update(finish)
	clear_screen()

	pass


switch = {
	
	const.MENU:
		run_menu,
	const.INFO:
		run_info,
	const.PLOT:
		run_plot,
	const.STORY:
		run_story,
	const.GAME_PLAY:
		run_game_play,
	const.GAME_PAUSE:
		run_game_pause,
	const.GAME_FINISH:
		run_game_finish
}

def game_loop():

	global GAME_SATE

	init()

	while const.GAME_LOOP:
		
		switch.get(GAME_SATE)()


if __name__ == "__main__":
	game_loop()