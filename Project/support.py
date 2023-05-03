import pygame as pg
import os

def GetSurf(filename):
	# get the directory of this file
	sourceFileDir = os.path.dirname(os.path.abspath(__file__))

	# join the filepath and the filename
	file_path = os.path.join(sourceFileDir, f'Graphics/{filename}.png');
	surf = pg.image.load(file_path).convert_alpha()
	return surf