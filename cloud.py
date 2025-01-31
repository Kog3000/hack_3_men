import pygame
import time

class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, right):
        super().__init__()
        img_path1 = 'assets/smoke/smoke1.png'
        self.image1 = pygame.image.load(img_path1)
        self.image1 = pygame.transform.scale(self.image1, (350, 140))

        img_path2 = 'assets/smoke/smoke2.png'
        self.image2 = pygame.image.load(img_path2)
        self.image2 = pygame.transform.scale(self.image2, (350, 140))

        if right:
            self.rect = self.image1.get_rect(midleft=(pos[0] + 80, pos[1] + 40))
        else:
            self.rect = self.image2.get_rect(midright=(pos[0] + 200, pos[1] + 40))

    def animate(self, right):
        if right:
            img_path = 'assets/smoke/smoke1.png'
            self.image = pygame.image.load(img_path)
            self.image = pygame.transform.scale(self.image, (140, 140))
        else:
            img_path = 'assets/smoke/smoke2.png'
            self.image = pygame.image.load(img_path)
            self.image = pygame.transform.scale(self.image, (140, 140))
