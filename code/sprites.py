import os
from random import choice, randint

import pygame
from settings import *


class BG(pygame.sprite.Sprite):
	def __init__(self,groups,scale_factor):
		super().__init__(groups)
		bg_image = pygame.image.load(os.path.join('graphics', 'background.png')).convert()

		full_height = bg_image.get_height() * scale_factor
		full_width = bg_image.get_width() * scale_factor
		full_sized_image = pygame.transform.scale(bg_image,(full_width,full_height))
		
		self.image = pygame.Surface((full_width,full_height * 2))
		self.image.blit(full_sized_image,(0,0))
		self.image.blit(full_sized_image,(0,full_height))

		self.rect = self.image.get_rect(topleft = (0,0))
		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self,dt):
		self.pos.y -= 300 * dt
		if self.rect.centery <= 0:
			self.pos.y = 0
		self.rect.y = round(self.pos.y)

class Plane(pygame.sprite.Sprite):
	def __init__(self,groups,scale_factor):
		super().__init__(groups)

		# image 
		self.import_frames(scale_factor)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

		# rect
		self.rect = self.image.get_rect(midtop = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 20))
		self.pos = pygame.math.Vector2(self.rect.topleft)

		# movement
		self.gravity = 600
		self.direction = 0

		# mask
		self.mask = pygame.mask.from_surface(self.image)


	def import_frames(self,scale_factor):
		self.frames = []
		for i in range(3):
			surf = pygame.image.load(os.path.join('graphics', 'red0.png')).convert_alpha()
			scaled_surface = pygame.transform.scale(surf,pygame.math.Vector2(surf.get_size())* scale_factor)
			self.frames.append(scaled_surface)

	def apply_gravity(self,dt):
		self.direction += self.gravity * dt
		self.pos.y += self.direction * dt
		self.rect.y = round(self.pos.y)

	def jump(self):
		# self.jump_sound.play()
		self.direction = -400

	def animate(self,dt):
		self.frame_index += 10 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def rotate(self):
		rotated_plane = pygame.transform.rotozoom(self.image,-self.direction * 0.06,1)
		self.image = rotated_plane
		self.mask = pygame.mask.from_surface(self.image)

	def update(self,dt):
		self.apply_gravity(dt)
		self.animate(dt)
		self.rotate()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,groups,scale_factor):
		super().__init__(groups)
		self.sprite_type = 'obstacle'

		orientation = choice(('left','right'))
		surf = pygame.image.load(os.path.join('graphics', '1.png')).convert_alpha()
		self.image = pygame.transform.scale(surf,pygame.math.Vector2(surf.get_size()) * scale_factor)
		
		y = WINDOW_HEIGHT + randint(40,100)

		if orientation == 'left':
			x = WINDOW_WIDTH + randint(5,100)
			self.rect = self.image.get_rect(midright = (x,y))
		else:
			x = randint(-100,-5)
			self.image = pygame.transform.flip(self.image,True,False)
			self.rect = self.image.get_rect(midleft = (x,y))

		self.pos = pygame.math.Vector2(self.rect.topleft)

		# mask
		self.mask = pygame.mask.from_surface(self.image)

	def update(self,dt):
		self.pos.y -= 300 * dt
		self.rect.y = round(self.pos.y)
		if self.rect.bottom <= -100:
			self.kill()
