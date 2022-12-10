import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image.fill(TILE_COLOR)

		self.rect = self.image.get_rect(topleft = pos)

class Tile2(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
		self.image.fill(TILE2_COLOR)

		self.rect = self.image.get_rect(topleft = pos)

class End(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.Surface((TILE_SIZE,TILE_SIZE // 3))
		self.image.fill(END_COLOR)

		self.rect = self.image.get_rect(bottomleft = pos)

class Coin(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)

		self.image = pygame.Surface((TILE_SIZE // 4, TILE_SIZE // 4))
		self.image.fill(COIN_COLOR)

		self.rect = self.image.get_rect(topleft=pos)