from tile import Tile
import pygame as pg

class Box(Tile):
		def __init__(self, pos, tag, files):
			Tile.__init__(self, pos, tag,  files)
			self.colliding_point = ""
			self.rays = {
				"left": False,
				"right": False,
				"top": False,
				"bottom": False,
			}