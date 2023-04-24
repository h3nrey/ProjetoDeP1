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
		self.time = 0
  
	

if __name__ == "__main__":
    game = Game() # Create a object of the game class
    game_instance.run()
