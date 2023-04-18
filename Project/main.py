import pygame as pg
import sys # to quit the game loop correctly
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    
    def check_events(self):
        events = pg.event.get()
        for event in events:

            # Handle the exit of the game
            if(event.type == pg.QUIT):
                pg.quit()
                sys.exit()
    
    def draw(self):
        pass

    def update(self):
        pass
    

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game() # Create a object of the game class
    game.run();
