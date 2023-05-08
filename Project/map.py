import pygame as pg
from settings import *
from tile import *
from box import Box
from button import Button

class Ray(pg.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pg.surface.Surface((2,2))
		# self.image.fill("black")
		self.rect = self.image.get_rect(center = pos)

class Map():
	def __init__(self, screen, current_map):
		self.map = current_map
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
				cell_pos = ((i * TILESIZE + TILESIZE / 2) + MAP_X_OFFSET, (j * TILESIZE + TILESIZE / 2) + MAP_Y_OFFSET)
				
				if("D" in cell):				
					deg = 0
					if(cell == "DT"): 
						deg = -90
					elif(cell == "DB"):
						deg = 90
					elif(cell == "DR"):
						deg = 180

					tile = Tile(cell_pos, TAG_DOOR, ["door", "door_open"], deg)
					self.door.add(tile)

				elif(cell == "P"):
					self.player_pos = cell_pos
				
				elif(cell == "B"):
					tile = Box(cell_pos, TAG_DRAGGABLE, ["box"])
					self.box_tiles.add(tile)
				
				elif("T" in cell):
					hole_pos = ((int(cell[2]) * TILESIZE + TILESIZE / 2) + MAP_X_OFFSET, int(cell[3]) * TILESIZE + TILESIZE / 2 + MAP_Y_OFFSET)
					hole_tile = Tile(hole_pos, TAG_HOLE, ["hole"])
					button_tile = Button(cell_pos, TAG_BUTTON, ["button", "button_pressed"], hole_tile)
					self.tiles.add(hole_tile)
					self.tiles.add(button_tile)
						
				else: 
					if(cell != " " and cell != "D" and cell != "" and cell != "H"):	
						tile = self.choose_tile(cell, cell_pos)
						self.tiles.add(tile)

	def create_floor(self, current_map):
		for j, row in enumerate(current_map):
			for i, cell in enumerate(row):
				tag = "floor"
				pos = ((i * TILESIZE + TILESIZE / 2) + MAP_X_OFFSET, j * TILESIZE + TILESIZE / 2 + MAP_Y_OFFSET)
				tile = Tile(pos, tag, ["floor", "floor_bright"])
				self.floor_tiles.add(tile)

	def choose_tile(self, cell, cell_pos):
		tag = ""
		files = []
			
		if(cell == "X"):
			tag = TAG_BLOCK
			files = ["block"]
		
		if(cell == "E"):
			tag = TAG_ENERGIA
			files = ["light"]
		
		if(cell == "C"):
			tag = TAG_CLOCK
			files = ["clock"]
		
		if(cell == "K"):
				tag = TAG_KEY
				files = ["key"]
		
		# if("H" in cell):
		# 	tag = "Hole"
		# 	files = ["hole"]


		tile = Tile(cell_pos, tag, files)
		return tile

	# Check Collision
	def check_box_collision_with_wall(self):
		block_tiles = [tile for  tile in self.tiles if tile.tag == TAG_BLOCK]
		collidiable_tiles = pg.sprite.Group()
		collidiable_tiles.add(block_tiles)
		collidiable_tiles.add(self.box_tiles)

		for tile in self.box_tiles:
			local_rays = pg.sprite.Group()
				
			ray_right = Ray((tile.rect.right + 1, tile.rect.center[1]))
			ray_left = Ray((tile.rect.left - 1, tile.rect.center[1]))
			ray_top = Ray((tile.rect.center[0], tile.rect.top - 1))
			ray_bottom = Ray((tile.rect.center[0], tile.rect.bottom + 1))

			local_rays.add(ray_right)
			local_rays.add(ray_left)
			local_rays.add(ray_top)
			local_rays.add(ray_bottom)

			collided_right =  pg.sprite.spritecollide(ray_right, collidiable_tiles, False)
			collided_left =  pg.sprite.spritecollide(ray_left, collidiable_tiles, False)
			collided_top =  pg.sprite.spritecollide(ray_top, collidiable_tiles, False)
			collided_bottom =  pg.sprite.spritecollide(ray_bottom, collidiable_tiles, False)

			if(collided_right):
				tile.rays["right"] = True
			else:
				tile.rays["right"] = False

			if(collided_left):
				tile.rays["left"] = True
			else:
				tile.rays["left"] = False

			if(collided_top):
				tile.rays["top"] = True
			else:
				tile.rays["top"] = False

			if(collided_bottom):
				tile.rays["bottom"] = True
			else:
				tile.rays["bottom"] = False
			
			local_rays.draw(self.screen)
			

	def check_box_collision_with_button(self):
		tiles_collided = pg.sprite.groupcollide(self.tiles, self.box_tiles, False, False)
		buttons_collided = [button for button in tiles_collided if button.tag == TAG_BUTTON] # [0] button, [1] box

		if(len(buttons_collided) > 0):
			buttons_collided[0].toogle_gate(True)
	
	def draw_map(self, display_surface):
		self.floor_tiles.draw(display_surface)
		self.tiles.draw(display_surface)
		self.door.draw(display_surface)
		self.box_tiles.draw(display_surface)

	def update(self):
		self.check_box_collision_with_wall()
		self.check_box_collision_with_button()
