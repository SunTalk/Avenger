from Declaration import *
from chess import *
from Board import *
from interface import *

level_one_board = Board()
level_one_surface = interface()

def level_one_set() :

	level_one_board.for_reset()
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].kill_myself()
	for i in range(0,len(soldier_list)) :
		soldier_list[i].kill_myself()
	for i in range(0,len(enemy_list)):
		enemy_list[i].kill_myself()

	obstacle_list.clear()
	soldier_list.clear()
	enemy_list.clear()

	obstacle_list.append(chess( A1_x, A1_y, const.OBSTACLE  ))
	obstacle_list.append(chess( H1_x, H1_y, const.OBSTACLE  ))
	obstacle_list.append(chess( A8_x, A8_y, const.OBSTACLE  ))
	obstacle_list.append(chess( H8_x, H8_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C3_x, C3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F3_x, F3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C6_x, C6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F6_x, F6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D2_x, D2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E2_x, E2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( D7_x, D7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E7_x, E7_y, const.OBSTACLE  ))

	soldier_list.append(chess( B1_x, B1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( C1_x, C1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( D1_x, D1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( E1_x, E1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( F1_x, F1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( G1_x, G1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( C2_x, C2_y, const.SOLDIER, const.COMMANDER ))
	soldier_list.append(chess( F2_x, F2_y, const.SOLDIER, const.COMMANDER ))

	enemy_list.append(chess( B8_x, B8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C8_x, C8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D8_x, D8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E8_x, E8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( F8_x, F8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( G8_x, G8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C7_x, C7_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( F7_x, F7_y, const.ENEMY, const.COMMANDER ))

	level_one_board.build(level_one_surface)

def level_one_run() :

	level_one_board.display(display)
	level_one_board.build(level_one_surface)
	level_one_board.set_move_time()

	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw(level_one_board.board, level_one_surface)
	for i in range(0,len(soldier_list)):
		soldier_list[i].draw(level_one_board.board, level_one_surface)
		if level_one_board.get_start_move() :
			soldier_list[i].check(level_one_board.get_mode())
		soldier_list[i].down(level_one_board.get_mode(),level_one_board.get_action())
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw(level_one_board.board, level_one_surface)
		if level_one_board.get_start_move() :
			enemy_list[i].check(level_one_board.get_mode())
		enemy_list[i].down(level_one_board.get_mode(),level_one_board.get_action())
		
	obstacle_list[0].defeat(level_one_board.get_spin(),level_one_board.get_mode(),soldier_list,enemy_list)

# def level_one_WorL() :
# 	if len(soldier_list) == 0 :
# 		return const.LOSE
# 	if len(enemy_list) == 0 :
# 		return const.WIN
# 	return 0