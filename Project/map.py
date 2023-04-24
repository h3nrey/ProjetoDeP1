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
		# Drawn floor tiles
		for j, row in enumerate(self.map):
			for i, cell in enumerate(row):
				color, tag = "#222222", "floor"
				tile = Tile((i * 32 + 16, j * 32 + 16), color, tag)
				self.tiles.add(tile)

		# Drawn Object tiles
		for j, row in enumerate(self.map):
			for i, cell in enumerate(row):
				color, tag = "darkgray", ""

				if(cell != " "):
					
					if(cell == "X"):
						color = "darkgray"
						tag = TAG_BLOCK

					if(cell == "D"):
						color = "#3F1D0B"
						tag = TAG_DRAGGABLE
					
					if(cell == "E"):
						color = "#FFBF00"
						tag = TAG_ENERGIA
					
					if(cell == "C"):
						color = "#6395EC"
						tag = TAG_CLOCK
					
					if(cell == "K"):
						color = "#DFFF7F"
						tag = TAG_KEY


					tile = Tile((i * 32 + 16, j * 32 + 16), color, tag)
					self.tiles.add(tile)

				

				
				

	def draw_map(self):
		for tile in self.world_map:
			print(tile)
			# pg.draw.rect(self.screen, "darkgray", (pos[0] * 32, pos[1] * 32, 32, 32))
			# self.tiles.add(tile)
		self.tiles.draw()

