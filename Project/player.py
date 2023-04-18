import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
	def __init__(self, screen):
		super().__init__();
		self.screen = screen;
		self.image = pg.Surface((10,10));
		self.image.fill("white");
		self.rect = self.image.get_rect(center = (WIDTH / 2, HEIGHT / 2))

		# movement
		self.dir = pg.math.Vector2(0,0);
	
	def check_player_inputs(self):
		pressed  = pg.key.get_pressed()

		if(pressed[pg.K_RIGHT]):
			self.dir = pg.math.Vector2(1,0);
		
		elif(pressed[pg.K_LEFT]):
			self.dir = pg.math.Vector2(-1,0);
		
		elif(pressed[pg.K_UP]):
			self.dir = pg.math.Vector2(0, -1);

		elif(pressed[pg.K_DOWN]):
			self.dir = pg.math.Vector2(0, 1);

		else:
			self.dir = pg.math.Vector2(0,0);
	
	def movement(self):
		x = self.rect[0]
		y = self.rect[1]

		self.rect = (x + (self.dir.x * PLAYERSPD), y + (self.dir.y * PLAYERSPD));

	def update(self):
		self.check_player_inputs();
		self.movement();
		pass;
		# self.draw(self.screen);
