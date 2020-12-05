import numpy as np
import matplotlib.pyplot as plt

###
# Here we want to define the function we will be averaging. Normally, our x
# input would be a list of x values, such as [0.1, 0.3, 0.5, ...], however in
# this case, we want to show the power of a new data type called numpy arrays.
#
# To illustrate the difference between numpy arrays and traditional python
# lists, consider the following example:
#
# >> x = [1, 2, 3]
# >> x_squared = [item**2 for item in x]
# >> print(x_squared)
#        [1, 4, 9]
# >> x = np.array([1, 2, 3])
# >> x_squared = x**2
# >> print(x_squared)
#       array([1, 4, 9])
#
# In this example, we can see that when you are using a numpy array instead of
# a normal python list, we don't have to loop through every element to apply an
# operation. Instead we can just apply the operation to the entire list.
#
# In this function we expect the input to be a numpy array of length N, and we
# want to apply the function to every element of the array without using any
# kind of loop.
# A useful function for this is the numpy square-root function np.sqrt(...)
# Documentation can be found here: https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html
###
def f(x):
    # your code goes here
    return np.array([])

###
# This function should take an integer N and return a numpy array with N
# random numbers between 0 and 1. To do this we can use the np.random module
# Conveniently, every numpy function already returns a numpy array instead of
# a list!
###
def get_random_xs(N):
    # your code goes here
    return np.array([])

###
# This function should take an integer N and return a numpy array with N
# equally spaced values between 0 and 1. For example:
#
# >> xs = get_linear_xs(5)
# >> print(xs)
#        array([0.  , 0.25, 0.5 , 0.75, 1. ])
#
# For this function it would be useful to use the numpy function for sampling
# equally spaced points. See the documentation for np.linspace(...):
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
###
def get_linear_xs(N):
    # your code goes here
    return np.array([])

###
# Here we want to estimate the value of pi using a linear numpy array of size
# N. The input should be an integer N, and the output should be the estimate
# for pi (the data type should be float)
###
def estimate_pi_linear(N):
    # your code goes here
    return 0.0

###
# Here we want to estimate the value of pi using a numpy array with random
# numbers between 0 and 1 of size N. The input should be an integer N, and the
# output should be the estimate for pi (the data type should be float).
###
def estimate_pi_random(N):
    # your code goes here
    return 0.0


###
# This is a plotting method I wrote for you that will compare the two methods
# of estimation. You don't need to add any code here, but this can be run in
# in the main method once the other functions have been completed.
###
def compare_random_vs_linear():
    Ns = np.array([10**n for n in range(3,9)])
    pi_estimate_random = np.array([estimate_pi_random(N) for N in Ns])
    pi_estimate_linear = np.array([estimate_pi_linear(N) for N in Ns])

    plt.loglog(Ns, pi_estimate_random, label='Random Estimate')
    plt.loglog(Ns, pi_estimate_linear, label='Linear Estimate')
    plt.loglog(Ns, np.pi*np.ones(len(Ns)), label='True value')
    plt.legend()
    plt.show()


###
# This is just a test function that will plot your f(x) function. It is useful
# to check whether your f(x) function is returning a proper quarter-circle.
###
def plot_fx():
    x = np.array([xx*0.001 for xx in range(1000)])
    y = f(x)
    plt.plot(x, y, lw=3)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f(x) = \sqrt{1-x^2}$')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


if __name__ == '__main__':
    # The line below can be uncommented if you want to check whether your
    # function is defined properly and plots correctly. If you want to run just
    # this part, comment out the line below with compare_random_vs_linear()
    # plot_fx()
    
    # Here we compare the two methods. If everything is working correctly, the
    # function should show the two lines converging on the true value of pi
    compare_random_vs_linear()
