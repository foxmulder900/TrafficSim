import pygame

from Vehicle import Vehicle
from VehicleState import Accelerating, Braking

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 300])

car = Vehicle(px=60, py=150, ax=0.022, ay=0)
car.set_state(Accelerating())

duration = 5000
start_time = pygame.time.get_ticks()
while pygame.time.get_ticks()-start_time < duration:
    screen.fill((1, 50, 50))

    car.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    if not car.is_in_state(Braking) and pygame.time.get_ticks()-start_time > duration/2:
        car.set_state(Braking())
