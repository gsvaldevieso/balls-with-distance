import pygame
from pygame.locals import *
from random import *
from math import hypot

class BallsWithDistance:
	_balls_avaible = []
	_width = 800
	_height = 600

	def __init__(self):
		pygame.init()
		self._game_font = pygame.font.SysFont("monospace", 15)
		self.screen = pygame.display.set_mode((self._width, self._height))  	
		self.is_running = 1
		self.init_balls()
		self.main_loop()

	def main_loop(self):
		while self.is_running:
			pygame.time.delay(5)
			self.check_for_collision()
			self.update_balls_movement()
			self.update_surface()
			
			for event in pygame.event.get():
				if event.type == QUIT:
					self.is_running = 0
				else:
				  print event

	def update_surface(self):
		self.screen.fill((120, 120, 120))

		for ball in self._balls_avaible:
			pygame.draw.circle(self.screen, (255,0,0), (ball['x'], ball['y']), ball['radius'])

		self.connects_balls_by_line()

		pygame.display.flip()		

	def quit():
		pygame.quit()
	
	def add_ball(self):
		self._balls_avaible.append({'x': randrange(self._width-100)+1, 'y':randrange(self._height-100)+1, 'velx': randrange(2)+1, 'vely': randrange(2)+1, 'radius': 50})

	def init_balls(self):
		for i in range(0,2):
			self.add_ball()
	
	def check_for_collision(self):
		for ball in self._balls_avaible:
			if ball['x'] + ball['radius'] >= self._width or ball['x'] - ball['radius'] < 0:
				ball['velx'] *= -1
			
			if ball['y'] + ball['radius'] >= self._height or ball['y'] - ball['radius'] < 0:
				ball['vely'] *= -1

	def update_balls_movement(self):
		for ball in self._balls_avaible:
			ball['x'] += ball['velx']
			ball['y'] += ball['vely']

	def connects_balls_by_line(self):
		for ball in self._balls_avaible:
			for other_ball in self._balls_avaible:
				self.draw_distances_text(ball, other_ball)
				pygame.draw.line(self.screen, (255,0,0), (ball['x'], ball['y']), (other_ball['x'], other_ball['y']), 1)

	def draw_distances_text(self, first_ball, second_ball):
			label = self._game_font.render(str(int(self.get_distance_between_two_points(first_ball, second_ball))), 1, (255,255,0))
			self.screen.blit(label, self.midpoint(first_ball, second_ball))

	def get_distance_between_two_points(self, first_ball, second_ball):
		return hypot(second_ball['x'] - first_ball['x'], second_ball['y'] - first_ball['y'])

	def midpoint(self, p1, p2):
		return ((p1['x']+p2['x'])/2, (p1['y']+p2['y'])/2)

bwd = BallsWithDistance()

