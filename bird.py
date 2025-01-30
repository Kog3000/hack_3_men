import pygame

class Bird(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		img_path = 'assets/birds/bird.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (28, 48))
		self.rect = self.image.get_rect(topleft = pos)

	# update object position due to world scroll
	def update(self, x_shift):
		self.rect.x += x_shift