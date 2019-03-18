import const
## block center
	# A1_x = 0 ,A2_x = 1 ,A3_x = 2 ,A4_x = 3 ,A5_x = 4 ,A6_x = 5 ,A7_x = 7 ,A8_x = 7
	# B1_x = 0 ,B2_x = 1 ,B3_x = 2 ,B4_x = 3 ,B5_x = 4 ,B6_x = 5 ,B7_x = 7 ,B8_x = 7
	# C1_x = 0 ,C2_x = 1 ,C3_x = 2 ,C4_x = 3 ,C5_x = 4 ,C6_x = 5 ,C7_x = 7 ,C8_x = 7
	# D1_x = 0 ,D2_x = 1 ,D3_x = 2 ,D4_x = 3 ,D5_x = 4 ,D6_x = 5 ,D7_x = 7 ,D8_x = 7
	# E1_x = 0 ,E2_x = 1 ,E3_x = 2 ,E4_x = 3 ,E5_x = 4 ,E6_x = 5 ,E7_x = 7 ,E8_x = 7
	# F1_x = 0 ,F2_x = 1 ,F3_x = 2 ,F4_x = 3 ,F5_x = 4 ,F6_x = 5 ,F7_x = 7 ,F8_x = 7
	# G1_x = 0 ,G2_x = 1 ,G3_x = 2 ,G4_x = 3 ,G5_x = 4 ,G6_x = 5 ,G7_x = 7 ,G8_x = 7
	# H1_x = 0 ,H2_x = 1 ,H3_x = 2 ,H4_x = 3 ,H5_x = 4 ,H6_x = 5 ,H7_x = 7 ,H8_x = 7

	# A1_y = 0 ,A2_y = 0 ,A3_y = 0 ,A4_y = 0 ,A5_y = 0 ,A6_y = 0 ,A7_y = 0 ,A8_y = 0
	# B1_y = 1 ,B2_y = 1 ,B3_y = 1 ,B4_y = 1 ,B5_y = 1 ,B6_y = 1 ,B7_y = 1 ,B8_y = 1 
	# C1_y = 2 ,C2_y = 2 ,C3_y = 2 ,C4_y = 2 ,C5_y = 2 ,C6_y = 2 ,C7_y = 2 ,C8_y = 2
	# D1_y = 3 ,D2_y = 3 ,D3_y = 3 ,D4_y = 3 ,D5_y = 3 ,D6_y = 3 ,D7_y = 3 ,D8_y = 3
	# E1_y = 4 ,E2_y = 4 ,E3_y = 4 ,E4_y = 4 ,E5_y = 4 ,E6_y = 4 ,E7_y = 4 ,E8_y = 4
	# F1_y = 5 ,F2_y = 5 ,F3_y = 5 ,F4_y = 5 ,F5_y = 5 ,F6_y = 5 ,F7_y = 5 ,F8_y = 5
	# G1_y = 6 ,G2_y = 6 ,G3_y = 6 ,G4_y = 6 ,G5_y = 6 ,G6_y = 6 ,G7_y = 6 ,G8_y = 6
	# H1_y = 7 ,H2_y = 7 ,H3_y = 7 ,H4_y = 7 ,H5_y = 7 ,H6_y = 7 ,H7_y = 7 ,H8_y = 7
##
const.ZERO  = 30

const.ONE   = 90
const.TWO   = 150
const.THREE = 210
const.FOUR  = 270
const.FIVE  = 330
const.SIX   = 390
const.SEVEN = 450
const.EIGHT = 510

const.NINE  = 570

boundary_x = [const.ZERO  ,const.ONE   ,const.TWO   ,const.THREE ,const.FOUR  ,const.FIVE  ,const.SIX   ,const.SEVEN ,const.EIGHT ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.EIGHT ,const.SEVEN ,const.SIX   ,const.FIVE  ,const.FOUR  ,const.THREE ,const.TWO   ,const.ONE   ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ]
boundary_y = [const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ZERO  ,const.ONE   ,const.TWO   ,const.THREE ,const.FOUR  ,const.FIVE  ,const.SIX   ,const.SEVEN ,const.EIGHT ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.NINE  ,const.EIGHT ,const.SEVEN ,const.SIX   ,const.FIVE  ,const.FOUR  ,const.THREE ,const.TWO   ,const.ONE   ]

board_x = [[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT],[const.ONE,const.TWO,const.THREE,const.FOUR,const.FIVE,const.SIX,const.SEVEN,const.EIGHT]]
board_y = [[const.ONE,const.ONE,const.ONE,const.ONE,const.ONE,const.ONE,const.ONE,const.ONE],[const.TWO,const.TWO,const.TWO,const.TWO,const.TWO,const.TWO,const.TWO,const.TWO],[const.THREE,const.THREE,const.THREE,const.THREE,const.THREE,const.THREE,const.THREE,const.THREE],[const.FOUR,const.FOUR,const.FOUR,const.FOUR,const.FOUR,const.FOUR,const.FOUR,const.FOUR],[const.FIVE,const.FIVE,const.FIVE,const.FIVE,const.FIVE,const.FIVE,const.FIVE,const.FIVE],[const.SIX,const.SIX,const.SIX,const.SIX,const.SIX,const.SIX,const.SIX,const.SIX],[const.SEVEN,const.SEVEN,const.SEVEN,const.SEVEN,const.SEVEN,const.SEVEN,const.SEVEN,const.SEVEN],[const.EIGHT,const.EIGHT,const.EIGHT,const.EIGHT,const.EIGHT,const.EIGHT,const.EIGHT,const.EIGHT]]

A1_x = 0
A2_x = 0
A3_x = 0
A4_x = 0
A5_x = 0
A6_x = 0
A7_x = 0
A8_x = 0
B1_x = 1
B2_x = 1
B3_x = 1
B4_x = 1
B5_x = 1
B6_x = 1
B7_x = 1
B8_x = 1
C1_x = 2
C2_x = 2
C3_x = 2
C4_x = 2
C5_x = 2
C6_x = 2
C7_x = 2
C8_x = 2
D1_x = 3
D2_x = 3
D3_x = 3
D4_x = 3
D5_x = 3
D6_x = 3
D7_x = 3
D8_x = 3
E1_x = 4
E2_x = 4
E3_x = 4
E4_x = 4
E5_x = 4
E6_x = 4
E7_x = 4
E8_x = 4
F1_x = 5
F2_x = 5
F3_x = 5
F4_x = 5
F5_x = 5
F6_x = 5
F7_x = 5
F8_x = 5
G1_x = 6
G2_x = 6
G3_x = 6
G4_x = 6
G5_x = 6
G6_x = 6
G7_x = 6
G8_x = 6
H1_x = 7
H2_x = 7
H3_x = 7
H4_x = 7
H5_x = 7
H6_x = 7
H7_x = 7
H8_x = 7

A1_y = 0
A2_y = 1
A3_y = 2
A4_y = 3
A5_y = 4
A6_y = 5
A7_y = 6
A8_y = 7
B1_y = 0
B2_y = 1
B3_y = 2
B4_y = 3
B5_y = 4
B6_y = 5
B7_y = 6
B8_y = 7
C1_y = 0
C2_y = 1
C3_y = 2
C4_y = 3
C5_y = 4
C6_y = 5
C7_y = 6
C8_y = 7
D1_y = 0
D2_y = 1
D3_y = 2
D4_y = 3
D5_y = 4
D6_y = 5
D7_y = 6
D8_y = 7
E1_y = 0
E2_y = 1
E3_y = 2
E4_y = 3
E5_y = 4
E6_y = 5
E7_y = 6
E8_y = 7
F1_y = 0
F2_y = 1
F3_y = 2
F4_y = 3
F5_y = 4
F6_y = 5
F7_y = 6
F8_y = 7
G1_y = 0
G2_y = 1
G3_y = 2
G4_y = 3
G5_y = 4
G6_y = 5
G7_y = 6
G8_y = 7
H1_y = 0
H2_y = 1
H3_y = 2
H4_y = 3
H5_y = 4
H6_y = 5
H7_y = 6
H8_y = 7

