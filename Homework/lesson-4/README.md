# Homework 4
## Different ways of calculating the value of <img src="https://latex.codecogs.com/gif.latex?\LARGE&space;\pi" title="\LARGE \pi" />
   
1. The value of <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /> can be calculated by plotting random points on a graph in the range <img src="https://latex.codecogs.com/gif.latex?S&space;=&space;(-1,\&space;1)\times&space;(-1,\&space;1)" title="S = (-1,\ 1)\times (-1,\ 1)" /> and checking whether they are within the unit circle <img src="https://latex.codecogs.com/gif.latex?S" title="S" />. Remember that the unit circle has a radius <img src="https://latex.codecogs.com/gif.latex?r=1" title="r=1" /> and area <img src="https://latex.codecogs.com/gif.latex?A_{circle}=\pi&space;r^2&space;=&space;\pi" title="A_{circle}=\pi r^2 = \pi" />. The area of the square is <img src="https://latex.codecogs.com/gif.latex?A_{square}=2\times&space;2" title="A_{square}=2\times 2" />. Therefore the probability that any random point <img src="https://latex.codecogs.com/gif.latex?P_{x,y}" title="P_{x,y}" /> in <img src="https://latex.codecogs.com/gif.latex?S" title="S" /> is within the circle <img src="https://latex.codecogs.com/gif.latex?C" title="C" /> is:
	
	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;P(P_{x,y}&space;\in&space;C\&space;|\&space;P_{x,y}&space;\in&space;S)&space;=&space;\frac{A_{circle}}{A_{square}}&space;=&space;\frac{\pi}{4}" title="\large P(P_{x,y} \in C\ |\ P_{x,y} \in S) = \frac{A_{circle}}{A_{square}} = \frac{\pi}{4}" /></div>

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