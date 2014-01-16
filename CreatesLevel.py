import pygame
import sys
import PlayerClass
from PlayerClass import *

class Border(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image= pygame.Surface([30,30])
		self.image.fill([255,0,0])

		self.rect = self.image.get_rect()
		self.rect.x =x
		self.rect.y =y
		


class Level:
	def __init__(self, blueprint):
		self.level1 =[]
		self.border=pygame.sprite.Group()
		self.all_sprite = pygame.sprite.Group() #list of all sprites
		self.level = open(blueprint, "r")
		self.player_sprite = pygame.sprite.Group()
		self.enemy_sprite = pygame.sprite.Group()
		
	
	def levelCreate(self,x,y):
		#changes the .txt file to a 2d array
		x = 0
		y = 150
		for l in self.level:
			self.level1.append(l)
		
		
		for i in range(len(self.level1)):
			for j in range(len(self.level1[i])):
				if self.level1[i][j] == "X":
					obstacle = Border(x, y)
					self.border.add(obstacle)
					self.all_sprite.add(obstacle)
				if self.level1[i][j] == "1":
					user = Player(x,y)
					self.player = user
					self.all_sprite.add(user)
					self.player_sprite.add(user)
				x += 25
			y+=25
			x=0
	def getSize(self):
		rows =len(self.level1)
		col = len(self.level1[0])
		return [rows*25, col*25]
					
					
			
		

