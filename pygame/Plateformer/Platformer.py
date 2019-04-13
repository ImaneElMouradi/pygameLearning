# Pygame template - skeleton for a new pygame project
import pygame
import random
#import settings
from settings import * 





# initialize pygame and create window
pygame.init()
pygame.mixer.init() #for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


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
	screen.fill(BLACK)
	all_sprites.draw(screen)
	# *after* drawing everything, flip the display
	pygame.display.flip()



pygame.quit()
