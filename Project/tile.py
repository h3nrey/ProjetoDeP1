import pygame as pg;

class Tile(pg.sprite.Sprite):
	def __init__(self, pos, color, tag):
		super().__init__()
		self.image = pg.Surface((30, 30))
		self.image.fill(color)
		self.rect = self.image.get_rect(center = pos)
		self.tag = tag

	def destroy(self):
		self.kill()
    
