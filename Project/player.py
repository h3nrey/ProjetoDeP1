import pygame as pg
from settings import *
from main import *
from support import *

import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# join the filepath and the filename
filePath = os.path.join(sourceFileDir, 'Graphics/angel.png');

class Player(pg.sprite.Sprite):
	def __init__(self, screen, pos, game):
		super().__init__()
		self.screen = screen
		# self.image = GetSurf("anja")
		self.image = pg.image.load(filePath).convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		self.time = 60
		self.game = game

		# movement
		self.dir = pg.math.Vector2(0,0)
		self.can_move = True;

		# keys
		self.key = 0

		# energia
		self.energia = PLAYERENERGIA

		#states
		# self.can_press = True;
	
	def check_player_inputs(self):
		pressed  = pg.key.get_pressed()

		if(pressed[pg.K_RIGHT]):
			self.dir = pg.math.Vector2(1,0)
		
		elif(pressed[pg.K_LEFT]):
			self.dir = pg.math.Vector2(-1,0)
		
		elif(pressed[pg.K_UP]):
			self.dir = pg.math.Vector2(0, -1)

		elif(pressed[pg.K_DOWN]):
			self.dir = pg.math.Vector2(0, 1)

		else:
			self.dir = pg.math.Vector2(0,0)
			
		
		if(pressed[pg.K_RIGHT] == False and pressed[pg.K_LEFT] == False and pressed[pg.K_UP] == False and pressed[pg.K_DOWN] == False):
			self.can_move = True;
	
		if(pressed[pg.K_RIGHT] == True or pressed[pg.K_LEFT] == True or pressed[pg.K_UP] == True or pressed[pg.K_DOWN] == True):
			self.movement()
	
	def movement(self):
		x = self.rect[0]
		y = self.rect[1]

		pos_x = x + (self.dir.x * PLAYERSPD)
		pos_y = y + (self.dir.y * PLAYERSPD)

		if(self.can_move and self.energia > 0):
			self.rect.x = pos_x
			self.rect.y = pos_y
			self.energia -= 1
			self.game.audio_handler.play_sound(SOUNDS["move"])
		self.can_move = False;

	def collide(self, sprite):
		self.energia += 1
		self.game.audio_handler.play_sound(SOUNDS["collide"])
		
		# Right Collision
		if(self.dir == pg.math.Vector2(-1,0)):
			self.rect.left = sprite.rect.right + 4
		
		# Left Collision
		if(self.dir == pg.math.Vector2(1,0)):
			self.rect.right = sprite.rect.left - 4

		# Top Collision
		if(self.dir == pg.math.Vector2(0,1)):
			self.rect.bottom = sprite.rect.top - 4

		# Down Collision
		if(self.dir == pg.math.Vector2(0,-1)):
			self.rect.top = sprite.rect.bottom + 4

	def drag(self, box):
		# Right Collision
		if(self.dir == pg.math.Vector2(-1,0)):
			if(box.rays["left"] == False):
				box.rect.right = self.rect.left - 4
			else:
				self.collide(box)
			
		
		# Left Collision
		elif(self.dir == pg.math.Vector2(1,0)):
			if(box.rays["right"] == False):
				box.rect.left = self.rect.right + 4
			else:
				self.collide(box)

		# Top Collision
		if(self.dir == pg.math.Vector2(0,1)):
			if(box.rays["bottom"] == False):
				box.rect.top = self.rect.bottom + 4
			else:
				self.collide(box)
			

		# Down Collision
		if(self.dir == pg.math.Vector2(0,-1)):
			if(box.rays["top"] == False):
				box.rect.bottom = self.rect.top - 4
			else:
				self.collide(box)

	def handle_collision(self, tiles, boxes_tiles, door, floor_tiles):
		if(door != None):
			if (door.rect.colliderect(self.rect)):
				if(self.key < 1):
					self.collide(door)
				else:
					door.destroy()
				return
		
		# Floor Tiles
		floor_colliding = pg.sprite.spritecollide(self, floor_tiles, False)
		for tile in floor_colliding:
			tile.update_surf(tile.frames[1])

		# Boxes
		boxes_colliding = pg.sprite.spritecollide(self, boxes_tiles, False);
		for box in boxes_colliding:
			self.drag(box)

		# Tiles
		tiles_colliding = pg.sprite.spritecollide(self, tiles, False)

		for tile in tiles_colliding:
			if(tile.tag == TAG_BLOCK or tile.tag == TAG_HOLE):
					self.collide(tile)
					
			else:
				if(tile.tag == TAG_KEY):
					self.key += 1
					door.update_surf(door.frames[1])
					# print(f"door tiles: {door.frames[1]}")
					tile.destroy()
				
				if(tile.tag == TAG_BUTTON):
					tile.toogle_gate(True)

				elif(tile.tag == TAG_ENERGIA):
					self.energia += 14
					tile.destroy()
				
				elif(tile.tag == TAG_CLOCK):
					self.time += 10
					tile.destroy()
		
		if(len(tiles_colliding) <= 0):
			for tile in tiles:
				if(tile.tag == TAG_BUTTON):
					tile.toogle_gate(False)
	
	def check_if_passed_room(self, event):
		if(
			self.rect.x < MAP_X_OFFSET or 
     	self.rect.x > WIDTH - MAP_X_OFFSET or 
		 	self.rect.y < MAP_Y_OFFSET or 
		 	self.rect.y > HEIGHT - MAP_Y_OFFSET
		):
			self.rect.x = 400
			pg.event.post(event)
			return True
		return False

	def update(self, game):
		self.check_player_inputs()
		self.handle_collision(game.tiles, game.boxes, game.door.sprite, game.floor_tiles)
		self.check_if_passed_room(game.level_passed_event)

		# if(self.energia == 8):
		# 	game.audio_handler.stop_music()
		# 	game.audio_handler.play_excited_music()