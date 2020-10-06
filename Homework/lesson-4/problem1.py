###
# Here we are defining aliases for the imports
# usually if I import numpy I would later have to
# do numpy.random to access the random module, however
# as we have defined an alias np, I can just do
# np.random instead which is shorter.
#
# Ensure you have installed numpy and matplotlib
# as per the instructions before running this file.
###
import numpy as np
import matplotlib.pyplot as plt

###
# This function should return a two dimensional list of points
# with shape (N, 2). This means that the first axis has size N,
# and the second axis has size 2 (since our points are in two
# dimensions). If I print this list it should look something like:
#
#    points = get_random_points(3)
#    print(points)
#
# output -> [[-0.2, 0.5], [0.8, 0.9], [-0.8, -0.3]]
#
# This is technically a list of lists, and isn't something we have done
# before. Ask if you need a hint. To do this you should use
# np.random (Documentation here: https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.random.html)
###
def get_random_points(N):
    # your code goes here
    return [[]]

###
# This function takes in a point [x, y] and returns True
# if the point is in the circle and False if it is outside
###
def is_point_in_circle(point):
    # your code goes here
    return True


def estimate_pi(N):
    # your code goes here
    return 0.0

###
# I have implemented a plotting function for you, so don't worry
# about doing anything here. If you have implemented is_point_in_circle
# correctly, this will display all the points color-coded for whether
# or not they are in the circle.
###
def plot_random_points(points):
    points_in_circle = np.array([point for point in points if is_point_in_circle(point)])
    points_outside_circle = np.array([point for point in points if not is_point_in_circle(point)])
    
    plt.scatter(points_in_circle[:,0], points_in_circle[:,1])
    plt.scatter(points_outside_circle[:,0], points_outside_circle[:,1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

###
# This function will plot the accuracy of your estimate as a function of N.
# Again, I have implemented this function already. You don't have to add any
# code here.
###
def plot_accuracy():
    Ns = [10**i for i in range(2,8)]
    pis = [estimate_pi(N) for N in Ns]
    plt.loglog(Ns, pis, label="Estimates")
    plt.loglog(Ns, np.pi*np.ones(len(Ns)), label="True value")
    plt.xlabel("N")
    plt.ylabel(r"$\pi$ estimate")
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    # uncomment the following line to plot the accuracy
    # plot_accuracy()

    # this will plot the points to check the accuracy of your
    # is_point_in_circle function. Comment it out if you are
    # testing the accuracy above.
    plot_random_points(get_random_points(10000))
