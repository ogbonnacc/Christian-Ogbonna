__author__ = 'christian'
from numpy import*
from numbers import Number

def circle_area(radius):
    """

    :param radius:
    :return:
    """
    return pi*radius**2
print(circle_area(2))


def triangle_area(base, height):
    """

    :param base:
    :param height:
    :return:
    """
    return 0.5*base*height
print(triangle_area(10, 12))

def cuboid_surface_area(length, width, height):
    """

    :param length:
    :param width:
    :param height:
    :return:
    """
    return 2*(length*width+length*height+width*height)
print(cuboid_surface_area(4, 5, 6))



def semicircle_perimeter(radius):
    """

    :param radius:
    :return:
    """
    return pi*radius
print(semicircle_perimeter(7))



def cylinder_volume(radius, height):
    """

    :param radius:
    :param height:
    :return:
    """
    return pi*radius**2*height
print(cylinder_volume(3.5, 2))


def cube_surface_area(height):

    """
    :param height:
    :return:
    """
    return 6*height**2
print(cube_surface_area(10))

def rectangle_area(length, breadth):
    """

    :param length:
    :param breadth:
    :return:
    """
    return length*breadth
print(rectangle_area(12, 10))


def sphere_area(radius: Number) -> Number:
    """
    Calculate sphere area.
    @param radius: sphere radius
    @return: sphere volume (in units of radius ^3)

    >>> sphere_area(7)
    132
    """
    return 4*pi*radius**2
print(sphere_area(7))


def square_based_pyramid_surface_area(length, height):
    """

    :param length:
    :param height:
    :return:
    """
    return length**2+2*length*height
print(square_based_pyramid_surface_area(6, 8))


def trapezium_area(length, breadth, height):
    """

    :param length:
    :param breadth:
    :param height:
    :return:
    """
    return 0.5*(length+breadth)*height
print(trapezium_area(12, 8, 6))





