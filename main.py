import pygame, sys
from settings import *
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3 Богатыря")

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)  # громкость от 0.0 до 1.0

pygame.mixer.music.load('sounds/bg_music.mp3')

pygame.mixer.music.play(-1)

class Platformer:
	def __init__(self, screen, width, height):
		self.screen = screen
		self.clock = pygame.time.Clock()
		self.player_event = False

		self.bg_img = pygame.image.load('assets/terrain/bg1.jpg')
		self.bg_img = pygame.transform.scale(self.bg_img, (width, height))

	def main(self):
		world = World(world_map, self.screen)
		while True:
			self.screen.blit(self.bg_img, (0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif not world.player.sprite.game_over:
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							self.player_event = "left"
						if event.key == pygame.K_RIGHT:
							self.player_event = "right"
						if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
							self.player_event = "space"
						if event.key == pygame.K_w:
							world.attack()
					elif event.type == pygame.KEYUP:
						self.player_event = False
				else:
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							world = World(world_map, self.screen)


			world.update(self.player_event)
			pygame.display.update()
			self.clock.tick(60)


if __name__ == "__main__":
	play = Platformer(screen, WIDTH, HEIGHT)
	play.main()