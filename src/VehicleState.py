import numpy


class VehicleState:
    def update(self, vehicle):
        vehicle.position = numpy.add(vehicle.position, vehicle.velocity)

    def activate(self, vehicle):
        pass


class Idle(VehicleState):
    def activate(self, vehicle):
        vehicle.velocity = numpy.array([0, 0])


class Accelerating(VehicleState):
    def update(self, vehicle):
        super().update(vehicle)
        vehicle.velocity = numpy.add(vehicle.velocity, vehicle.acceleration)


class Braking(VehicleState):
    def update(self, vehicle):
        super().update(vehicle)
        vehicle.velocity = numpy.add(vehicle.velocity, numpy.array([-0.01, 0.0]))
        magnitude = numpy.linalg.norm(vehicle.velocity)
        if magnitude <= 0:
            vehicle.set_state(Idle())
