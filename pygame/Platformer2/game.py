import pygame
import time
import sys
import os


'''
Objects
'''
#python classes and functions
pygame.display.set_mode()

img_player = pygame.image.load(os.path.join('images','hero.png')).convert()

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
    	pygame.sprite.Sprite.__init__(self)
    	self.movex = 0
    	self.movey = 0
    	self.frame = 0 # count frames

    	img_player.convert_alpha()
    	img_player.set_colorkey(ALPHA)
		

    	
    	self.images = []
    	self.images.append(img_player)

    	self.image = self.images[0]
    	

    	self.rect = self.image.get_rect()
    
    def control(self,x,y):
    	'''
    	control player ;ove;ent 
    	'''
    	self.movex += x
    	self.movey += y

    def update(self):
    	'''
    	Update sprite position
    	'''
    	self.rect.x += self.movex
    	self.rect.y += self.movey

    ''' for animation

    # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)+4]
    '''

'''class Enemy(pygame.sprite.Sprite):
	
	Spawn an enemy
	

	def __init__(self,x,y,img):'''




#run-once code
main = True

BLUE  = (25,25,200)
BLACK = (23,23,23)
WHITE = (254,254,254)
ALPHA = (0,0,0)

worldx = 800
worldy = 600

fps = 40 #frame rate
ani = 4  #animation cycles

clock = pygame.time.Clock()
pygame.init()

world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.jpg')).convert()
backdropbox = world.get_rect()


# bring the playerinto the game
player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 400   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 # how many pixels to move/ vitesse



'''
Main Loop
'''
#game loop
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
            	player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
            	player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
            	print("jump")

        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_LEFT or event.key == ord('a'):
        		player.control(steps,0) #to return the sprites momentum back to 0 -> stops
        	if event.key == pygame.K_RIGHT or event.key == ord('d'):
        		player.control(-steps,0)
        	if event.key == ord('q'):
        		pygame.quit()
        		sys.exit()
        		main=False
        	

                


    world.blit(backdrop, backdropbox)
    player.update() # to update visually the player position
    player_list.draw(world) # draw player
    pygame.display.flip()
    clock.tick(fps)


