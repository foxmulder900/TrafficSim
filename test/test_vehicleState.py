from unittest import TestCase

import numpy

from Vehicle import Vehicle
from VehicleState import VehicleState, Idle, Accelerating, Braking


class TestVehicleState(TestCase):
    def test_VehicleState_update_changes_position(self):
        subject = VehicleState()
        vehicle = Vehicle(px=0, py=0, vx=1, vy=2)

        subject.update(vehicle)

        self.assertEqual(vehicle.position[0], 1)
        self.assertEqual(vehicle.position[1], 2)

    def test_Idle_activate_resets_velocity(self):
        subject = Idle()
        vehicle = Vehicle(vx=5, vy=10)

        subject.activate(vehicle)

        self.assertEqual(numpy.linalg.norm(vehicle.velocity), 0)

    def test_Accelerating_update_increases_velocity(self):
        subject = Accelerating()
        vehicle = Vehicle(vx=0, vy=0, ax=1, ay=1)

        subject.update(vehicle)

        self.assertEqual(vehicle.velocity[0], 1)
        self.assertEqual(vehicle.velocity[1], 1)

    def test_Braking_update_decreases_velocity(self):
        subject = Braking()
        vehicle = Vehicle(vx=10, vy=10)

        subject.update(vehicle)

        self.assertEqual(vehicle.velocity[0], 9.99)
        self.assertEqual(vehicle.velocity[1], 10)

    def test_Braking_transitions_to_Idle_when_velocity_is_zero(self):
        subject = Braking()
        vehicle = Vehicle(vx=0, vy=0, state=Idle())

        subject.update(vehicle)

        self.assertEqual(vehicle.state.__class__, Idle)
