# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
def main():
	pygame.init()
	#GROUPS AND CONTAINERS
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	#
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		for drawables in drawable:
			drawables.draw(screen)
		pygame.display.flip()

		dt = (clock.tick(60) / 1000)

if __name__=="__main__":
	main()
