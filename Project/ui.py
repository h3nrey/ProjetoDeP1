import pygame as pg
import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# join the filepath and the filename
filePath = os.path.join(sourceFileDir, 'Graphics/pixel.ttf');

class Text(pg.sprite.Sprite):
	def __init__(self, pos, text, fontSize=24, color= "white"):
		super().__init__()
		self.font = pg.font.Font(filePath, fontSize)
		self.image = self.font.render(text, False, color)
		self.rect = self.image.get_rect(center = pos)

	def update(self, text):
		self.image = self.font.render(str(text), False, "white")

