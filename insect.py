import random
import pygame

class Insect(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.count = 0
        self.move_right = True
        super().__init__()
        imgs = ['bloha.png', 'spider.png']
        self.k = random.randint(0, 1)
        img_path = f'assets/insects/{imgs[self.k]}'
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift):
        self.rect.x += x_shift
        self.count += 1
        if self.move_right:
            self.rect.x -= 5
        else:
            self.rect.x += 5
        if self.count > 20:
            self.count = 0
            self.move_right = not self.move_right

