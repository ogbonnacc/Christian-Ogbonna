from numbers import Number
import numpy as np


def square_perimeter(side : Number) -> Number:
    """
    calculate perimeter of a square from side length.
    :param side: the side length
    :return:the perimeter(same units as side length)
    >>>square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    calculate area of a square from side length.
    :param side: the side length
    :return: the area (units^2 from side)
    square_area(4)
    16
    """
    return side*side


def segment_area(radius, breadth, height, theta1, theta2):
    """

    :param radius: length of one side of sector
    :param breadth: base of triangle
    :param height: height of triangle
    :param theta1: angle of sector
    :param theta2: angle of triangle
    :return:segment area in units^2
    segment_area(10, 12, 8, np.pi/4, np.pi/4)
    5.239
    """

    return ((theta1/360)*np.pi*radius**2) - (0.5*breadth*height*np.sin(theta2))

if __name__ == "__main__":
    sampleRadius = 12
    sampleBreadth = 10
    sampleHeight = 14
    sampleTheta1 = np.pi/4
    sampleTheta2 = np.pi/4
    sampleSide = 12
    print("area:", square_area(sampleSide),"perimeter:",square_perimeter(sampleSide), "area:",
          segment_area(sampleRadius,sampleBreadth, sampleHeight, sampleTheta1, sampleTheta2,))