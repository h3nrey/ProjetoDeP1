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
		pg.display.set_caption("Anja Iluminada")
		self.new_game()
  
	# start core objects of the game
	def new_game(self):
		# map
		self.current_map_index = 0
		self.map = Map(self.screen, MAPS[self.current_map_index])

		# player 
		self.player = pg.sprite.GroupSingle()
		self.player.add(Player(self.screen, self.map.player_pos))
		self.playerRef = self.player.sprite
		pg.time.set_timer(pg.USEREVENT, 1000)

		# objects
		self.drag_objects = self.map.tiles
		self.door = self.map.door

		# game
		self.time = 60

		# custom events
		self.LEVELPASSED = pg.USEREVENT + 1
		self.level_passed_event = pg.event.Event(self.LEVELPASSED)

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
				
				if(event.type == self.LEVELPASSED):
					self.current_map_index += 1
					self.map.create_map(MAPS[self.current_map_index])
					self.playerRef.energia = 20


	# Draw everything on screen
	def draw(self):
			self.screen.fill("black")
			# self.map.draw_map(self.screen)
			self.drag_objects.draw(self.screen)
			self.door.draw(self.screen)
			self.player.draw(self.screen)
			self.ui.draw(self.screen)
	
	def update(self):
		self.player.update(self.drag_objects, self.door.sprite, self.level_passed_event)
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

if __name__ == "__main__":
		game = Game() # Create a object of the game class
		game.run()
