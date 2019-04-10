from Declaration import *
from chess import *
from board import *
from interface import *

# level_double_board = Board()
# level_double_surface = interface()

def level_double_set(level_double_board,level_double_surface) :

	level_double_board.for_reset()
	level_double_board.doublemode = True
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].kill_myself()
	for i in range(0,len(soldier_list)) :
		soldier_list[i].kill_myself()
	for i in range(0,len(enemy_list)):
		enemy_list[i].kill_myself()

	obstacle_list.clear()
	soldier_list.clear()
	enemy_list.clear()

	obstacle_list.append(chess( B2_x, B2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G2_x, G2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C3_x, C3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F3_x, F3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( A4_x, A4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D4_x, D4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E4_x, E4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( H4_x, H4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( A5_x, A5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D5_x, D5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E5_x, E5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( H5_x, H5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C6_x, C6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F6_x, F6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( B7_x, B7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G7_x, G7_y, const.OBSTACLE  ))

	soldier_list.append(chess( B1_x, B1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( G1_x, G1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( C2_x, C2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( D2_x, D2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( E2_x, E2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( F2_x, F2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( C1_x, C1_y, const.SOLDIER, const.COMMANDER ))
	soldier_list.append(chess( F1_x, F1_y, const.SOLDIER, const.COMMANDER ))
	soldier_list.append(chess( D1_x, D1_y, const.SOLDIER, const.KING      ))
	soldier_list.append(chess( E1_x, E1_y, const.SOLDIER, const.KING      ))

	enemy_list.append(chess( B8_x, B8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( G8_x, G8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C7_x, C7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D7_x, D7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E7_x, E7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( F7_x, F7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C8_x, C8_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( F8_x, F8_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( D8_x, D8_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( E8_x, E8_y, const.ENEMY, const.KING      ))

	level_double_board.build(level_double_surface)

def random_obstacle(level_double_board) :
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].kill_myself()
	obstacle_list.clear()
	for i in range(0,10) :
		x = random.randint(0,7)
		y = random.randint(0,7)
		obstacle_list.append(chess( x, y, const.OBSTACLE  ))

def level_double_run(level_double_board,level_double_surface) :

	level_double_board.display(display)
	level_double_board.build(level_double_surface)
	level_double_board.set_clock_time()

	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw(level_double_board.board, level_double_surface)
	for i in range(0,len(soldier_list)):
		soldier_list[i].draw(level_double_board.board, level_double_surface)
		if level_double_board.get_start_move() :
			soldier_list[i].check(level_double_board.get_mode())
		soldier_list[i].down(level_double_board.get_mode(),level_double_board.get_action())
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw(level_double_board.board, level_double_surface)
		if level_double_board.get_start_move() :
			enemy_list[i].check(level_double_board.get_mode())
		enemy_list[i].down(level_double_board.get_mode(),level_double_board.get_action())

	obstacle_list[0].defeat(level_double_board.get_spin(),level_double_board.get_mode(),level_double_board.get_start_move(),soldier_list,enemy_list)

	if level_double_board.get_spin() == False and level_double_board.get_move()%3 == 0 and level_double_board.get_clock() == 1 :
		random_obstacle(level_double_board)

	for i in range(0,len(obstacle_list)) :
		if obstacle_list[i].get_life() == False :
			del obstacle_list[i]
			break


def level_one_WorL() :
	if len(soldier_list) == 0 and len(enemy_list) == 0 :
		return const.FLAT
	if len(soldier_list) == 0 :
		return const.LOSE
	if len(enemy_list) == 0 :
		return const.WIN
	return 0