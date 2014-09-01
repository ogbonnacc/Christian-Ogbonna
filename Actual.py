__author__ = 'christian'
from pylab import*

from geom_formulae import*
#$$$$$$$$$$$$$$$$$$$$$$I plotted a rectangle_area with fixed breadth$$$$$$$$$$$$$$$$$$$$$$
v_rectangle_area = np.vectorize(rectangle_area)
#v_circle_perimeter = np.vectorize(circle_perimeter)

S = np.linspace(0, 10)  # our side lengths

A = v_rectangle_area(S, 6)  # the areas
#P = v_circle_perimeter(S)  # the perimeters

plot(S, A, '-b', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('rectangle Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$sphere_surface_area plot$$$$$$$$$$$$$$$$$$$$$$$$$$$$
v_sphere_surface_area = np.vectorize(sphere_surface_area)
#v_circle_perimeter = np.vectorize(circle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = v_sphere_surface_area(S)  # the areas
#P = v_circle_perimeter(S)  # the perimeters

plot(S, A, '-g', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('sphere Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$circle_area (geo-plot) $$$$$$$$$$$$$$$$$$$$$$$$$$$$

v_circle_area = np.vectorize(circle_area)
#v_circle_perimeter = np.vectorize(circle_perimeter)

S = np.linspace(0, 10)  # our side lengths

A = v_circle_area(S)  # the areas
#P = v_circle_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('radius')
ylabel('geo values')
title('circle Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$triangle_area Geo plot with varying height $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
v_triangle_area = np.vectorize(triangle_area)
#v_circle_perimeter = np.vectorize(circle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = triangle_area(10, S)  # the areas
#P = v_circle_perimeter(S)  # the perimeters

plot(S, A, '-h', label="Area")
#plot(S, P, ':b', label="Perimeter")

xlabel('height')
ylabel('geo values')
title('sphere Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$GEO VALUES FOR A SEMI_CIRCLE PERIMETER$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#v_triangle_area = np.vectorize(triangle_area)
v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

#A = triangle_area(10, S)  # the areas
P = semicircle_perimeter(S)  # the perimeters

#plot(S, A, '-h', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('radius')
ylabel('geo values')
title('semicircle Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$$$$$CYLINDER GEO_VALUES WITH FIXED HEIGHT################################
v_cylinder_volume = np.vectorize(cylinder_volume)
#v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = cylinder_volume(S, 10)  # the volume
#P = semicircle_perimeter(S)  # the perimeters

plot(S, A, '-b', label="Volume")
#plot(S, P, ':b', label="Perimeter")

xlabel('radius')
ylabel('geo values')
title('cylinder Geo Properties')
legend(loc='upper right')
#$$$$$$$$$$$$$$$$$$$$$$$$$CUBE_SURFACE_AREA GEO_PROPERTIES$$$$$$$$$$$$$$$
v_cube_surface_area = np.vectorize(cube_surface_area)
#v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = cube_surface_area(S)  # the volume
#P = semicircle_perimeter(S)  # the perimeters

plot(S, A, '-r', label="surface_area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('cube Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$$$$$$$$TRAPEZIUM AREA GEO_PROPERTIES WITH VARYING LENGTH$$$$$$$$$$

v_trapezium_area = np.vectorize(trapezium_area)
#v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = trapezium_area(S, 10, 10)  # the volume
#P = semicircle_perimeter(S)  # the perimeters

plot(S, A, '-b', label="trapezium_area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('trapezium Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$CUBOID GEO_PROPERTIES WITH VARYING LENGTH$$$$$$$$$$$$$$$$$$$

v_cuboid_surface_area = np.vectorize(cuboid_surface_area)
#v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = cuboid_surface_area(S, 10, 10)  # the volume
#P = semicircle_perimeter(S)  # the perimeters

plot(S, A, '-b', label="cuboid_surface_area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('cuboid Geo Properties')
legend(loc='upper right')

#$$$$$$$$$$$$$$$$$$$SQUARE_PYRAMID GEO_PROPERTIES$$$$$$$$$$$$$$$$$
v_square_pyramid_surface_area = np.vectorize(square_pyramid_surface_area)
#v_semicircle_perimeter = np.vectorize(semicircle_perimeter)
S = np.linspace(0, 10)  # our side lengths

A = square_pyramid_surface_area(S, 10,)  # the volume
#P = semicircle_perimeter(S)  # the perimeters

plot(S, A, '-b', label="square_pyramid_surface_area")
#plot(S, P, ':b', label="Perimeter")

xlabel('length')
ylabel('geo values')
title('square_pyramid Geo Properties')
legend(loc='upper right')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$GEO_PROPERTIES FOR A SEGMENT AREA WITH VARYING RADIUS$$$$$$$$$$$$$$$$$$$$$
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


