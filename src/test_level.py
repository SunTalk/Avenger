from Declaration import *
from chess import *
from test_Board import *
from interface import *

test_b = testBoard()
game = interface()

def test_level_set() :

	test_b.for_reset()
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].kill_myself()
	for i in range(0,len(soldier_list)) :
		soldier_list[i].kill_myself()
	for i in range(0,len(enemy_list)):
		enemy_list[i].kill_myself()

	obstacle_list.clear()
	soldier_list.clear()
	enemy_list.clear()

	obstacle_list.append(chess( A6_x, A6_y, const.OBSTACLE ))
	obstacle_list.append(chess( B5_x, B5_y, const.OBSTACLE ))
	obstacle_list.append(chess( C2_x, C2_y, const.OBSTACLE ))
	obstacle_list.append(chess( C4_x, C4_y, const.OBSTACLE ))
	obstacle_list.append(chess( F7_x, F7_y, const.OBSTACLE ))
	obstacle_list.append(chess( G4_x, G4_y, const.OBSTACLE ))
	obstacle_list.append(chess( F3_x, F3_y, const.OBSTACLE ))
	obstacle_list.append(chess( C7_x, C7_y, const.OBSTACLE ))
	obstacle_list.append(chess( H7_x, H7_y, const.OBSTACLE ))
	obstacle_list.append(chess( E8_x, E8_y, const.OBSTACLE ))
	obstacle_list.append(chess( G1_x, G1_y, const.OBSTACLE ))
	 
	soldier_list.append(chess( A1_x, A1_y, const.SOLDIER, const.KING      ))
	soldier_list.append(chess( B6_x, B6_y, const.SOLDIER, const.COMMANDER ))
	soldier_list.append(chess( B3_x, B3_y, const.SOLDIER, const.SERVANT   ))

	enemy_list.append(chess( A3_x, A3_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( D1_x, D1_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( D2_x, D2_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E3_x, E3_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( E4_x, E4_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( D5_x, D5_y, const.ENEMY, const.COMMANDER ))
	enemy_list.append(chess( D6_x, D6_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( A7_x, A7_y, const.ENEMY, const.KING      ))
	enemy_list.append(chess( A8_x, A8_y, const.ENEMY, const.SERVANT   ))
	enemy_list.append(chess( E5_x, E5_y, const.ENEMY, const.SERVANT   ))

	test_b.build(game)

def test_level_run() :

	test_b.display(display)
	test_b.build(game)
	test_b.set_move_time()

	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw(test_b.board, game)
	for i in range(0,len(soldier_list)):
		soldier_list[i].draw(test_b.board, game)
		if test_b.get_start_move() :
			soldier_list[i].check(test_b.get_mode())
		soldier_list[i].down(test_b.get_mode(),test_b.get_action())
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw(test_b.board, game)
		if test_b.get_start_move() :
			enemy_list[i].check(test_b.get_mode())
		enemy_list[i].down(test_b.get_mode(),test_b.get_action())
		
	obstacle_list[0].defeat(test_b.get_spin(),test_b.get_mode(),soldier_list,enemy_list)