import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt


# helper class to handle functionality for generation of bezier curve from set of points...
class bezier_curve:

    # current location of locus...
    def segment(t, p1, p2):
        q = (1 - t) * p1 + t * p2
        return q

    # points interpolated...
    def interpolated_points(t, points):
        plotpoints = []
        for i in range(0, len(points) - 1):
            plotpoints += [bezier_curve.segment(t, points[i], points[i + 1])]
        return plotpoints

    # return the first point in set...
    def point(t, points):
        plotpoints = points
        while len(plotpoints) > 1:
            plotpoints = bezier_curve.interpolated_points(t, plotpoints)

        return plotpoints[0]

    # generate points of beizer curve...
    def curve_generation(sequence_values, points):
        curve = np.array([[0.0] * len(points[0])])
        for t in sequence_values:
            curve = np.append(curve, [bezier_curve.point(t, points)], axis=0)
        curve = np.delete(curve, 0, 0)
        return curve


# create plot window using matplotlib...
fig = plt.figure(dpi=128, figsize=(5, 5))

# generate numpy array with sequence of numbers from 0-1 at intervals of 0.01...
sequence = np.arange(0, 1, 0.01)


# take input from the user...
number = int(input('Enter the number of points for which bezier curve is to be obtained'))
data_points = []

for i in range(1, number+1):
    xi, yi = map(int, input('Enter x and y coordinate of the point').split())
    data_points.append([xi, yi])


# create a numpy array from given set of points...
given_points = a(data_points)

# plot points on the generated window...
curve_points = bezier_curve.curve_generation(sequence, given_points)

plt.xticks([i for i in range(-100, 100)]), plt.yticks([i for i in range(-100, 100)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

# plot points lying on bezier curve....
plt.plot(curve_points[:, 0], curve_points[:, 1])

# plot initial given points...
plt.plot(given_points[:, 0], given_points[:, 1], 'ro:')

# set title of plot...
plt.title('Bezier Curve')

# save plot locally....
plt.savefig('bezier.png')

# display plot..
plt.show()
