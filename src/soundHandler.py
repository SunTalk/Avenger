import pygame as p
import time

class SoundHandler():

	def __init__(self, path, file, name):
		p.mixer.init()
		p.time.delay(1000)
		p.mixer.music.load(path+file+name)


	def play(self):
		print('play')
		p.mixer.music.play()

	def stop(self):
		p.mixer.music.stop()

	def rewind(self):
		p.mixer.music.rewind()

	def pause(self):
		p.mixer.music.pause()

	def unpause(self):
		p.mixer.music.unpause()

	def set_volume(self):
		p.mixer.music.set_volume()

	def set_pos(self):
		p.mixer.music.set_pos()

	def get_volume(self):
		return p.mixer.music.get_volume()

	def isPlaying(self):
		return p.mixer.music.get_busy()
	def get_volume():
		return p.mixer.music.get_volume()
