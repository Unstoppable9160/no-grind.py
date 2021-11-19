from math import pi


def cube(s):
    """Volume of cube"""
    return s**3


def cuboid(l, b, h):
    """Volume of cuboid"""
    return l*b*h


def sphere(r):
    """Volume of sphere"""
    return (4.0/3.0)*pi*(r**3)
