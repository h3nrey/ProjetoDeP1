import pygame as pg;
from settings import *
from support import *

class Tile(pg.sprite.Sprite):
	def __init__(self, pos, color, tag):
		super().__init__()
		# self.image = pg.Surface((TILESIZE - 2, TILESIZE - 2))
		self.image = GetSurf(tag)
		# self.image.fill(color)
		self.rect = self.image.get_rect(center = pos)
		self.tag = tag
		
	def destroy(self):
		self.kill()
    
