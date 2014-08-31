__author__ = 'christian'
from numbers import Number
import numpy as np


def rectangle_area(length, breadth: Number) -> Number:
    """
    calculate area of rectangle from side length and side breadth.
    @param length: the side length
    @param breadth: the side breadth
    @return: the area (units^2 from length and breadth)
    rectangle_area (6,4)
    24
    """
    return length*breadth


def sphere_surface_area(radius: Number) -> Number:
        """
        Calculate surface  of sphere area from radius
        @param radius: sphere radius
        @return: sphere area (in units of radius ^2)

        >>> sphere_area(7)
        132
        """
        return 4*np.pi*radius**2


def circle_area(radius: Number) -> Number:
    """
    calculate circle area from radius
    @param radius: circle radius
    @return: circle area (in units of radius^2)
    >>>circle_area(7)
    154
    """
    return np.pi*radius**2


def triangle_area(breadth, height: Number) -> Number:
    """
    calculate triangle area from base and height
    @param breadth: the side breadth
    @param height: the side height
    @return:triangle area(units^2 from base and height)
    >>>triangle_area(2,1)
    1
    """
    return 0.5*breadth*height


def semicircle_perimeter(radius: Number) -> Number:
    """
    calculate semicircle area from radius
    @param radius: semicircle radius
    @return:semicircle  area( in units of radius)
    >>>semicircle_area (7)
    22
    """
    return np.pi*radius + 2*radius


def cylinder_volume(radius, height: Number) -> Number:
    """
    calculate cylinder volume from radius and height
    @param radius: cylinder radius
    @param height: cylinder height
    @return: volume of cylinder in units of (radius, height)^3
    >>>cylinder_volume (3.5,2)
    77
    """
    return np.pi*radius**2*height


def cube_surface_area(length: Number) -> Number:
    """
    calculate surface area of a cube
    @param length: length of cube
    @return:surface area of cube in units of height^2
    >>>cube_surface_area(10)
    600
    """
    return 6*length**2


def trapezium_area(length, width, height: Number) -> Number:
    """
    calculate area of trapezium from the length, breadth and height
    @param length:length of trapezium
    @param width:width of trapezium
    @param height: height of trapezium
    @return: area of trapezium in units^2
    >>>trapezium_area(12,8,6)
    60.0
    """
    return 0.5*(length + width)*height


def cuboid_surface_area(length, width, height):
    """
     calculate the surface area of a cuboid
    @param length:length of cuboid
    @param width: width of cuboid
    @param height: height of cuboid
    @return: surface area of cuboid in units^2
    >>>cuboid_surface_area(4,5,6)
    148
    """
    return 2*(length*width+length*height+width*height)


def square_pyramid_surface_area(length, height: Number) -> Number:
    """
    calculate surface_area of square based pyramid
    @param length: length of base
    @param height: height of pyramid
    @return: surface_area of square_based_pyramid
    >>>square_pyramid_surface_area (6,8)
    132
    """
    return length**2+2*length*height


def segment_area(radius, breadth, height, theta1, theta2):
    """

    @param radius: length of one side of sector
    @param breadth: base of triangle
    @param height: height of triangle
    @param theta1: angle of sector
    @param theta2: angle of triangle
    @return:segment area in units^2
    segment_area(10, 12, 8, np.pi/4, np.pi/4)
    5.239
    """

    return ((theta1/360)*np.pi*radius**2) - (0.5*breadth*height*np.sin(theta2))


def triangle_area(base=None, height=None, side_a=None, side_b=None, side_c=None):
    """
    I am to calculate area of triangle from two perspective
    @param base: base of triangle
    @param height: height of triangle
    @param side_a:side_a of the triangle
    @param side_b: side_b of the triangle
    @param side_c: side_c of the triangle
    @return:Area of triangle
    >>>triangle_area(base=10, height=8)
    40
    For the second method the sum of any two side should be greater than the third.
    >>>triangle_area(side_a=2,side_b=3,side_c=4)
    2.9047
    """
    if (base is not None) & (height is not None):
        return 0.5 * base * height
    elif (side_a is not None) & (side_b is not None) & (side_c is not None):
        if (side_a + side_b) > side_c & (side_b + side_c) > side_a & (side_a + side_c) > side_b:
            s = (side_a + side_b + side_c) * 0.5
            return (s*(s-side_a)*(s-side_b)*(s-side_c)) ** 0.5
        else:
            return"The sum of two sides must be greater than the third side of a triangle"
    else:
        return "no such triangle"


if __name__ == "__main__":
    sampleLength = 6
    sampleRadius = 3
    sampleWidth = 4
    sampleHeight = 8
    sampleBreadth = 12
    sampleTheta1 = np.pi/4
    sampleTheta2 = np.pi/4
    print("area of rectangle:", rectangle_area(sampleLength, sampleBreadth))
    print("surface area of sphere:", sphere_surface_area(sampleRadius))
    print("area of circle:", circle_area(sampleRadius))
    print("area of triangle:", triangle_area(sampleBreadth, sampleHeight))
    print("perimeter of semi_circle:", semicircle_perimeter(sampleRadius))
    print("volume of cylinder:", cylinder_volume(sampleRadius, sampleHeight))
    print("surface_area of cube:", cube_surface_area(sampleLength))
    print("area of trapezium:", trapezium_area(sampleLength, sampleWidth, sampleHeight))
    print("surface_area of cuboid:", cuboid_surface_area(sampleLength, sampleWidth, sampleHeight))
    print("surface_area of square_pyramid:", square_pyramid_surface_area(sampleLength, sampleHeight))
    print("area of segment:",  segment_area(sampleRadius, sampleBreadth, sampleHeight, sampleTheta1, sampleTheta2,))
    print("area:", triangle_area(10))




