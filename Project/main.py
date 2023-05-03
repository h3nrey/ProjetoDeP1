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
		self.current_level_index = 0
		self.map = Map(self.screen, MAPS[self.current_level_index])

		# player 
		self.player = pg.sprite.GroupSingle()
		self.player.add(Player(self.screen, self.map.player_pos))
		self.playerRef = self.player.sprite
		pg.time.set_timer(pg.USEREVENT, 1000)

		# objects
		self.tiles = self.map.tiles
		self.boxes = self.map.box_tiles
		self.door = self.map.door

		# game
		self.time = 60

		# custom events
		self.LEVELPASSED = pg.USEREVENT + 1
		self.level_passed_event = pg.event.Event(self.LEVELPASSED)

		# ui
		self.ui = Ui(self.screen)

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

				if(event.type == pg.KEYDOWN):
					if(event.key == pg.K_r):
						self.new_game()

	# Draw everything on screen
	def draw(self):
			self.screen.fill("black")

			self.map.draw_map(self.screen)

			self.player.draw(self.screen)
	
	def update(self):
		self.player.update(self.tiles, self.boxes,self.door.sprite, self.level_passed_event)

		# self.ui.update([
		# 	f"chaves: {self.playerRef.key}", 
		# 	f"tempo: {self.playerRef.time}", 
		# 	f"energia: {self.playerRef.energia}"]
		# )

		self.ui.update([
			f"chaves: {self.playerRef.key}", 
			f"energia: {self.playerRef.energia}"]
		)
		
		self.map.check_tiles_collision()
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
