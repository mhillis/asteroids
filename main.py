# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from sys import exit as sysexit
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
	pygame.init()
	#GROUPS AND CONTAINERS
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	###
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		#Check if asteroid hits player
		for asteroid in asteroids:
			if asteroid.collision(player):
				sysexit("Game over!")
			for shot in shots:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.kill()

		for drawables in drawable:
			drawables.draw(screen)
		pygame.display.flip()

		dt = (clock.tick(60) / 1000)

if __name__=="__main__":
	main()
