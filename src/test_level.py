from Declaration import *
from chess import *
from board import *

obstacle_list = []
soldier_list = []
enemy_list = []

obstacle_list.append(chess(A6_x,A6_y,const.OBSTACLE))
obstacle_list.append(chess(B5_x,B5_y,const.OBSTACLE))
obstacle_list.append(chess(C2_x,C2_y,const.OBSTACLE))
obstacle_list.append(chess(C4_x,C4_y,const.OBSTACLE))
obstacle_list.append(chess(F7_x,F7_y,const.OBSTACLE))
obstacle_list.append(chess(G5_x,G5_y,const.OBSTACLE))
obstacle_list.append(chess(H4_x,H4_y,const.OBSTACLE))

soldier_list.append(chess(A1_x,A1_y,const.SOLDIER))
soldier_list.append(chess(B3_x,B3_y,const.SOLDIER))

enemy_list.append(chess(D1_x,D1_y,const.ENEMY))
enemy_list.append(chess(D2_x,D2_y,const.ENEMY))
enemy_list.append(chess(E3_x,E3_y,const.ENEMY))
enemy_list.append(chess(E4_x,E4_y,const.ENEMY))
enemy_list.append(chess(D5_x,D5_y,const.ENEMY))
enemy_list.append(chess(D6_x,D6_y,const.ENEMY))
enemy_list.append(chess(A7_x,A7_y,const.ENEMY))
enemy_list.append(chess(A8_x,A8_y,const.ENEMY))
enemy_list.append(chess(E5_x,E5_y,const.ENEMY))

def test_level_run() :
	for i in range(0,len(obstacle_list)) :
		obstacle_list[i].draw()
	for i in range(0,len(soldier_list)) :
		soldier_list[i].draw()
		soldier_list[i].check()
		soldier_list[i].down()
	for i in range(0,len(enemy_list)) :
		enemy_list[i].draw()
		enemy_list[i].check()
		enemy_list[i].down()
	# defeat_class(soldier_list,enemy_list)