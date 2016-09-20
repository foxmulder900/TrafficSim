import numpy
import pygame

from VehicleState import VehicleState


class Vehicle:
    def __init__(self, px=0, py=0, vx=0, vy=0, ax=1, ay=1, state=VehicleState()):
        self.position = numpy.array([px, py])
        self.velocity = numpy.array([vx, vy])
        self.acceleration = numpy.array([ax, ay])
        self.state = state
        state.activate(self)

    def draw(self, surface):
        self.state.update(self)
        front_position = numpy.add(self.position, [30, 0])
        back_position = numpy.add(self.position, [-30, 0])
        pygame.draw.circle(surface, (125, 253, 254), front_position.astype(int), 10, 3)
        pygame.draw.line(surface, (125, 253, 254), front_position, back_position, 3)
        pygame.draw.circle(surface, (125, 253, 254), back_position.astype(int), 10, 3)

    def set_state(self, state):
        self.state = state
        state.activate(self)
        print('%s is in state: %s' % (self, state.__class__))

    def is_in_state(self, state_class):
        return isinstance(self.state, state_class)
