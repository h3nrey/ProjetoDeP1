import pygame as pg;
from settings import *
from support import *

class Tile(pg.sprite.Sprite):
	def __init__(self, pos, tag, files,deg= 0):
		super().__init__()
		self.frames = GetSurf(files)
		self.image = self.frames[0]
		self.rect = self.image.get_rect(center = pos)
		self.tag = tag
		self.deg = deg
		self.rotate(deg)
	
	def rotate(self, deg):
		self.image = pg.transform.rotate(self.image, deg);
	
	def update_surf(self, other_sprite):
		self.image = other_sprite
		self.rotate(self.deg)

	def destroy(self):
		self.kill()
    
