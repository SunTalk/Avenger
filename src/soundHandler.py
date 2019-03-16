import pygame as py
import time

class SoundHandler():

	def __init__(self, path, file, name):
		py.mixer.init()
		py.time.delay(1000)
		py.mixer.music.load(path+file+name)


	def play(self):
		print('play')
		py.mixer.music.play()

	def stop(self):
		py.mixer.music.stop()

	def rewind(self):
		py.mixer.music.rewind()

	def pause(self):
		py.mixer.music.pause()

	def unpause(self):
		py.mixer.music.unpause()

	def set_volume(self):
		py.mixer.music.set_volume()

	def set_pos(self):
		py.mixer.music.set_pos()

	def get_volume(self):
		return py.mixer.music.get_volume()

	def isPlaying(self):
		return py.mixer.music.get_busy()
	def get_volume():
		return py.mixer.music.get_volume()
