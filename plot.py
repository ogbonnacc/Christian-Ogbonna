__author__ = 'christian'
from pylab import*
#from square_geom import*
v_square_area = np.vectorize(square_area)
v_square_perimeter = np.vectorize(square_perimeter)

s = np.linspace(0, 10)
A = v_square_area(s)
p = v_square_perimeter(s)

plot (s, A, '-r', label = "Area")
plot (s, p, ':b', label = "perimeter")

xlabel ('side length')
ylabel ('geo values')
title ('square Geo properties')
legend (loc = 'upper right')

show ()

