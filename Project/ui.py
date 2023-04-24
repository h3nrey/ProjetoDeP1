import pygame as pg

class Text(pg.sprite.Sprite):
	def __init__(self, pos, text, fontSize=10, color= "white"):
		super().__init__()
		self.font = pg.font.Font("Graphics/pixel.TTF", fontSize)
		self.surf = self.font.render(text, False, color)
		self.rect = self.surf.get_rect(center = pos)

