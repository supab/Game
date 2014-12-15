import pygame
from pygame.locals import *
from gamelib import SimpleGame


class Meteor(object):
	def __init__(self, radius, color, pos, speed, hp):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.color = color
		self.radius = radius
		self.hp = hp
		self.meteor_image = pygame.image.load('meteor1.png')
		
	def move(self, delta_t,player):
		self.y += 1
		if player.x >= self.x:
			self.x += 1
		elif player.x < self.x:
			self.x -= 1
		if self.y > 30:
			self.y = 30
	def render(self, display):
		pos = (int(self.x),int(self.y))
		#pygame.draw.circle(display, self.color, pos, self.radius/2, 5)
		display.blit(self.meteor_image, (self.x-24, self.y-24))

###################################
class Player(object):
	THICKNESS = 48
	
	def __init__(self, color, pos, height=48):
		(self.x, self.y) = pos
		self.height = height
		self.color = color
		self.ship_image = pygame.image.load('ship1.png')

	def move_left(self):
		self.x -= 10
		if self.x < 0:
			self.x = 0

	def move_right(self):
		self.x += 10
		if self.x > 480:
			self.x = 480
		
	def render(self, display):
		#pygame.draw.rect(display, self.color, pygame.Rect(self.x-self.THICKNESS/2.0, self.y-self.height/2.0, self.THICKNESS, self.height), 3)
		display.blit(self.ship_image, (self.x-24, self.y-24))

###################################
class Bullet(object):
	THICKNESS = 5
	
	def __init__(self, pos, color, speed, height=15):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.height = height
		self.color = color
		
	def move(self, delta_t, player):
		global score, game_over
		
		self.x += self.vx*delta_t
		self.y -= self.vy*delta_t
	
	def render(self, display):
		pygame.draw.rect(display, self.color, pygame.Rect(self.x-self.THICKNESS/2, self.y-self.height/2, self.THICKNESS, self.height), 0)

###################################
class EnemyBullet(Bullet):
	def __init__(self, pos, color, speed, height=15):
		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.height = height
		self.color = color
	def move(self, delta_t, player):
		global score, game_over
		
		self.x += self.vx*delta_t
		self.y += self.vy*delta_t

###################################

class Life(object):
	
	def __init__(self, radius, color, pos):	
		(self.x, self.y) = pos
		self.color = color
		self.radius = radius
		self.life_image = pygame.image.load('life.png')

	def render(self, display):
		pos = (int(self.x),int(self.y))
		#pygame.draw.circle(display, self.color, pos, self.radius, 0)
		display.blit(self.life_image, (self.x-5, self.y-5))