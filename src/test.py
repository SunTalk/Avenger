import pygame as py
py.init()

display = py.display.set_mode((1200, 800))
py.display.set_caption('test')

while True:

	event = py.event.wait()

	if event.type == py.QUIT:
		py.quit()
		quit()
	print(event.type)