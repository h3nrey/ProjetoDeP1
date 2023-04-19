import pygame as pg
from settings import *
from tile import *

class Map():
	def __init__(self, screen):
		self.map = map
		self.world_map = {}
		self.screen = screen
		self.tiles = pg.sprite.Group()
		self.create_map()

	def create_map(self):
		for j, row in enumerate(self.map):
			for i, cell in enumerate(row):
				if cell != " ":
					drag = False
					color = "darkgray"
					if cell == "D": 
						drag = True
						color = "red"

					tile = Tile(drag, (i * 32, j * 32), color)
					# print(self.tiles)
					self.tiles.add(tile)

	def draw_map(self):
		for tile in self.world_map:
			print(tile)
			# pg.draw.rect(self.screen, "darkgray", (pos[0] * 32, pos[1] * 32, 32, 32))
			# self.tiles.add(tile)
		self.tiles.draw()

