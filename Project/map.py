import pygame as pg
from settings import *
from tile import *
from box import Box

class Map():
	def __init__(self, screen, current_map):
		self.map = current_map
		self.world_map = {}
		self.screen = screen
		self.tiles = pg.sprite.Group()
		self.floor_tiles = pg.sprite.Group()
		self.box_tiles = pg.sprite.Group()
		self.door = pg.sprite.GroupSingle()
		self.player_pos = (0,0)
		self.create_map(self.map)


	# Create map
	def create_map(self, current_map):
		# clean tiles 
		self.tiles.empty()

		# Drawn floor tiles
		self.create_floor(current_map)

		# Drawn Object tiles
		for j, row in enumerate(current_map):
			for i, cell in enumerate(row):
				cell_pos = (i * TILESIZE + TILESIZE / 2, j * TILESIZE + TILESIZE / 2)
				
				if(cell == "D"):				
					tile = Tile(cell_pos, "purple", TAG_DOOR)
					self.door.add(tile)

				elif(cell == "P"):
					self.player_pos = cell_pos
				
				elif(cell == "B"):
					tile = Box(cell_pos, "purple", TAG_DRAGGABLE, self.screen)
					self.box_tiles.add(tile)
						
				else: 
					if(cell != " " and cell != "D"):	
						tile = self.choose_tile(cell, cell_pos)
						self.tiles.add(tile)

	def create_floor(self, current_map):
		for j, row in enumerate(current_map):
			for i, cell in enumerate(row):
				color, tag = "#222222", "floor"
				tile = Tile((i * TILESIZE + TILESIZE / 2, j * TILESIZE + TILESIZE / 2), color, tag)
				self.floor_tiles.add(tile)

	def choose_tile(self, cell, cell_pos):
		color, tag = "darkgray", ""
			
			
		if(cell == "X"):
			tag = TAG_BLOCK
									
		# if(cell == "B"):
		# 	tag = TAG_DRAGGABLE
		
		if(cell == "E"):
			tag = TAG_ENERGIA
		
		if(cell == "C"):
			tag = TAG_CLOCK
		
		if(cell == "K"):
				tag = TAG_KEY


		tile = Tile(cell_pos, color, tag)
		return tile

	# Check Collision
	def check_tiles_collision(self):
		block_tiles = [tile for  tile in self.tiles if tile.tag == TAG_BLOCK]

		for tile in self.box_tiles:
			for i, block in enumerate(block_tiles):
				ray_left = pg.draw.line(self.screen, pg.Color(0, 0, 0, 0), tile.rect.center, (tile.rect.left - 20, tile.rect.center[1]))
				ray_right = pg.draw.line(self.screen, pg.Color(0, 0, 0, 0), tile.rect.center, (tile.rect.right + 20, tile.rect.center[1]))
				ray_top = pg.draw.line(self.screen, pg.Color(0, 0, 0, 0), tile.rect.center, (tile.rect.center[0], tile.rect.top - 20))
				ray_bottom = pg.draw.line(self.screen, pg.Color(0, 0, 0, 0), tile.rect.center, (tile.rect.center[0], tile.rect.bottom + 20))

				if(ray_left.colliderect(block)): tile.rays["left"] = True
				if(ray_right.colliderect(block)): tile.rays["right"] = True
				if(ray_top.colliderect(block)): tile.rays["top"] = True
				if(ray_bottom.colliderect(block)): tile.rays["bottom"] = True
				
				if(tile.rays["left"] == False and i == len(self.tiles) - 1): 
					tile.rays["left"] = False

				if(tile.rays["top"] == False and i == len(self.tiles) - 1): 
					tile.rays["top"] = False

				if(tile.rays["bottom"] == False and i == len(self.tiles) - 1): 
					tile.rays["bottom"] = False

				if(tile.rays["right"] == False and i == len(self.tiles) - 1): 
					tile.rays["right"] = False
				


	def draw_map(self, display_surface):
		self.floor_tiles.draw(display_surface)
		self.tiles.draw(display_surface)
		self.door.draw(display_surface)
		self.box_tiles.draw(display_surface)

