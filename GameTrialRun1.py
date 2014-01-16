#! /usr/bin/env python

import pygame
import sys
import CreatesLevel
from CreatesLevel import *
import Enemy
from Enemy import *



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
level1.all_sprite.add(player.health)
enemy = Enemy(400,0)
level1.enemy_sprite.add(enemy)
level1.all_sprite.add(enemy)
facing = ""
size = [700, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GAME")

#screen.fill(white)
counter =0

done = False

#clock = pygame.time.Clock()

while done == False:
	counter += 1
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
			if event.key == pygame.K_SPACE:
				start = pygame.time.get_ticks()
			
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.change_x=0
			if event.key == pygame.K_RIGHT:
				player.change_x=0
			if event.key == pygame.K_SPACE:
				end = (int) (pygame.time.get_ticks() - start)/500
				if end > 1:		 		
					bullet = Bullet(player.rect.x, player.rect.y+10,facing,end)
				else:
					bullet = Bullet(player.rect.x, player.rect.y+10, facing, 1)
				bullets.add(bullet)
				level1.all_sprite.add(bullet)


	for bulletz in enemy.enemy_bullet:
		level1.all_sprite.add(bulletz)
				

	
	for bullet in enemy.enemy_bullet:
		hit_player = pygame.sprite.spritecollide(bullet, level1.player_sprite, False)
		for hits in hit_player:
			enemy.enemy_bullet.remove(bullet)
			level1.all_sprite.remove(bullet)
			hits.health.counter -=1
					
	for bullet in bullets:
		block_hit_list = pygame.sprite.spritecollide(bullet, level1.enemy_sprite, False)
		for block in block_hit_list:
			bullets.remove(bullet)
			level1.all_sprite.remove(bullet)
			level1.enemy_sprite.remove(block)
			#check health of enemy
			level1.all_sprite.remove(block)
		if bullet.rect.x >=700 or bullet.rect.x<=0:
			bullets.remove(bullet)
			level1.all_sprite.remove(bullet)
	
	bullets.update()
	if counter%10 ==0:
		enemy.gravity()
		enemy.update(level1.border)	
	player.calc_grav()
	player.update(level1.border)
	
	
	screen.fill(white)
	level1.all_sprite.draw(screen)
	clock.tick(60)
	pygame.display.flip()
	
pygame.quit()
