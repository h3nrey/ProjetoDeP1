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
				# if cell != " ":
				color = "#222222"
				tag = "floor"

				if cell == "X":
					tag = TAG_BLOCK
					static = True
					color = "darkgray"

				if cell == "D": 
					tag = TAG_DRAGGABLE
					drag = True
					color = "brown"
					
				if cell == "K":
					tag = TAG_KEY
					collectable = True
					color = "orange"

				if cell == "E":
					tag = TAG_ENERGIA
					color = "yellow"
				
				if cell == "C":
					tag = TAG_CLOCK
					color = "blue"
				

				tile = Tile((i * 32 + 16, j * 32 + 16), color, tag)
				# print(self.tiles)
				self.tiles.add(tile)

	def draw_map(self):
		for tile in self.world_map:
			print(tile)
			# pg.draw.rect(self.screen, "darkgray", (pos[0] * 32, pos[1] * 32, 32, 32))
			# self.tiles.add(tile)
		self.tiles.draw()

