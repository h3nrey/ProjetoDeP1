import pygame as pg
import os

def GetSurf(files):
	# get the directory of this file
	sourceFileDir = os.path.dirname(os.path.abspath(__file__))

	# join the filepath and the filename
	surfs = []
	for file in files:
		# print(f"file: {file}.png")
		file_path = os.path.join(sourceFileDir, f'Graphics/{file}.png');
		surf = pg.image.load(file_path).convert_alpha()
		surfs.append(surf)
	return surfs

def get_file_path(file):
	# get the directory of this file
	source_file_dir = os.path.dirname(os.path.abspath(__file__))

	# join the filepath and the filename
	file_path = os.path.join(source_file_dir, file)
	return file_path