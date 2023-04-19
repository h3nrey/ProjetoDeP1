import pygame as pg;

class Tile(pg.sprite.Sprite):
	def __init__(self, draggable, pos, color):
		super().__init__()
		self.image = pg.Surface((32, 32))
		self.image.fill(color)
		self.rect = self.image.get_rect(center = pos)
		self.is_draggable = draggable
	
	def update(self):
		pass
    
