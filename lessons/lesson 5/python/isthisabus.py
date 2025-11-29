class Vehicle:
    def _init_(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage= mileage
class bus(Vehicle):
    pass
school_bus=Bus("School Volvo", 100, 12)
print("Vehicle Name:", School_bus.name, "speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)