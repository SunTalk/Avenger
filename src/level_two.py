from Declaration import *
from chess import *
from Board import *
from interface import *

level_two_board = Board()
level_two_surface = interface()

def level_two_set() :

	level_two_board.for_reset()
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].kill_myself()
	for i in range(0,len(soldier_list)) :
		soldier_list[i].kill_myself()
	for i in range(0,len(enemy_list)):
		enemy_list[i].kill_myself()

	obstacle_list.clear()
	soldier_list.clear()
	enemy_list.clear()

	obstacle_list.append(chess( B1_x, B1_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D1_x, D1_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F1_x, F1_y, const.OBSTACLE  ))
	obstacle_list.append(chess( H1_x, H1_y, const.OBSTACLE  ))
	obstacle_list.append(chess( A3_x, A3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C3_x, C3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E3_x, E3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G3_x, G3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( B5_x, B5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D5_x, D5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F5_x, F5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( H5_x, H5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( A7_x, A7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C7_x, C7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E7_x, E7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G7_x, G7_y, const.OBSTACLE  ))

	soldier_list.append(chess( A2_x, A2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( C2_x, C2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( E2_x, E2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( G2_x, G2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( B4_x, B4_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( D4_x, D4_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( F4_x, F4_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H4_x, H4_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( A6_x, A6_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( C6_x, C6_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( E6_x, E6_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( G6_x, G6_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H6_x, H6_y, const.SOLDIER, const.COMMANDER ))

	enemy_list.append(chess( A1_x, A1_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( C1_x, C1_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E1_x, E1_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( G1_x, G1_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( B3_x, B3_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D3_x, D3_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( F3_x, F3_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( H3_x, H3_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( A5_x, A5_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C5_x, C5_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E5_x, E5_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( G5_x, G5_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( B7_x, B7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D7_x, D7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( F7_x, F7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( H7_x, H7_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( A8_x, A8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( B8_x, B8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C8_x, C8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D8_x, D8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E8_x, E8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( F8_x, F8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( G8_x, G8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( H8_x, H8_y, const.ENEMY, const.SERVANT   ))

	level_two_board.build(level_two_surface)

def level_two_run() :

	level_two_board.display(display)
	level_two_board.build(level_two_surface)
	level_two_board.set_clock_time()

	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw(level_two_board.board, level_two_surface)
	for i in range(0,len(soldier_list)):
		soldier_list[i].draw(level_two_board.board, level_two_surface)
		if level_two_board.get_start_move() :
			soldier_list[i].check(level_two_board.get_mode())
		soldier_list[i].down(level_two_board.get_mode(),level_two_board.get_action())
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw(level_two_board.board, level_two_surface)
		if level_two_board.get_start_move() :
			enemy_list[i].check(level_two_board.get_mode())
		enemy_list[i].down(level_two_board.get_mode(),level_two_board.get_action())
		
	obstacle_list[0].defeat(level_two_board.get_spin(),level_two_board.get_mode(),soldier_list,enemy_list)

# def level_two_WorL() :
# 	if len(soldier_list) == 0 :
# 		return const.LOSE
# 	if len(enemy_list) == 0 :
# 		return const.WIN
# 	return 0