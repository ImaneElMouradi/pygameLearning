# ---Platform game !---

import pygame as pg
import random
from settings import * 


class Game: 
	def __init__(self):
		# initialize game window, etc

		pg.init()
		pg.mixer.init() #for sound
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()

		self.running = True

	def new(self):
		all_sprites = pg.sprite.Group()



	def run(self):
		# Game Loop
		
		self.playing = True  # a loop that ticks the clock, checks for events, execute the update, execute the draw 
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()



	def update(self):

		# Game loop - Update
		self.all_sprites.update()
		


	def events(self):
		# Game loop - Events
		for event in pg.event.get():
		# check for closing window
			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False #you stop playing the game you also stop playing the whole program
				self.running = False


	def draw(self):
		# Game loop - draw
		
		# Draw / render
		screen.fill(BLUE)
		all_sprites.draw(screen)
		# *after* drawing everything, flip the display
		pygame.display.flip()



	def show_start_screen(self):
		# game splash/ start screen
		pass


	def show_go_screen(self):
		# game over/continue
		pass


g = Game() # a instance of the game
g.show_start_screen()

while g.running: 
	g.new() 
	g.show_go_screen()

pg.quit()






