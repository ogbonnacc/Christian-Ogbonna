__author__ = 'christian'
from pylab import*
from numbers import Number
from geom_formulae import*

#def square_perimeter(side : Number) -> Number:
 #   """
  #  Calculate perimeter of a square from side length.

   # @param side: the side length
    #@return: the perimeter (same units as side length)

    #>>> square_perimeter(4)
    #16
    #"""
    #return 4*side


#def square_area(side):
 #   """
  #  Calculate area of a square from side length.
   # @param side: the side length
    #@return: the area (units^2 from side)
    #>>> square_area(4)
    #16
    #"""
    #return side*side

from pylab import *

#from square_geom import *

#v_square_area = np.vectorize(square_area)
#v_square_perimeter = np.vectorize(square_perimeter)

#S = np.linspace(0, 10)  # our side lengths

#A = v_square_area(S)  # the areas
#P = v_square_perimeter(S)  # the perimeters

#plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

#xlabel('side length')
#ylabel('geo values')
#title('Square Geo Properties')
#legend(loc='upper right')

#show()


v_segment_area_area = np.vectorize(segment_area)
#v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = segment_area(S, 10, 10, np.pi/2, np.pi/2)  # the volume
#P = semicircle_perimeter(S)  # the perimeters

plot(S, A, '-b', label="segment_area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('segment_area Geo Properties')
legend(loc='upper right')

show()
