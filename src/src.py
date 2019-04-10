from Declaration import *
from Function_declare import *
from soundHandler import SoundHandler
from textHandler import *
from interface import *
from Image import *
from test_level import *
from level_newplayer import *
from level_one import *
from level_two import *
from level_three import *
from level_four import *
from level_double import *
from KeyHandler import *
from PlotDisplay import *
from CharactorImage import *

soundHandler   = SoundHandler()
plotDisplay    = PlotDisplay()
writeText      = textHandler()
win_text    = textHandler()
lose_text   = textHandler()
info_text   = textHandler()
max_move    = textHandler()

menu    = interface()
info    = interface()
plot    = interface()
game    = interface()
finish  = interface()
loading = interface()
double  = interface()

Font = Font_EN

music = True

MAXMOVE = 20
MMOVE   = 20

def initBackground():
	menu.loadUI(image.getImg(const.MENU))
	info.loadUI(image.getImg(const.INFO))
	game.loadUI(image.getImg(const.GAME_PLAY))
	finish.loadUI(image.getImg(const.GAME_FINISH))
	loading.loadUI(image.getImg(const.LOADING))
	plot.loadUI(None)

def initButton():
	menu.set_button(const.MENU)

	menu.set_custom_button(const.MENU_START_BUTTON_X,
						   const.MENU_START_BUTTON_Y+2*const.MENU_START_BUTTON_HEIGHT,
						   const.MENU_START_BUTTON_WIDTH,
						   const.MENU_START_BUTTON_HEIGHT,
						   white,
						   "INFO",
						   128
						   )

	info.set_button(const.INFO)

	plot.set_custom_button(1000, 0, 200, 100, white, "SKIP", 128)
	game.set_custom_button(1000, 300, 200, 100, white, "restart", 128)
	game.set_custom_button(1000, 600, 200, 100, white, "menu", 128)
	finish.set_custom_button(500, 550, 200, 100, white, "Menu", 128)

def clear_WORLD():
	global WORLD_LINE
	global CHAPTER
	global ACT

	WORLD_LINE = 'N'
	CHAPTER   = const.CHAPTER_1
	ACT       = const.ACT_1

def init():

	global WORLD_LINE
	global GAME_STATE
	global NEXT_STATE
	global CHAPTER
	global ACT

	load_built_in_UI()
	initBackground()
	initButton()

	win_text.setText("You Win", 600, 200, size=100)
	win_text.setText("Press enter to continue", 600, 480, size=100)

	lose_text.setText("You Lose", 600, 200, size=100)
	lose_text.setText("Press enter to continue", 600, 480, size=100)

	info_text.setText("左右鍵移動板子", 950, 320, 'SimHei.ttf',size=33)
	info_text.setText("使我方(綠色)及", 950, 360, 'SimHei.ttf', size=33)
	info_text.setText("敵方(紅色)掉落", 950, 400, 'SimHei.ttf', size=33)
	info_text.setText("並依照階級大小", 950, 440, 'SimHei.ttf', size=33)
	info_text.setText("吃掉對立的敵人", 950, 480, 'SimHei.ttf', size=33)
	info_text.setText("每關會限制步數", 950, 520, 'SimHei.ttf', size=33)


	GAME_STATE = const.MENU
	NEXT_STATE = const.GAME_NONE
	clear_WORLD()

def clear(class_object, plotDisplay=None):
	clear_screen()
	class_object.clearFlag()

	if plotDisplay != None:
		plotDisplay.clearContext()

def clear_screen():
	display.fill(white)

def changeMAXMOVE():
	global MMOVE

	if CHAPTER == const.CHAPTER_3:
		MMOVE = 15
	else:
		MMOVE = 20 

def writeMove(board):

	color = None

	changeMAXMOVE()

	if WORLD_LINE == 'Z':
		color = gold
	else:
		color = red

	move = board.get_move()
	font = py.font.Font(const.PATH+const.FONTFILE+"SimHei.ttf", 50)
	text = font.render(str(move)+" Move", True, color)
	display.blit(text, (1000, 0))

	if GAME_STATE == const.GAME_PLAY:
		text_move = font.render("Max move is "+str(MMOVE), True, color)
		display.blit(text_move, (825, 70))
	elif GAME_STATE == const.INFO:
		text_move = font.render("Max move is INF", True, color)
		display.blit(text_move, (825, 70))


def level_set(level):

	if level == const.LEVEL_ONE:
		level_one_set(level_board,level_surface)
	elif level == const.LEVEL_TWO:
		level_two_set(level_board,level_surface)
	elif level == const.LEVEL_THREE:
		if WORLD_LINE == 'X':
			level_three_set(level_board,level_surface)
		if WORLD_LINE == 'Z':
			level_four_set(level_board,level_surface)

def transitions():

	global WORLD_LINE
	global CHAPTER
	global ACT

	if NEXT_STATE == const.PLOT or NEXT_STATE == const.GAME_PLAY:
		
		ACT += 1

		if (ACT == const.ACT_F):
			if CHAPTER == const.CHAPTER_2:
				if plotDisplay.press[0]:#press kill
					print("in Z")
					WORLD_LINE = 'Z'
					CHAPTER    = const.CHAPTER_2
					ACT        = const.ACT_2
					plotDisplay.reset_press()
				elif plotDisplay.press[1]: #press not kill
					print("in X")
					WORLD_LINE = 'X'
					CHAPTER    = const.CHAPTER_2
					ACT 	   = const.ACT_2
					plotDisplay.reset_press()
				else:
					print("in else")
					ACT = const.ACT_1
					CHAPTER += 1
			else:
				ACT = const.ACT_1
				CHAPTER += 1

def loadMUSIC(name):

	if music:
		if soundHandler.getName() != name:
			if soundHandler.isPlaying():
				soundHandler.stop()
			soundHandler.loadMUSIC(name)
			py.time.delay(500)
		else:
			print("music is same")

def play_music():
	if music:
		if not soundHandler.isPlaying():
			print(soundHandler.getName() + " play")
			soundHandler.play()

def event_judge(class_object, class_object2=None):
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		class_object.event_handle(event)
		if class_object2 != None:
			class_object2.event_handle(event)
		keyHandler.setKey(event)

def event_judge_game_play(class_object):

	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()
			quit()
		class_object.event_handle(event)
		level_board.event_handle(event)
		keyHandler.setKey(event)

def update(class_object, class_object2=None, write_object=None, board=None):
	
	class_object.update()#background
	
	if class_object2 != None:# plotdisplay
		class_object2.update()
	
	if GAME_STATE == const.INFO:
		if board != None:
			writeMove(board)
			level_newplayer_run(level_board, level_surface)

	if GAME_STATE == const.DOUBLE:
		if board != None :
			writeMove(board)
			random_obstacle(level_board)
			level_double_run(level_board,level_surface)

	if GAME_STATE == const.GAME_PLAY:
		if board != None:
			writeMove(board)
		if PLAYING_STATE == const.LEVEL_ONE:
			level_one_run(level_board,level_surface)
		elif PLAYING_STATE == const.LEVEL_TWO:
			level_two_run(level_board,level_surface)
		elif PLAYING_STATE == const.LEVEL_THREE:
			if WORLD_LINE == 'X':
				level_three_run(level_board,level_surface)
			if WORLD_LINE == 'Z':
				level_four_run(level_board,level_surface)
	if write_object != None:
		write_object.rec_write()

	py.display.update()
	clock.tick(fps)

def win():

	if len(enemy_list) == 0:
		return True
	if level_board.get_move() >= MMOVE:
		return False
	if len(soldier_list) == 0:
		return False

def isFinish():

	changeMAXMOVE()
	if level_board.get_move() >= MMOVE and level_board.get_clock() == 0 :
		return True
	if len(soldier_list) == 0 or len(enemy_list) == 0:
		return True

def run_menu():

	global GAME_STATE
	global NEXT_STATE
	global CHAPTER
	global ACT

	loadMUSIC(const.MUSICNAME[const.MENU])
	play_music()
	
	event_judge(menu)
	update(menu)
	if menu.start_is_press():
		print("start")
		GAME_STATE = const.LOADING
		NEXT_STATE = const.PLOT
		# CHAPTER   = const.CHAPTER_1
		# ACT       = const.ACT_1
		clear(menu)

	elif menu.custom_is_press():
		if menu.get_custom_button_name('INFO'):
			print('INFO')
			GAME_STATE = const.LOADING
			NEXT_STATE = const.INFO
		clear(menu)

	elif menu.back_is_press():
		exit()

def run_info():

	global GAME_STATE
	global NEXT_STATE

	loadMUSIC(const.MUSICNAME[const.INFO])
	level_newplayer_set(level_board, level_surface)

	while True:
		play_music()
		event_judge_game_play(info)
		update(info, board=level_board, write_object=info_text)
		if info.back_is_press():
			GAME_STATE = const.LOADING
			NEXT_STATE = const.MENU
			clear(info)
			break

def run_plot():

	global GAME_STATE
	global NEXT_STATE
	global PLAYING_STATE
	global WORLD_LINE
	global CHAPTER
	global ACT

	if CHAPTER == const.CHAPTER_3 and (ACT == 'L' or ACT == 'W'):
		if WORLD_LINE == 'X':
			if ACT == 'W':
				loadMUSIC(const.PLOTMX_W)
			if ACT == 'L':
				loadMUSIC(const.PLOTMX_L)
		if WORLD_LINE == 'Z':
			if ACT == 'W':
				loadMUSIC(const.PLOTMZ_W)
			if ACT == 'L':
				loadMUSIC(const.PLOTMZ_L)
	else:
		print("loadMUSIC")
		loadMUSIC(const.MUSICNAME[const.PLOT])

	plotDisplay.load_plot(WORLD_LINE, CHAPTER, ACT)
	if WORLD_LINE == 'N':
		plot.loadUI(plot_image.getImg(CHAPTER))
	elif WORLD_LINE == 'X' and CHAPTER == const.CHAPTER_3:
		plot.loadUI(plot_image.getImg(const.PLOT_3_X))
	elif WORLD_LINE == 'Z' and CHAPTER == const.CHAPTER_3:
		plot.loadUI(plot_image.getImg(const.PLOT_3_Z))
	#print(plotDisplay.index)


	while True:

		play_music()

		event_judge(plot, plotDisplay)
		plotDisplay.plot_display()
	
		update(plot, plotDisplay)

		if plotDisplay.isfinish() or plot.custom_is_press():
			if plot.get_custom_button_name('SKIP') or plotDisplay.isfinish():
				if plot.get_custom_button_name('SKIP'):
					if CHAPTER == const.CHAPTER_2 and ACT == const.ACT_2 and WORLD_LINE == 'N':
						plotDisplay.toChoose()
						clear(plot)
						print('SKIP')
						continue
					if (CHAPTER == const.CHAPTER_3) and (ACT == 'W' or ACT == 'L'):
						clear(plot, plotDisplay)
						GAME_STATE = const.GAME_FINISH
						print('finish')
						break
					print('SKIP')
				if (CHAPTER == const.CHAPTER_3) and (ACT == 'W' or ACT == 'L'):
					clear(plot, plotDisplay)
					GAME_STATE = const.GAME_FINISH
					print('finish')
					break
				if ACT == const.ACT_1:
					GAME_STATE    = const.LOADING
					NEXT_STATE    = const.GAME_PLAY
					PLAYING_STATE = CHAPTER
				else:
					if (WORLD_LINE=='N') and (CHAPTER == const.CHAPTER_2 and ACT == const.ACT_2):
						GAME_STATE == const.PLOT
					else:
						GAME_STATE = const.LOADING
						NEXT_STATE = const.PLOT
				clear(plot, plotDisplay)
				transitions()
				print(WORLD_LINE+'_'+str(CHAPTER)+'_'+str(ACT))
				break

	#while story is playing
	#if story is finish
		#

	pass

def run_story():

	global GAME_STATE
	global NEXT_STATE

	pass

def run_game_play():

	global GAME_STATE
	global NEXT_STATE
	global ACT

	if CHAPTER == const.CHAPTER_3:
		if WORLD_LINE == 'X':
			loadMUSIC(const.BATTLEM[2])
		if WORLD_LINE == 'Z':
			loadMUSIC(const.BATTLEM[3])
	else:
		loadMUSIC(const.BATTLEM[1])



	if WORLD_LINE == 'N':
		game.loadUI(plot_image.getImg(CHAPTER))
	elif WORLD_LINE == 'X' and CHAPTER == const.CHAPTER_3:
		game.loadUI(plot_image.getImg(const.PLOT_3_X))
	elif WORLD_LINE == 'Z' and CHAPTER == const.CHAPTER_3:
		game.loadUI(plot_image.getImg(const.PLOT_3_Z))

	leave = False

	level_set(CHAPTER)
	# level_board = get_level_board()


	while 1:
		play_music()
		event_judge_game_play(game)
		update(game, board=level_board)
		if isFinish():
			if win():
				while 1:
					event_judge_game_play(game)
					update(game, board=level_board, write_object=win_text)
					if keyHandler.getKey() == py.K_RETURN:
						leave = True
						clear(game)
						print(WORLD_LINE+'_'+str(CHAPTER)+'_'+str(ACT))
						GAME_STATE = const.LOADING
						NEXT_STATE = const.PLOT
						if CHAPTER == const.CHAPTER_3 and ACT == const.ACT_2:
							ACT = 'W'
							print(ACT)
						break
					if game.custom_is_press():
						if game.get_custom_button_name("menu"):
							clear(game)
							GAME_STATE = const.LOADING
							NEXT_STATE = const.MENU
							clear_WORLD()
							loadMUSIC(const.MUSICNAME[const.MENU])
							writeText.clear()
							leave = True
							break

			else:
				while 1:
					event_judge_game_play(game)
					update(game, board=level_board, write_object=lose_text)
					if keyHandler.getKey() == py.K_RETURN:
						leave = True
						clear(game)
						GAME_STATE = const.LOADING
						NEXT_STATE = const.GAME_PLAY
						if CHAPTER == const.CHAPTER_3 and ACT == const.ACT_2:
							GAME_STATE = const.LOADING
							NEXT_STATE = const.PLOT
							ACT = 'L'
							print(ACT)
						break
					if game.custom_is_press():
						if game.get_custom_button_name("menu"):
							clear(game)
							GAME_STATE = const.LOADING
							NEXT_STATE = const.MENU
							clear_WORLD()
							loadMUSIC(const.MUSICNAME[const.MENU])
							writeText.clear()
							leave = True
							break
		if game.custom_is_press():
			if game.get_custom_button_name("restart"):
				clear(game)
				GAME_STATE = const.LOADING
				NEXT_STATE = const.GAME_PLAY
				break
			if game.get_custom_button_name("menu"):
				clear(game)
				GAME_STATE = const.LOADING
				NEXT_STATE = const.MENU
				clear_WORLD()
				loadMUSIC(const.MUSICNAME[const.MENU])
				writeText.clear()
				break

		if leave:
			break;

def run_game_pause():

	global GAME_STATE
	global NEXT_STATE

	pass

def run_game_finish():

	global GAME_STATE
	global NEXT_STATE
	global WORLD_LINE
	global CHAPTER
	global ACT

	writeText.setText("結局", 600, 250, 'SimHei.ttf', green, 100)
	writeText.setText("達成",600, 450, 'SimHei.ttf', purple, 100)
	if WORLD_LINE == 'X':
		if ACT == 'W':
			writeText.setText("美麗的世界", 600, 350, 'SimHei.ttf', gold, 100)
		if ACT == 'L':
			writeText.setText("不後悔的決定", 600, 350, 'SimHei.ttf', gold, 100)
	if WORLD_LINE == 'Z':
		if ACT == 'W':
			writeText.setText("深淵的等待", 600, 350, 'SimHei.ttf', black, 100)
		if ACT == 'L':
			writeText.setText("喪鐘為誰而鳴", 600, 350, 'SimHei.ttf', gold, 100)
	#writeText.setText("Thanks for playing", 600, 300, 'Regular.ttf', orangered, 100)

	while True:
		play_music()
		event_judge(finish)
		update(finish, write_object=writeText)
		if finish.get_custom_button_name("Menu"):
			clear(finish)
			GAME_STATE = const.LOADING
			NEXT_STATE = const.MENU
			clear_WORLD()
			loadMUSIC(const.MUSICNAME[const.MENU])
			writeText.clear()
			break

	pass

def run_loading() :
	global GAME_STATE
	global NEXT_STATE
	load_len = 0
	loading.update()
	print("loading")
	while True:
		load_len = load_len + random.randint(0,3)
		if load_len > 900 :
			load_len = 900
		py.draw.rect(display,gold,[150,600,load_len,20])
		py.draw.rect(display,black,[150,600,900,20],3)
		py.display.update()
		if load_len >= 900 :
			GAME_STATE = NEXT_STATE
			break

def run_double():

	global GAME_STATE
	global NEXT_STATE

	level_double_set(level_board, level_surface)

	while True:
		event_judge_game_play(double)
		update(double, board=level_board)
		# if double.back_is_press():
		# 	GAME_STATE = const.LOADING
		# 	NEXT_STATE = const.MENU
		# 	clear(double)
		# 	break


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
		run_game_finish,
	const.LOADING:
		run_loading,
	const.DOUBLE:
		run_double

}

def game_loop():

	global GAME_STATE
	global NEXT_STATE

	init()

	while const.GAME_LOOP:
		
		switch.get(GAME_STATE)()


if __name__ == "__main__":
	game_loop()