# Pygame template - skeleton for a new pygame project
import pygame
import random
from settings import * 
import os


class Player(pygame.sprite.Sprite):
	# sprite for the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# every sprite has an image ( character for exp )
		self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
		# in order to ignore the rectangle around the sprite
		self.image.set_colorkey(BLACK)

		# and a rectangle around it 
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH /2 , HEIGHT /2)

		self.y_speed = 5

	def update(self):
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 200:
			self.y_speed = -5
		if self.rect.top < 200:
			self.y_speed = 5

		self.rect.x += 5
		if self.rect.left > WIDTH:
			self.rect.right = 0


# set up assets folders
game_folder = os.path.dirname(__file__)	
img_folder = os.path.join(game_folder, "img")

		
# initialize pygame and create window
pygame.init()
pygame.mixer.init() #for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gameception")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#Game loop
running = True
while running:
	# keep loop running at the right speed
	clock.tick(FPS)
	# Process input ( events )
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
  

	# Update
	all_sprites.update()


	# Draw / render
	screen.fill(BLUE)
	all_sprites.draw(screen)
	# *after* drawing everything, flip the display
	pygame.display.flip()



pygame.quit()
