import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.radius


# Example usage:
r = float(input("Enter radius: "))
c = Circle(r)

print("Area:", c.area())
print("Circumference:", c.circumference())