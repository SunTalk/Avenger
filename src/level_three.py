from Declaration import *
from chess import *
from board import *
from interface import *

level_three_board = Board()
level_three_surface = interface()

def level_three_set() :

	level_three_board.for_reset()
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].kill_myself()
	for i in range(0,len(soldier_list)) :
		soldier_list[i].kill_myself()
	for i in range(0,len(enemy_list)):
		enemy_list[i].kill_myself()

	obstacle_list.clear()
	soldier_list.clear()
	enemy_list.clear()

	obstacle_list.append(chess( C4_x, C4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F4_x, F4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C5_x, C5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F5_x, F5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D3_x, D3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E3_x, E3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D6_x, D6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E6_x, E6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( B2_x, B2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( B7_x, B7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G2_x, G2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G7_x, G7_y, const.OBSTACLE  ))

	soldier_list.append(chess( H7_x, H7_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( G8_x, G8_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( G1_x, G1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H2_x, H2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H5_x, H5_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H4_x, H4_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H1_x, H1_y, const.SOLDIER, const.COMMANDER ))
	soldier_list.append(chess( H8_x, H8_y, const.SOLDIER, const.COMMANDER ))

	enemy_list.append(chess( A7_x, A7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( B8_x, B8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( B1_x, B1_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( A2_x, A2_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( A1_x, A1_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( A8_x, A8_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( B4_x, B4_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( B5_x, B5_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( A4_x, A4_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( A5_x, A5_y, const.ENEMY, const.KING      ))

	level_three_board.build(level_three_surface)

def level_three_run() :

	level_three_board.display(display)
	level_three_board.build(level_three_surface)
	level_three_board.set_move_time()

	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw(level_three_board.board, level_three_surface)
	for i in range(0,len(soldier_list)):
		soldier_list[i].draw(level_three_board.board, level_three_surface)
		if level_three_board.get_start_move() :
			soldier_list[i].check(level_three_board.get_mode())
		soldier_list[i].down(level_three_board.get_mode(),level_three_board.get_action())
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw(level_three_board.board, level_three_surface)
		if level_three_board.get_start_move() :
			enemy_list[i].check(level_three_board.get_mode())
		enemy_list[i].down(level_three_board.get_mode(),level_three_board.get_action())
		
	obstacle_list[0].defeat(level_three_board.get_spin(),level_three_board.get_mode(),soldier_list,enemy_list)

def level_one_WorL() :
	if len(soldier_list) == 0 :
		return const.LOSE
	if len(enemy_list) == 2 :
		return const.WIN
	return 0