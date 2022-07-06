from math import pi


def square_a(s):
    """Area of square"""
    return s*s


def rectangle_a(l, b):
    """Area of rectangle"""
    return l*b


def circle_a(r):
    """Area of circle"""
    return 2*pi*(r**2)


def cube_v(s):
    """Volume of cube"""
    return s**3


def cuboid_v(l, b, h=None):
    """Volume of cuboid"""
    return l*b*h


def sphere_v(r):
    """Volume of sphere"""
    return (4.0/3.0)*pi*(r**3)
