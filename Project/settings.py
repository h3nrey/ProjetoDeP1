import pygame as pg

map1 = [
  ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], #0
  ["X", "X", "X", "X", "X", " ", " ", " ", " ", "X"], #1
  ["X", "X", " ", "K", "B", " ", "X", " ", " ", "X"], #2
  ["X", "X", "X", "X", " ", " ", "X", " ", "X", "X"], #3
  ["X", " ", " ", " ", "B", " ", "X", " ", " ", "X"], #4
  ["X", " ", " ", " ", " ", " ", "X", " ", "P", "X"], #5
  ["X", " ", " ", " ", " ", " ", "X", " ", "X", "X"], #6
  ["D", " ", " ", " ", " ", " ", " ", " ", "E", "X"], #7
  ["X", " ", " ", " ", " ", " ", " ", " ", " ", "X"], #8
  ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], #9
]

map2 = [
  ["X", "X", "X", "X", "X", "D", "X", "X", "X", "X"], #0
  ["X", "X", "X", "X", "X", " ", " ", " ", " ", "X"], #1
  ["X", "X", " ", "K", "B", " ", "X", " ", " ", "X"], #2
  ["X", "X", "X", "X", " ", " ", "X", " ", "X", "X"], #3
  ["X", " ", " ", " ", "B", " ", "X", " ", " ", "X"], #4
  ["X", " ", " ", " ", " ", " ", "X", " ", " ", "X"], #5
  ["X", " ", " ", " ", " ", " ", "X", " ", "X", "X"], #6
  ["X", "P", " ", " ", " ", " ", " ", " ", "E", "X"], #7
  ["X", " ", " ", " ", " ", " ", " ", " ", " ", "X"], #8
  ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], #9
]


MAPS = [map1, map2]
# Resolution
TILESIZE = 40
WIDTH = TILESIZE * len(map1[0])
MAP_Y_OFFSET = 50
HEIGHT = 600

# FPS
FPS = 60;

# Player
PLAYERSIZE = 40
PLAYERSPD = TILESIZE
PLAYERENERGIA = 14

# Game tags
TAG_BLOCK = "block"
TAG_DRAGGABLE = "box"
TAG_ENERGIA = "light"
TAG_CLOCK = "clock"
TAG_KEY = "key"
TAG_DOOR = "door"

# Paleta de cores
C_BLUE = "#6CECEC"
C_LIGHT_BLUE = "#6CB9C9"
C_GRAY_BLUE = "#6D85A5"
C_GRAY_PURPLE = "#6E5181"
C_LIGHT_PURPLE = "#6F1D5C"
C_PURPLE = "#4F1446"
C_DARK_PURPLE = "#2E0A30"
C_DEEP_PURPLE = "#0D001A"

