import pygame as pg
from settings import *
from main import *


class Player(pg.sprite.Sprite):
	def __init__(self, screen, pos):
		super().__init__()
		self.screen = screen
		self.image = pg.Surface((PLAYERSIZE, PLAYERSIZE))
		self.image.fill("yellow")
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
		# Right Collision
		if(self.dir == pg.math.Vector2(-1,0)):
			self.rect.left = sprite.rect.right
		
		# Left Collision
		if(self.dir == pg.math.Vector2(1,0)):
			self.rect.right = sprite.rect.left

		# Top Collision
		if(self.dir == pg.math.Vector2(0,1)):
			self.rect.bottom = sprite.rect.top

		# Down Collision
		if(self.dir == pg.math.Vector2(0,-1)):
			self.rect.top = sprite.rect.bottom

	def drag(self, sprite):
		# Right Collision
		if(self.dir == pg.math.Vector2(-1,0)):
			sprite.rect.right = self.rect.left
		
		# Left Collision
		if(self.dir == pg.math.Vector2(1,0)):
			sprite.rect.left = self.rect.right

		# Top Collision
		if(self.dir == pg.math.Vector2(0,1)):
			sprite.rect.top = self.rect.bottom

		# Down Collision
		if(self.dir == pg.math.Vector2(0,-1)):
			sprite.rect.bottom = self.rect.top

	def handle_collision(self, sprites):
		for sprite in sprites:
			if(sprite.rect.colliderect(self.rect)):
				if(sprite.tag == TAG_BLOCK):
					self.collide(sprite)
					
				else:
					if(sprite.tag == TAG_DRAGGABLE):
						self.drag(sprite)

					elif(sprite.tag == TAG_KEY):
						self.key += 1
						sprite.destroy()

					elif(sprite.tag == TAG_ENERGIA):
						self.energia += 10
						sprite.destroy()
					
					elif(sprite.tag == TAG_CLOCK):
						self.time += 10
						sprite.destroy()
				
			
	def update(self, collideSprites):
		self.check_player_inputs()
		self.handle_collision(collideSprites)