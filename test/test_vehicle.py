from unittest import TestCase
from unittest.mock import Mock, ANY

import pygame

import Vehicle
import VehicleState


class TestVehicle(TestCase):

    def test_vehicle_is_initialized_with_zero_position_and_velocity(self):
        subject = Vehicle.Vehicle()

        self.assertEqual(subject.position[0], 0)
        self.assertEqual(subject.position[1], 0)
        self.assertEqual(subject.velocity[0], 0)
        self.assertEqual(subject.velocity[1], 0)

    def test_vehicle_is_initialized_in_base_VehicleState(self):
        subject = Vehicle.Vehicle()

        self.assertIs(subject.state.__class__, VehicleState.VehicleState)

    def test_draw_updates_state(self):
        subject = Vehicle.Vehicle()
        mock_state_update = subject.state.update = Mock()
        pygame.draw.circle = Mock()
        pygame.draw.line = Mock()

        subject.draw(None)

        mock_state_update.assert_called_once_with(subject)

    def test_draws_circle_with_pygame(self):
        subject = Vehicle.Vehicle()
        mock_pygame_draw_circle = pygame.draw.circle = Mock()
        mock_pygame_draw_line = pygame.draw.line = Mock()
        mock_pygame_surface = Mock()

        subject.draw(mock_pygame_surface)

        self.assertEqual(mock_pygame_draw_circle.call_count, 2)
        mock_pygame_draw_circle.assert_called_with(mock_pygame_surface, ANY, ANY, ANY, ANY)
        mock_pygame_draw_line.assert_called_once_with(mock_pygame_surface, ANY, ANY, ANY, ANY)

    def test_set_state_also_activates_state(self):
        subject = Vehicle.Vehicle()
        mock_state = Mock()
        mock_state_activate = mock_state.activate = Mock()

        subject.set_state(mock_state)

        mock_state_activate.assert_called_once_with(subject)

    def test_is_in_state_returns_correctly(self):
        subject = Vehicle.Vehicle(state=VehicleState.Accelerating())

        self.assertTrue(subject.is_in_state(VehicleState.Accelerating))
        self.assertFalse(subject.is_in_state(VehicleState.Idle))
