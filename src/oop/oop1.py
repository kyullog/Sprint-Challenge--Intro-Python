# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base vehicle class


class Vehicle:
    pass

# ground vehicle, based on vehicle


class GroundVehicle(Vehicle):
    pass

# sub classes for ground vehicle


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# Flight vehicle, based on vehicle class


class FlightVehicle(Vehicle):
    pass

# Flight vehicle subclasses


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
