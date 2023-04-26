import pygame as pg
from settings import *
from tile import *

class Map():
	def __init__(self, screen):
		self.map = map
		self.world_map = {}
		self.screen = screen
		self.tiles = pg.sprite.Group()
		self.door = pg.sprite.GroupSingle()
		self.create_map()

	def create_map(self):
		# Drawn floor tiles
		self.draw_floor()

		# Drawn Object tiles
		for j, row in enumerate(self.map):
			for i, cell in enumerate(row):
				if(cell == "D"):				
					tile = Tile((i * 32 + 16, j * 32 + 16), "purple", TAG_DOOR)
					self.door.add(tile)
					
				else: 
					if(cell != " " and cell != "D"):	
						tile = self.choose_tile(cell, i, j)
						self.tiles.add(tile)

	def draw_floor(self):
		for j, row in enumerate(self.map):
			for i, cell in enumerate(row):
				color, tag = "#222222", "floor"
				tile = Tile((i * 32 + 16, j * 32 + 16), color, tag)
				self.tiles.add(tile)

	def choose_tile(self, cell, i, j):
		color, tag = "darkgray", ""
			
			
		if(cell == "X"):
			color = "darkgray"
			tag = TAG_BLOCK
									
		if(cell == "B"):
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
		return tile

				
	def draw_map(self):
		self.tiles.draw()

