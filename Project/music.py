import pygame as pg
from support import *

calm_music = get_file_path("Audio/RequiemIntrotus.mp3")
excited_music =  get_file_path("Audio/ElAngelus.mp3")
move_sound = get_file_path("Audio/move.wav")
class AudioSystem:
		def __init__(self):
				pg.mixer.init()
				self.music_calm = pg.mixer.Sound(calm_music)
				self.music_excited = pg.mixer.Sound(excited_music)
				self.music_calm.set_volume(1)
				self.music_excited.set_volume(0.2)
				
		def play_calm_music(self):
				self.music_calm.play(loops=-1)
				
		def play_excited_music(self):
				self.music_excited.play(loops=-1)
				
		def play_sound(self, sound):
			sound = pg.mixer.Sound(sound)
			sound.play()
				
		def stop_music(self):
				pg.mixer.stop()
				
		def set_volume(self, volume):
				self.music_calm.set_volume(volume)
				self.music_excited.set_volume(volume)
        