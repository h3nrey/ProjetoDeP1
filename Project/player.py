import pygame as pg
from settings import *
from main import *
from support import *

import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# join the filepath and the filename
filePath = os.path.join(sourceFileDir, 'Graphics/anja.png');

class Player(pg.sprite.Sprite):
	def __init__(self, screen, pos):
		super().__init__()
		self.screen = screen
		self.image = GetSurf("anja")
		# self.image = pg.Surface((PLAYERSIZE, PLAYERSIZE))
		# self.image.fill("yellow")
		print(f"pos: {pos}")
		self.rect = self.image.get_rect(center = pos)
		self.can_move = True;
		self.time = 60

		# movement
		self.dir = pg.math.Vector2(0,0)

		# keys
		self.key = 0

		# energia
		self.energia = PLAYERENERGIA
	
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
		self.can_move = False;

	def collide(self, sprite):
		self.energia += 1
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
		if(self.dir == pg.math.Vector2(1,0)):
			if(box.rays["right"] == False):
				box.rect.left = self.rect.right + 4
			else:
				self.collide(box)

		# Top Collision
		if(self.dir == pg.math.Vector2(0,1)):
			if(box.rays["top"] == False):
				box.rect.top = self.rect.bottom + 4
			else:
				self.collide(box)
			

		# Down Collision
		if(self.dir == pg.math.Vector2(0,-1)):
			if(box.rays["top"] == False):
				box.rect.bottom = self.rect.top - 4
			else:
				self.collide(box)

	def handle_collision(self, sprites, boxes_tiles, door):
		if(door != None):
			if (door.rect.colliderect(self.rect)):
				if(self.key < 1):
					self.collide(door)
				else:
					door.destroy()
				return
		
		for box in boxes_tiles:
			# print(f"box rays {box.rays}")
			if(box.rect.colliderect(self.rect)):
				self.drag(box)

		for sprite in sprites:
			if(sprite.rect.colliderect(self.rect)):

				if(sprite.tag == TAG_BLOCK):
					self.collide(sprite)
					
				else:
					if(sprite.tag == TAG_KEY):
						self.key += 1
						sprite.destroy()

					elif(sprite.tag == TAG_ENERGIA):
						self.energia += 8
						sprite.destroy()
					
					elif(sprite.tag == TAG_CLOCK):
						self.time += 10
						sprite.destroy()

					# elif(sprite.tag == TAG_DOOR):
					# 	sprite.destroy()
	
	def check_if_passed_room(self, event):
		if(self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT):
			self.rect.x = 400
			pg.event.post(event)
			return True
		return False
			
	def update(self, collideSprites, box_tiles, door, event):
		self.check_player_inputs()
		self.handle_collision(collideSprites, box_tiles, door)
		self.check_if_passed_room(event)