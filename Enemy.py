import pygame
import PlayerClass
from PlayerClass import *

class Enemy(pygame.sprite.Sprite):
	change_x=0
	change_y=0
	flag = True #keep from going to far down
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([32, 32])
		self.image.fill((200,0,200))
		self.rect = self.image.get_rect()
		self.rect.x =x
		self.rect.y =y
		self.counter = 0
		self.enemy_bullet = pygame.sprite.Group()
	def update(self,blocks):
		facing = "right"
		self.rect.x += self.change_x
		if self.flag == True:		
			self.rect.y += self.change_y
		if self.counter <6:
			self.change_x = .002
			facing = "right"
		else:
			facing = "left"
			self.change_x=-0.002
			if self.counter > 12:
				self.counter =0
			if self.counter == 6:
				bullet = Bullet(self.rect.x, self.rect.y+10, facing,1)
				self.enemy_bullet.add(bullet)
		self.enemy_bullet.update()
		
			
		self.counter +=1
		any_collision = pygame.sprite.spritecollide(self, blocks, False)
		if len(any_collision) == 0:
			self.flag = True
		for block in any_collision:
			if self.change_x >= 0:
				self.rect.right = block.rect.left
			else:
				self.rect.left = block.rect.right
			if self.change_y >=0:
				self.rect.bottom = block.rect.top +1
				self.flag = False

	def gravity(self):
		self.change_y += 2.1

