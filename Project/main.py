import pygame as pg
import sys 

from support import *
from settings import *
from player import *
from tile import *
from map import *
from ui import *
from music import *

class Game:
	def __init__(self):
		pg.init()
		self.screen_setup()
		self.current_scene = SCENE_MENU
		self.current_level_index = 0
		self.mouse_pressed = True
		self.audio_handler = AudioSystem()

		# ui
		self.ui = Ui(self.screen, self)

		# custom events
		self.LEVELPASSED = pg.USEREVENT + 1
		self.level_passed_event = pg.event.Event(self.LEVELPASSED)

		self.clock = pg.time.Clock()
		# self.new_game()
	
	def screen_setup(self):
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		game_icon = GetSurf(["anja"])[0]
		pg.display.set_icon(game_icon)
		pg.display.set_caption("Anja Iluminada")
  
	# start core objects of the game
	def new_game(self):
		# map
		self.map = Map(self.screen, MAPS[self.current_level_index])

		# player 
		self.player = pg.sprite.GroupSingle()
		self.player.add(Player(self.screen, self.map.player_pos, self))
		self.playerRef = self.player.sprite
		pg.time.set_timer(pg.USEREVENT, 1000)

		# objects
		self.floor_tiles = self.map.floor_tiles
		self.tiles = self.map.tiles
		self.boxes = self.map.box_tiles
		self.door = self.map.door


		# music
		self.audio_handler.play_calm_music()

		# game
		self.time = 60
	
	def close_game(self):
		pg.quit()
		sys.exit()

	# Check the events of the game
	def check_events(self):
			self.events = pg.event.get()

			for event in self.events:
				# Handle the exit of the game
				if(event.type == pg.QUIT):
						self.close_game()

				if(event.type == pg.USEREVENT):
					if(self.playerRef.time > 0):
						self.playerRef.time -= 1

				if(event.type == self.LEVELPASSED):
					if(self.current_level_index < len(MAPS) - 1):
						self.current_level_index += 1
						self.new_game()
					else:
						self.current_scene = SCENE_END

				if(event.type == pg.KEYDOWN):
					if(event.key == pg.K_r):
						self.new_game()
				
				if(event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
					self.mouse_pressed = True
				else: self.mouse_pressed = False

	# Draw everything on screen
	def draw(self):
			if(self.current_scene == SCENE_GAME):
				self.screen.fill("black")
				self.map.draw_map(self.screen)
				self.player.draw(self.screen)

			elif(self.current_scene == SCENE_MENU):
				self.screen.fill(C_DEEP_PURPLE)
				self.ui.draw_tittle_screen(self)
			
			elif(self.current_scene == SCENE_END):
				self.screen.fill(C_DEEP_PURPLE)
	
	def start_game(self):
		self.change_current_scene(SCENE_GAME)
		self.new_game()
		
	def change_current_scene(self, scene_name):
		# if(self.audio_handler):
		self.current_scene = scene_name
		self.audio_handler.stop_music()
	
	def update(self):
		self.ui.update(self)

		if(self.current_scene == SCENE_GAME):
			self.player.update(self)
			self.map.update()
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
