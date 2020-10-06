# Homework 4
## Different ways of calculating the value of <a href="https://www.codecogs.com/eqnedit.php?latex=\pi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /></a>
   
1. The value of $\pi$ can be calculated by plotting random points on a graph in the range $S = (-1,\ 1)\times (-1,\ 1)$ and checking whether they are within the unit circle $S$. Remember that the unit circle has a radius $r=1$ and area $A_{circle}=\pi r^2 = \pi$. The area of the square is $A_{square}=2\times 2$. Therefore the probability that any random point $P_{x,y}$ in $S$ is within the circle $C$ is:
   $$P(P_{x,y} \in C\ |\ P_{x,y} \in S) = \frac{A_{circle}}{A_{square}} = \frac{\pi}{4}$$
This function reads as such: *The probability that a point $P_{x,y}$ is within the circle $C$ given that it is within the area of the square $S$ is equal to the ratio of the areas of $C$ and $S$*. If we can calculate this probability $P$ then we can invert this equation to find the value of $\pi$:
	$$\pi = 4P$$
In order to estimate the value of $P$ and consequently the value of $\pi$, we can start by randomly generating a list of $N$ points in $S$, and checking how many are within the circle $C$ ($N_C$). The estimated probability then becomes:
	$$P = \frac{N_C}{N}$$
which increases in accuracy as the number of sample points $N$ increases. Use the package NumPy (Numerical Python) to generate points in the range $(-1,\ 1)\times (-1,\ 1)$ and check whether they are in the circle. Remember that a point $P_{x,y} = (x,\ y)$ will be in a circle of radius $r$ when:
		$$x^2 + y^2 \leq r^2$$
Note: In order to do this problem, you will need to install both `numpy` and `matplotlib`. You can install both of these packages from the command line via:
```
	pip install numpy
	pip install matplotlib
```