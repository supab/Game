import pygame
from pygame.locals import *

class SimpleGame(object):
	def __init__(self,title, background_color,window_size = (640,480),fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.background_color = background_color
		self.is_terminated = False
		
	def game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)
		
	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()
			elif event.type == KEYDOWN:
				self.on_key_down(event.key)
			elif event.type ==KEYUP:
				self.on_key_up(event.key)
			# elif event.type == KEYRIGHT:
				# self.on_key_right(event.key)
			# elif event.type ==KEYLEFT:
				# self.on_key_left(event.key)
				
	def terminate(self):
		self.is_terminated = True
	def collisiondetector(self):
		pass
		
	def init(self):
		self.game_init()
		
	def is_key_pressed(self, key):
		keys_pressed = pygame.key.get_pressed()
		if key < 0 or key >= len(keys_pressed):
			return False
		return keys_pressed[key]

	def is_key_down(self, key):
		keys_pressed = pygame.key.get_pressed()
		if key < 0 or key >= len(keys_pressed):
			return False
		if keys_pressed[key] == True:
			return True
		else: 
			return True
	
	def render(self, surface):
		pass
	def update(self):
		pass
	
	def run(self):
		self.init()
		while not self.is_terminated:
			self.__handle_events()
			self.update()
			self.surface.fill(self.background_color)
			self.render(self.surface)
			pygame.display.update()
			self.clock.tick(self.fps)
		print 'Game Over!!!'
		print 'Play Again python game.py'
		print 'Your score is %d' % self.score

	def on_key_up(self, key):
		pass

	def on_key_down(self, key):
		pass
	
	def on_key_left(self, key):
		pass

	def on_key_right(self, key):
		pass