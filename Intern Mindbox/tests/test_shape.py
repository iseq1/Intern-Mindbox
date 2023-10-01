import pytest
from Mindbox.squareOF import Shape, Circle, Triangle

def test_circle_area():
    circle = Circle(5)
    assert circle.calculate_area() == pytest.approx(78.5398163397)

def test_circle_negative_radius():
    circle = Circle(-5)
    with pytest.raises(ValueError):
        circle.calculate_area()

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.calculate_area() == pytest.approx(6)

def test_triangle_invalid_sides():
    triangle = Triangle(1, 2, 10)
    with pytest.raises(ValueError):
        triangle.calculate_area()

def test_triangle_right_triangle():
    right_triangle = Triangle(3, 4, 5)
    assert right_triangle.is_right_triangle() == True

def test_triangle_not_right_triangle():
    non_right_triangle = Triangle(3, 4, 6)
    assert non_right_triangle.is_right_triangle() == False

def test_circle_zero_radius():
    circle = Circle(0)
    assert circle.calculate_area() == pytest.approx(0)

def test_polygon_calculate_area_not_implemented():
    polygon = Shape()
    with pytest.raises(NotImplementedError):
        polygon.calculate_area()

def test_triangle_invalid_sides_zero():
    with pytest.raises(ValueError):
        triangle = Triangle(1, 0, 2)

def test_triangle_invalid_sides_negative():
    with pytest.raises(ValueError):
        triangle = Triangle(-1, 2, 3)

def test_triangle_right_triangle_hypotenuse_last():
    right_triangle = Triangle(4, 5, 3)
    assert right_triangle.is_right_triangle() == True

def test_triangle_right_triangle_hypotenuse_middle():
    right_triangle = Triangle(3, 5, 4)
    assert right_triangle.is_right_triangle() == True

def test_triangle_right_triangle_hypotenuse_first():
    right_triangle = Triangle(5, 3, 4)
    assert right_triangle.is_right_triangle() == True

def test_triangle_not_right_triangle_obtuse():
    obtuse_triangle = Triangle(1, 2, 3)
    assert obtuse_triangle.is_right_triangle() == False

def test_triangle_not_right_triangle_acute():
    acute_triangle = Triangle(3, 4, 6)
    assert acute_triangle.is_right_triangle() == False