import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
	def __init__(self, screen, pos):
		super().__init__()
		self.screen = screen
		self.image = pg.Surface((PLAYERSIZE, PLAYERSIZE))
		self.image.fill("green")
		self.rect = self.image.get_rect(center = pos)

		# movement
		self.dir = pg.math.Vector2(0,0)
	
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
	
	def movement(self):
		x = self.rect[0]
		y = self.rect[1]

		pos_x = x + (self.dir.x * PLAYERSPD)
		pos_y = y + (self.dir.y * PLAYERSPD)
		self.rect.x = pos_x
		self.rect.y = pos_y

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
			# Normal collision
			# if(sprite.is_draggable == False):
			if(sprite.rect.colliderect(self.rect)):
				if(sprite.is_draggable == False):
					self.collide(sprite)
				else:
					self.drag(sprite)
				
			

	def update(self, collideSprites):
		self.check_player_inputs()
		self.movement()
		self.handle_collision(collideSprites)
		pass
		# self.draw(self.screen)
