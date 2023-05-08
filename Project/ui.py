import pygame as pg
import os
from main import *
from settings import *
from support import *

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# join the filepath and the filename
filePath = os.path.join(sourceFileDir, 'Graphics/pixel2.ttf');

class Text(pg.sprite.Sprite):
	def __init__(self, pos=(50, 50), text="jorge", fontSize=20, color= "white"):
		super().__init__()
		self.font = pg.font.Font(filePath, fontSize)
		self.color = color
		self.image = self.font.render(text, False, color)
		self.rect = self.image.get_rect(center = pos)

	def update(self, text):
		self.image = self.font.render(str(text), False, self.color)
	

class StatHolder():
	def __init__(self, pos, icon, text):
		super().__init__()
		self.image = GetSurf(["score_holder"])[0]
		self.rect = self.image.get_rect(midleft = pos)
		self.icon = GetSurf([icon])[0]

		self.text = Text((pos[0] + 56, pos[1]), text, 14, C_LIGHT_PURPLE)
		self.text_holder = pg.sprite.GroupSingle()
		self.text_holder.add(self.text)

	def update(self, screen, text = ""):
		screen.blit(self.image, self.rect)
		screen.blit(self.icon, self.rect)

		self.text.update(text)
		self.text_holder.draw(screen)

class ClicableRect():
	def __init__(self, pos, text, callback, *args):
		self.pos = pos
		self.content = text
		self.text = Text(pos, self.content, 20, C_GRAY_BLUE)
		self.normal_size = self.text.image
		self.small_size = pg.transform.scale(self.text.image, (self.text.image.get_size()[0] * 0.8, self.text.image.get_size()[1] * 0.8))
		self.text_el = pg.sprite.Group()
		self.text_el.add(self.text)
		self.callback = callback
		self.args = args
	
	def start_game():
		print("start game")

	def check_collision(self, game):
		mouse_pos = pg.mouse.get_pos()

		if(self.text.rect.collidepoint(mouse_pos)):
			pg.mouse.set_cursor(*pg.cursors.broken_x)
			self.text.image = self.small_size

			if(game.mouse_pressed):
				if(self.args):
					print(f"args: {self.args}")
					self.callback(*self.args)
				else:
					self.callback()
		else:
			pg.mouse.set_cursor(*pg.cursors.arrow)
			self.text.image = self.normal_size

	def draw(self, screen):
		self.text_el.draw(screen)
		
class Ui():
	def __init__(self, screen, game):
		self.screen = screen
		self.elements = pg.sprite.Group()
		
		self.setup_ui()
		self.setup_title_screen(game)
		self.level_transition()
		self.setup_end_screen(game)

		# self.title_screen_image = GetSurf(["title_screen"])[0]
		# self.title_screen_rect = self.title_screen_image.get_rect(topleft = (0,0))

	def level_transition(self):
		# self.transition_text = Text((WIDTH / 2, HEIGHT / 2), "Level 01", 42)
		# self.elements.add(self.transition_text)
		self.bg = pg.Surface((WIDTH, HEIGHT))
		self.bg.fill("black")
		self.bg_rect = self.bg.get_rect(center = (WIDTH / 2, 0))
	
	def update_transition(self):
		if(self.bg_rect.bottom < HEIGHT):
			self.bg_rect.bottom += 5
			self.screen.blit(self.bg, self.bg_rect)
		       
	def setup_ui(self):
		gap = 32
		y_pos = 25
		startX = MAP_X_OFFSET #the space between the start of the screen and the half of the size of the bg
		self.keys_bg = GetSurf(["key_holder"])
		self.keys_bg_rect = self.keys_bg[0].get_rect(midleft = (startX, y_pos))
		self.keys_icon = GetSurf(["key_icon"])[0]

		self.clock_bg = StatHolder((startX + (gap  * 1) + 32, y_pos), "clock_icon",'60')
		self.energia_bg = StatHolder(((startX + 32) + (gap * 2) + (72 * 1), y_pos), "star_icon",'0')
		
	def setup_title_screen(self, game):
		self.title_screen_elements = pg.sprite.Group()
		title = Text((WIDTH / 2, 160), "BRIGHT ANGEL", 36, C_BLUE)
		self.title_screen_elements.add(title)
		self.play_button = ClicableRect((WIDTH / 2, 280), "Jogar", game.start_game)
		self.close_button = ClicableRect((WIDTH / 2, 340), "Sair", game.close_game)

	def draw_tittle_screen(self, game):
		self.title_screen_elements.draw(self.screen)
		self.play_button.draw(self.screen)
		self.play_button.check_collision(game)
		self.close_button.draw(self.screen)
		self.close_button.check_collision(game)
	
	def setup_end_screen(self, game):
		end_text = Text((WIDTH / 2, 100), "Você iluminou", 24, C_BLUE)
		end_text2 = Text((WIDTH / 2, 140), "o mundo novamente", 24, C_BLUE)
		self.play_again_button = ClicableRect((WIDTH / 2, 230), "menu", game.change_current_scene, "menu")
		# end_text = Text((WIDTH / 2, 100), "Você iluminou o mundo novamente", 24, C_BLUE)
		self.end_elements = pg.sprite.Group()
		self.end_elements.add(end_text)
		self.end_elements.add(end_text2)

	def update(self, game):
		if(game.current_scene == SCENE_GAME):
			self.screen.blit(self.keys_bg[0], self.keys_bg_rect)
			self.screen.blit(self.keys_icon, self.keys_bg_rect)
			self.clock_bg.update(self.screen, str(game.playerRef.time))
			self.energia_bg.update(self.screen, str(game.playerRef.energia))


			if(game.playerRef.key > 0): 
				self.keys_icon = GetSurf(["key_found"])[0]

		if(game.current_scene == SCENE_END):
			self.end_elements.draw(self.screen)
			self.play_again_button.draw(self.screen)
			self.play_again_button.check_collision(game)
		self.elements.draw(self.screen)
		# self.update_transition()
