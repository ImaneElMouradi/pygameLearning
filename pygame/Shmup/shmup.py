# Pygame template - skeleton for a new pygame project
import pygame
import random
from os import path
import time



# game options/ settings
TITLE = "Shoot 'em UP!"
WIDTH = 480
HEIGHT = 600
FPS = 60 #fast game


# define colors
WHITE = (255, 255, 255)
BLACK =(0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)


font_name = pygame.font.match_font('arial')


# set up assets folders
img_dir = path.join(path.dirname(__file__), "img") 


def draw_text(surface, color, text, size, x, y ):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, color) #the boolean is weither you want anti-aliased or not True = anti-aliased ( smoother )
	text_rect = text_surface.get_rect()
	text_rect.midtop = ( x, y )
	surface.blit(text_surface, text_rect)









class Player(pygame.sprite.Sprite):
	# sprite for the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# every sprite has an image ( character for exp )
		#self.image = pygame.Surface((50,40))
		self.image = pygame.transform.scale(player_img , (50,38))
		self.image.set_colorkey(BLACK)


 		
 		

		#self.image.fill(GREEN)
		# and a rectangle around it 
		self.rect = self.image.get_rect()

		self.radius = 20
		#pygame.draw.circle(self.image, RED, self.rect.center , self.radius)


		self.rect.centerx = WIDTH /2 
		self.rect.centery = HEIGHT-35
		self.speedx = 0
		self.munition = 50


	def update(self):
		self.speedx = 0
		# to now the exact key pressed ( down ) at that instant
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5
		if keystate[pygame.K_RIGHT]:
			self.speedx = 5

		self.rect.x += self.speedx

		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left <0:
			self.rect.left =0

	def shoot(self, position):
		#position=self.rect.centerx
		bullet = Bullet(position, self.rect.top)
		
		all_sprites.add(bullet)
		bullets.add(bullet)

		keystate = pygame.key.get_pressed()
		

	#def specialShoot(self):
		#if ( self.munition > 0):
			#bullet = Bullet(self.rect.right,self.rect.top)
			#all_sprites.add(bullet)
			#bullets.add(bullet)
			#bullet = Bullet(self.rect.left,self.rect.top)
			#all_sprites.add(bullet)
			#bullets.add(bullet)
			#self.munition -= 2


		
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((30,40))
		self.image_orig = random.choice(meteor_images)
		self.image_orig.set_colorkey(BLACK)

		self.image = self.image_orig.copy()
		#self.image.fill(RED)

		

		self.rect = self.image.get_rect()

		self.radius = int(self.rect.width * .85 /2) 
		#pygame.draw.circle(self.image , RED , self.rect.center , self.radius)

		self.rect.x = random.randrange( 0 , WIDTH - self.rect.width)
		self.rect.y = random.randrange(-150,-100)

		self.speedy = random.randrange(1,8)
		self.speedx = random.randrange(-3,3)

		self.rot = 0 
		self.rot_speed = random.randrange(-8,8)
		self.last_update = pygame.time.get_ticks()


	def rotate(self):
 		now = pygame.time.get_ticks()
 		if now - self.last_update > 50 :
 			self.last_update = 50 
 			#self.image = pygame.transform.rotate(self.image , self.rot_speed) <<< bad way to do it lol
 			self.rot = (self.rot + self.rot_speed) % 360 
 			new_image = pygame.transform.rotate(self.image_orig , self.rot) 
 			old_center = self.rect.center
 			self.image = new_image
 			self.rect = self.image.get_rect()
 			self.rect.center = old_center





	def update(self):
		self.rotate()
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -50 or self.rect.right> WIDTH+50:
			self.rect.x = random.randrange(0,WIDTH - self.rect.width)

			self.rect.y = random.randrange(-100,-40)
			self.speedy = random.randrange(1,8)

			#self.image_orig = random.choice(meteor_images)
			#self.image_orig.set_colorkey(BLACK)


	





class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y): #we want the bullet to spawn at a particular (x,y)
		pygame.sprite.Sprite.__init__(self)
		#self.image = pygame.Surface((10,20))
		#self.image.fill(YELLOW)
		self.image = bullet_img
		self.image.set_colorkey(BLACK)

		self.rect = self.image.get_rect()

		self.rect.bottom = y 
		self.rect.centerx = x 
		self.speedy = -10  #negative so the bullet goes up

	def update(self):
		self.rect.y += self.speedy

		# kill if it moves off the top of the screen 
		if self.rect.bottom < 0 :  
			self.kill()





# initialize pygame and create window
pygame.init()
pygame.mixer.init() #for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# load all game graphics
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(img_dir, "playerShip1_red.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed01.png")).convert()
meteor_images = []
meteor_list = ['meteorBrown_big2.png','meteorBrown_big1.png','meteorBrown_med1.png','meteorBrown_med3.png','meteorBrown_small1.png','meteorBrown_small2.png','meteorBrown_tiny1.png']
for img in meteor_list:
	meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())



all_sprites = pygame.sprite.Group()
#we created mobs(group) which will help with detecting collisi'meteorBrown_big1.png','meteorBrown_big1.png','meteorBrown_big1.png','meteorBrown_big1.png','meteorBrown_big1.png',ons between player and mobs 
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(8):
	m = Mob()
	all_sprites.add(m)
	mobs.add(m)


#Game loop
score=0
running = True
while running:
	# keep loop running at the right speed
	clock.tick(FPS)
	# Process input ( events )
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if player.munition > 0:
					player.shoot(player.rect.centerx)
				
					player.munition -=1

			if event.key == pygame.K_r:
				if player.munition > 0:
					player.shoot(player.rect.right)
					player.shoot(player.rect.left)
				
					player.munition -=2

	# Update
	all_sprites.update()


	# check to see if a bullet h      it a mob 
	
	hits = pygame.sprite.groupcollide(mobs , bullets , True, True)
	for hit in hits:
		score += 60 - hit.radius
		m = Mob()
		all_sprites.add(m)
		mobs.add(m)



	# check to see if a mob hit the player
	hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)  #( sprite , group of sprites you wanna check against, boolean weither the mob in "mobs" hit should be deleted or not) >>> gives a list
	if hits: #if not empty then game over
		running = False


	
	

	# Draw / render 
	#screen.fill(BLACK)
	screen.blit(background, background_rect)
	all_sprites.draw(screen)

	draw_text(screen, WHITE, str(score), 18, WIDTH/2, 10)
	draw_text(screen, WHITE,str(player.munition),20, 50, 0) 

	# *after* drawing everything, flip the display
	pygame.display.flip()


if hits:
	draw_text(screen, RED, "GAME OVER LOSER", 50, WIDTH/2, HEIGHT/2-50)
	pygame.display.update()
	time.sleep(2)


pygame.quit()
