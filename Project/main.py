import pygame as pg
import sys # to quit the game loop correctly
from settings import *
from player import *

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.new_game();
  
	# start core objects of the game
	def new_game(self):
		self.player = pg.sprite.GroupSingle();
		self.player.add(Player(self.screen));
		self.playerRef = self.player.sprite;
		self.clock = pg.time.Clock();
	
	# Check the events of the game
	def check_events(self):
			events = pg.event.get()

			for event in events:
				# Handle the exit of the game
				if(event.type == pg.QUIT):
						pg.quit()
						sys.exit()

	#draw everything on screen
	def draw(self):
			self.screen.fill("black");
			self.player.draw(self.screen);
			pass
	
	def update(self):
		self.player.update();
		pg.display.update();
		self.clock.tick(FPS);
	
	# Main Loop of the game
	def run(self):
			while True:
					self.check_events()
					self.update()
					self.draw()

if __name__ == "__main__":
    game = Game() # Create a object of the game class
    game.run();
