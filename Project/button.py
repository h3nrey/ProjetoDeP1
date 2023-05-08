import pygame as pg
from tile import Tile

class Button(Tile):
		def __init__(self, pos, tag, files, gate_rect):
			super().__init__(pos, tag, files)
			self.gate = gate_rect
			self.gate_rect = self.gate.rect
			self.pressed = False
    
		def toogle_gate(self, value):
			if(value == True):
				self.image = self.frames[1]
				self.gate.image.set_alpha(0)
				self.gate.rect = pg.rect.Rect((0,0), (0,0))
				self.pressed = True;
					
			else:
				self.image = self.frames[0]
				self.gate.image.set_alpha(255)
				self.gate.rect = self.gate_rect
				self.pressed = False;
		
		def update(self):
			if(self.pressed):
				print(self.gate.sprite)

             
        
		