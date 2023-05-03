import pygame as pg
import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# join the filepath and the filename
filePath = os.path.join(sourceFileDir, 'Graphics/pixel.ttf');

class Text(pg.sprite.Sprite):
	def __init__(self, pos=(50, 50), text="jorge", fontSize=24, color= "white"):
		super().__init__()
		self.font = pg.font.Font(filePath, fontSize)
		self.image = self.font.render(text, False, color)
		self.rect = self.image.get_rect(center = pos)

	def update(self, text):
		self.image = self.font.render(str(text), False, "white")

class Ui():
	def __init__(self, screen):
		self.keys_text = Text((80, 20), "chaves: 0")
		# self.clock_text = Text((250, 20), "tempo: 60")
		self.energia_text = Text((300, 20), "energia: 10")
		self.screen = screen
		self.elements = pg.sprite.Group()
		self.setup_ui()

	def setup_ui(self):
		self.elements.add(self.keys_text)
		# self.elements.add(self.clock_text)
		self.elements.add(self.energia_text)
	
	def update(self, content):
		for i, el in enumerate(self.elements):
			el.update(content[i])
		self.elements.draw(self.screen)
