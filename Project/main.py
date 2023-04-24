import pygame as pg
import sys # to quit the game loop correctly
from settings import *
from player import *
from tile import *
from map import *
from ui import *

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.new_game()
  
	# start core objects of the game
	def new_game(self):
		# map
		self.map = Map(self.screen)

		# player 
		self.player = pg.sprite.GroupSingle()
		self.player.add(Player(self.screen, (400, 400)))
		self.playerRef = self.player.sprite
		pg.time.set_timer(pg.USEREVENT, 1000)

		# map
		self.drag_objects = self.map.tiles

		# game
		self.time = 60

		# ui
		self.ui = pg.sprite.Group()
		key_text = Text((80, 20), "chaves: 0")
		clock_text = Text((200, 20), "tempo: 60")
		energia_text = Text((400, 20), "energia: 10")
		self.ui.add(key_text)
		self.ui.add(clock_text)
		self.ui.add(energia_text)

		self.clock = pg.time.Clock()
	
	# Check the events of the game
	def check_events(self):
			events = pg.event.get()

			for event in events:
				# Handle the exit of the game
				if(event.type == pg.QUIT):
						pg.quit()
						sys.exit()
				if(event.type == pg.USEREVENT):
					self.playerRef.time -= 1

	# Draw everything on screen
	def draw(self):
			self.screen.fill("black")
			# self.map.draw_map(self.screen)
			self.drag_objects.draw(self.screen)
			self.player.draw(self.screen)
			self.ui.draw(self.screen)
	
	def update(self):
		self.player.update(self.drag_objects)
		self.ui.sprites()[0].update(f"Keys {self.playerRef.key}")
		self.ui.sprites()[1].update(f"Tempo {self.playerRef.time}")
		self.ui.sprites()[2].update(f"Energia {self.playerRef.energia}")
		pg.display.update()
		self.clock.tick(FPS)
	
	# Main Loop of the game
	def run(self):
			while True:
					self.check_events()
					self.update()
					self.draw()

	def printa(self):
		print(self.time)

if __name__ == "__main__":
		game = Game() # Create a object of the game class
		game.run()
