__author__ = 'christian'
from numbers import Number
from numpy import*
def circle_area(radius):
    """

    :param radius:
    :return:
    """
    return pi*radius**2
print(circle_area(2))

def triangle_area(base,height):
    """

    :param base:
    :param height:
    :return:
    """
    return 0.5*base*height
print(triangle_area(10,12))

def cuboid_surfacearea(length,width,heigth):
    """

    :param length:
    :param width:
    :param heigth:
    :return:
    """
    return 2*(length*width+length*heigth+width*heigth)
print(cuboid_surfacearea(4,5,6))

def semicircle_perimeter(radius):
    """

    :param radius:
    :return:
    """
    return pi*radius
print(semicircle_perimeter(7))

def cylinder_volume(radius,height):
    """

    :param radius:
    :param height:
    :return:
    """
    return pi*radius**2*height
print(cylinder_volume(3.5,2))

def cube_surfacearea(height):
    """

    :param height:
    :return:
    """
    return 6*height**2
print(cube_surfacearea(10))

def rectangle_area(length,breadth):
    """

    :param length:
    :param breath:
    :return:
    """
    return length*breadth
print(rectangle_area(12,10))

def sphere_area(radius):
    """

    :param radius:
    :return:
    """
    return 4*pi*radius**2
print(sphere_area(7))
def squarebasedpyramid_surfacearea(length, height):
    """

    :param length:
    :param height:
    :return:
    """
    return length**2+2*length*height
print(squarebasedpyramid_surfacearea(6,8))

def trapezium_area(length,breadth,height):
    """

    :param length:
    :param breadth:
    :param height:
    :return:
    """
    return 0.5*(length+breadth)*height
print(trapezium_area(12,8,6))





