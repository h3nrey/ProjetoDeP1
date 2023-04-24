import pygame as pg;

class Tile(pg.sprite.Sprite):
	def __init__(self, pos, color, static, collectable, draggable):
		super().__init__()
		self.image = pg.Surface((30, 30))
		self.image.fill(color)
		self.rect = self.image.get_rect(center = pos)
		self.is_draggable = draggable
		self.is_collectable = collectable
		self.is_static = static

	def destroy(self):
		self.kill()
    
