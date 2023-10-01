import math

# Остался непонятым вопрос о том, нужно ли публиковать сделанную библиотеку на PyPi
# Я решил пока этим не заниматься, так как в задании ключевое слово "Напишите ... библиотеку"

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Area calculation not implemented")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        if self.radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Неверно заданы стороны")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        if (
            self.side1 + self.side2 <= self.side3
            or self.side1 + self.side3 <= self.side2
            or self.side2 + self.side3 <= self.side1
        ):
            raise ValueError("Треугольник с такими сторонами не существует")
        s = (self.side1 + self.side2 + self.side3) / 2
        if s==0:
            raise ValueError("Каждая сторона триугольника должна быть более 0")
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        sides.sort()

        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True
        return False