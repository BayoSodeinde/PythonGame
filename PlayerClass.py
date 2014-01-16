import pygame
import sys

class HealthBar(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface([55,5])
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.rect.x = x-20
		self.rect.y = y -10
		self.counter =5
	def update(self,x,y):
		self.rect.x = x-20
		self.rect.y = y -10
		if self.counter ==4:
			self.image.fill((103,199,30))
		if self.counter ==3:
			self.image.fill((234,255,0))
		if self.counter ==2:
			self.image.fill((255,149,0))
		if self.counter ==1:
			self.image.fill((255,0,0))
class Bullet(pygame.sprite.Sprite):

	def __init__(self,x,y,facing,time):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([time*4, time*4])
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.x =x
		self.rect.y =y
		self.facing = facing
	
	def update(self):
		if self.facing == "left":
			self.rect.x -= 24
		elif self.facing == "right":
			self.rect.x +=24
	
class Player(pygame.sprite.Sprite):
	change_x=0
	change_y=0

	jump_ok=False #Set to true if okay to jump

	frame_since_collision =0

	def __init__(self,x,y):
		# do draw
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([10, 25])
		self.image.fill((0,0,0))

		self.rect = self.image.get_rect()
		self.rect.x =x
		self.rect.y =y
		self.health = HealthBar(self.rect.x, self.rect.y)

	def update(self, blocks):

		self.rect.x += self.change_x

		#check to see if hit anything
		any_collision = pygame.sprite.spritecollide(self, blocks, False) #False so nothing disappears
		for block in any_collision:
			if self.change_x >= 0:
				self.rect.right = block.rect.left
			else:
				self.rect.left = block.rect.right

		self.rect.y += self.change_y

		any_collision = pygame.sprite.spritecollide(self, blocks, False)

		for block in any_collision:
			self.frame_since_collision =0

			if self.change_y >=0:
				self.rect.bottom = block.rect.top
				self.jump_ok = True
			else:
				self.rect.top = block.rect.bottom

			self.change_y=0


		if self.frame_since_collision > 3:
			self.jump_ok = False
		
		self.frame_since_collision += 1
		self.health.update(self.rect.x, self.rect.y)

	def calc_grav(self):
		self.change_y += .98 #gravity constant

	def jump(self, blocks):
		if self.jump_ok :
			self.change_y = -18
