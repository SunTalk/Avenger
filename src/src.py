from Declaration import *
from Function_declare import *
from soundHandler import SoundHandler
from interface import *
from Image import *
from test_level import *
from level_one import *
from level_two import *
from level_three import *
from level_double import *
from KeyHandler import *
from PlotDisplay import *

soundHandler = SoundHandler()
plotDisplay  = PlotDisplay()

menu   = interface()
info   = interface()
plot   = interface()
game   = interface()
finish = interface()

Font = Font_EN

music = False

def init():

	global GAME_STATE
	global CHAPTER
	global ACT

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

	plot.set_custom_button(1000, 0, 200, 100, white, "SKIP")

	game.loadUI(image.getImg(const.GAME_PLAY))
	finish.loadUI(image.getImg(const.GAME_FINISH))
	plot.loadUI(None)

	GAME_STATE = const.MENU
	CHAPTER   = const.CHAPTER_1
	ACT       = const.ACT_1
	loadMUSIC(const.MUSICNAME[const.MENU])

def clear(class_object):
	clear_screen()
	class_object.clearFlag()

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
		keyHandler.setKey(event)

def event_judge_game_play(class_object, level_board):
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		class_object.event_handle(event)
		level_board.event_handle(event)

def update(class_object):
	class_object.update()

	if GAME_STATE == const.GAME_PLAY:
		if PLAYING_STATE == const.LEVEL_ONE:
			level_one_run()
		elif PLAYING_STATE == const.LEVEL_TWO:
			level_two_run()
		elif PLAYING_STATE == const.LEVEL_THREE:
			level_three_run()

	py.display.update()
	clock.tick(fps)

def run_menu():

	global GAME_STATE
	global CHAPTER
	global ACT

	play_music()
	
	event_judge(menu)
	update(menu)
	if menu.start_is_press():
		print("play game")
		GAME_STATE = const.PLOT
		# CHAPTER   = const.CHAPTER_1
		# ACT       = const.ACT_1

		clear(menu)
		loadMUSIC(const.MUSICNAME[const.STORY])

	elif menu.custom_is_press():
		if menu.get_custom_button_name('INFO'):
			print('INFO')
			GAME_STATE = const.INFO
		clear(menu)

	elif menu.back_is_press():
		exit()

def run_info():

	global GAME_STATE

	event_judge(info)
	update(info)
	
	if info.back_is_press():
		GAME_STATE = const.MENU
		clear(info)

def run_plot():

	global GAME_STATE
	global PLAYING_STATE
	global WORLD_LINE
	global CHAPTER
	global ACT

	plotDisplay.load_plot(WORLD_LINE, CHAPTER, ACT)

	while True:

		event_judge(plot)
		plotDisplay.plot_display()

		if plotDisplay.isfinish():
			GAME_STATE    = const.GAME_PLAY
			PLAYING_STATE = const.LEVEL_ONE
			clear(plot)
			transitions(const.LEVEL_ONE)
			print(WORLD_LINE+'_'+str(CHAPTER)+'_'+str(ACT))
			break


		if plot.custom_is_press():
			if plot.get_custom_button_name('SKIP'):
				if ACT == const.ACT_1:
					GAME_STATE = const.GAME_PLAY
				
				print('SKIP')
				clear(plot)
				transitions(CHAPTER)
				PLAYING_STATE = CHAPTER
				print(WORLD_LINE+'_'+str(CHAPTER)+'_'+str(ACT))
				print(PLAYING_STATE)
				break
		update(plot)
	#while story is playing
	#if story is finish
		#

	pass

def run_story():

	global GAME_STATE

	pass

def run_game_play():

	global GAME_STATE

	play_music()

	while 1:
		event_judge_game_play(game, level_one_board)

		update(game)

	pass

def run_game_pause():

	global GAME_STATE

	pass

def run_game_finish():

	global GAME_STATE

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

	global GAME_STATE

	init()

	while const.GAME_LOOP:
		
		switch.get(GAME_STATE)()


if __name__ == "__main__":
	game_loop()