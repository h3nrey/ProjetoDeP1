from tile import Tile
import pygame as pg

class Box(Tile):
		def __init__(self, pos, color, tag, screen):
			Tile.__init__(self, pos, color, tag)
			self.colliding_point = ""
			self.rays = {
				"left": False,
				"right": False,
				"top": False,
				"bottom": False,
			}