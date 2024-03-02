from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine stared")

    def stop_engine(self):
        print("Car engine stopped")

class Boat(Vehicle):
    def start_engine(self):
        print("Boat engine started")

    def stop_engine(self):
        print("Boat engine stopped")

def test_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()

car = Car()
boat = Boat()

test_vehicle(car)
test_vehicle(boat)