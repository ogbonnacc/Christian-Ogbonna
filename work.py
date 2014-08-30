__author__ = 'christian'
from numbers import Number
import numpy as np
def rectangle_area(length, breadth: Number) -> Number:
    """
    calculate area of rectangle from side length and side breadth.
    :param length: the side length
    :param breadth: the side breadth
    :return: the area (units^2 from length and breadth)
    rectangle_area (6,4)
    24
    """
    return length*breadth



if __name__ == "__main__":
    sampleLength,Breadth = (10,11)
    print("area:", rectangle_area(sampleLength, Breadth))


def sphere_area(radius: Number) -> Number:
        """
        Calculate sphere area from radius
        @param radius: sphere radius
        @return: sphere area (in units of radius ^2)

        >>> sphere_area(7)
        132
        """
        return 4*np.pi*radius**2

if __name__ == "__main__":
    sampleRadius = 12
    print("area:", sphere_area(sampleRadius))

def circle_area(radius: Number) -> Number:
    """
    calculate circle area from radius
    :param radius: circle radius
    :return: circle area (in units of radius^2)
    >>>circle_area(7)
    154
    """
    return np.pi*radius**2

if __name__ == "__main__":
    sampleRadius = 12
    print("area:", circle_area(sampleRadius))


def triangle_area (base, height: Number) -> Number:
    """
    calculate triangle area from base and height
    :param base: the side base
    :param height: the side height
    :return:triangle area(units^2 from base and height)
    >>>triangle_area(2,1)
    1
    """
    return 0.5*base*height

if __name__ == "__main__":
    sampleBase,Height = (6, 8)
    print("area:", triangle_area(sampleBase,Height))

def semicircle_perimeter (radius: Number) -> Number:
    """
    calculate semicircle area from radius
    :param radius: semicircle radius
    :return:semicircle  area( in units of radius)
    >>>semicircle_area (7)
    22
    """
    return np.pi*radius

if __name__ == "__main__":
    sampleRadius = 12
    print("area:", semicircle_perimeter(sampleRadius))

def cylinder_volume (radius,height: Number) -> Number:
    """
    calculate cylinder volume from radius and height
    :param radius: cylinder radius
    :param height: cylinder height
    :return: volume of cylinder in units of (radius, height)^3
    >>>cylinder_volume (3.5,2)
    77
    """
    return np.pi*radius**2*height

if __name__== "__main__":
    sampleRadius,Height = (3,8)
    print("area:", cylinder_volume(sampleRadius,Height))

def cube_surface_area(height: Number) -> Number:
    """
    calculate surface area of a cube
    :param height: height of cube
    :return:surface area of cube in units of height^2
    >>>cube_surface_area(10)
    600
    """
    return 6*height**2

if __name__ == "__main__":
    sampleHeight = 12
    print ("area:", cube_surface_area(sampleHeight))

def trapezium_area(length, breadth, height: Number) -> Number:
    """
    calculate area of trapezium from the length, breadth and height
    :param length:length of trapezium
    :param breadth:breadth of trapezium
    :param height: height of trapezium
    :return: area of trapezium in units^2
    >>>trapezium_area(12,8,6)
    60.0
    """
    return 0.5*(length + breadth)*height

if __name__ == "__main__":
    sampleLenght,Breadth,Height =(4,9,12)
    print ("area:", trapezium_area(sampleLenght,Breadth,Height))

def cuboid_surface_area(length, width, height):
    """
     calculate the surface area of a cuboid
    :param length:length of cuboid
    :param width: width of cuboid
    :param height: height of cuboid
    :return: surface area of cuboid in units^2
    >>>cuboid_surface_area(4,5,6)
    148
    """
    return 2*(length*width+length*height+width*height)
if __name__== "__main__":
    sampleLength,Width,Height = (9, 12, 10)
    print("surface_area of cuboid:",cuboid_surface_area(sampleLength, Width, Height))

def square_based_pyramid_surface_area(length, height: Number) -> Number:
    """
    calculate surface_area of square based pyramid
    :param length: length of base
    :param height: height of pyramid
    :return: surface_area of square_based_pyramid
    >>>square_based_pyramid_surface_area (6,8)
    132
    """
    return length**2+2*length*height


if __name__ == "__main__":
    sampleLength, Height = (9, 12)
    print("square_based_pyramid_surface_area:", square_based_pyramid_surface_area(sampleLength, Height))




