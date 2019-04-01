from Declaration import *
from chess import *
from board import *
from interface import *

# level_four_board = Board()
# level_four_surface = interface()

def level_four_set(level_four_board,level_four_surface) :

	level_four_board.for_reset()
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
	obstacle_list.append(chess( D2_x, D2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( F2_x, F2_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G3_x, G3_y, const.OBSTACLE  ))
	obstacle_list.append(chess( B4_x, B4_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G5_x, G5_y, const.OBSTACLE  ))
	obstacle_list.append(chess( B6_x, B6_y, const.OBSTACLE  ))
	obstacle_list.append(chess( C7_x, C7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E7_x, E7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G7_x, G7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( E7_x, E7_y, const.OBSTACLE  ))
	obstacle_list.append(chess( G7_x, G7_y, const.OBSTACLE  ))

	soldier_list.append(chess( G2_x, G2_y, const.SOLDIER, const.KING      ))
	soldier_list.append(chess( G1_x, G1_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H2_x, H2_y, const.SOLDIER, const.SERVANT   ))
	soldier_list.append(chess( H1_x, H1_y, const.SOLDIER, const.SERVANT   ))

	enemy_list.append(chess( B7_x, B7_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( C5_x, C5_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( D6_x, D6_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( B8_x, B8_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( A8_x, A8_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( A7_x, A7_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( C4_x, C4_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( D5_x, D5_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( E6_x, E6_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( A4_x, A4_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( B5_x, B5_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C6_x, C6_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D7_x, D7_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E8_x, E8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( C3_x, C3_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( D4_x, D4_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E5_x, E5_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( F6_x, F6_y, const.ENEMY, const.SERVANT   ))


	level_four_board.build(level_four_surface)

def level_four_run(level_four_board,level_four_surface) :

	level_four_board.display(display)
	level_four_board.build(level_four_surface)
	level_four_board.set_clock_time()

	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw(level_four_board.board, level_four_surface)
	for i in range(0,len(soldier_list)):
		soldier_list[i].draw(level_four_board.board, level_four_surface)
		if level_four_board.get_start_move() :
			soldier_list[i].check(level_four_board.get_mode())
		soldier_list[i].down(level_four_board.get_mode(),level_four_board.get_action())
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw(level_four_board.board, level_four_surface)
		if level_four_board.get_start_move() :
			enemy_list[i].check(level_four_board.get_mode())
		enemy_list[i].down(level_four_board.get_mode(),level_four_board.get_action())
		
	obstacle_list[0].defeat(level_four_board.get_spin(),level_four_board.get_mode(),level_four_board.get_start_move(),soldier_list,enemy_list)

	if level_four_board.get_spin() == False and level_four_board.get_move()%3 == 0 and level_four_board.get_clock() == 1 :
		enemy_list.append(chess( random.randint(0,7), random.randint(0,7), const.ENEMY, random.randint(1,3) ))
		enemy_list.append(chess( random.randint(0,7), random.randint(0,7), const.ENEMY, random.randint(1,3) ))
		enemy_list.append(chess( random.randint(0,7), random.randint(0,7), const.ENEMY, random.randint(1,3) ))
		level_four_board.add_chess()

# def level_four_WorL() :
# 	if len(soldier_list) == 0 :
# 		return const.LOSE
# 	if len(enemy_list) == 0 :
# 		return const.WIN
# 	return 0