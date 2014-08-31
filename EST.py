from numpy import *
def triangle_area(base=None, height=None, side_a=None, side_b=None, side_c=None):
    """
    I am to calculate area of triangle from two perspective
    :param base: base of triangle
    :param height: height of triangle
    :param side_a:side_a of the triangle
    :param side_b: side_b of the triangle
    :param side_c: side_c of the triangle
    :return:Area of triangle
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
            return sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
        else:
            return"The sum of two sides must be greater than the third side of a triangle"
    else:
        return "no such triangle"


if __name__ == "__main__":
    print("area:", triangle_area(10))
