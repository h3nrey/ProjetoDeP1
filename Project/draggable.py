import pygame as pg;

class Draggable(pg.sprite.Sprite):
	def __init__(self, draggable):
		super().__init__()
		self.image = pg.Surface((32,32))
		self.image.fill("brown")
		self.rect = self.image.get_rect(center = (100,150))
		self.is_draggable = draggable
	
	def update(self):
		pass
    
