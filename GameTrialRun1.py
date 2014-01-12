#! /usr/bin/env python

import pygame
import sys
import CreatesLevel
from CreatesLevel import *




black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
blue = (0,0, 255)
green = (0,255,0)

pygame.init()

bullets = pygame.sprite.Group()
clock = pygame.time.Clock()

level1 = Level("level2")
level1.levelCreate(0,0)

player = level1.player
facing = ""
size = [700, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GAME")

#screen.fill(white)


done = False

#clock = pygame.time.Clock()

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				facing = "left"
				player.change_x = -8
			if event.key == pygame.K_RIGHT:
				facing = "right"
				player.change_x = 8
			if event.key == pygame.K_UP:
				player.jump(level1.border)
			
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.change_x=0
			if event.key == pygame.K_RIGHT:
				player.change_x=0
			if event.key == pygame.K_SPACE:
		 		bullet = Bullet(player.rect.x, player.rect.y+10,facing)
				bullets.add(bullet)
				level1.all_sprite.add(bullet)
				
		for bullet in bullets:
			block_hit_list = pygame.sprite.spritecollide(bullet, level1.border, True)
			for block in block_hit_list:
				bullets.remove(bullet)
				level1.all_sprite.remove(bullet)
			if bullet.rect.y >=701 or bullet.rect.y <= 0:
				bullets.remove(bullet)
				level1.all_sprite.remove(bullet)	
	
	bullets.update()	
	player.calc_grav()
	player.update(level1.border)
	
	screen.fill(white)
	level1.all_sprite.draw(screen)
	clock.tick(60)
	pygame.display.flip()
	
pygame.quit()
