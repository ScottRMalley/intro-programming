# Homework 4
## Different ways of calculating the value of <img src="https://latex.codecogs.com/gif.latex?\LARGE&space;\pi" title="\LARGE \pi" />
   
1. The value of <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /> can be calculated by plotting random points on a graph in the range <img src="https://latex.codecogs.com/gif.latex?S&space;=&space;(-1,\&space;1)\times&space;(-1,\&space;1)" title="S = (-1,\ 1)\times (-1,\ 1)" /> and checking whether they are within the unit circle <img src="https://latex.codecogs.com/gif.latex?S" title="S" />. Remember that the unit circle has a radius <img src="https://latex.codecogs.com/gif.latex?r=1" title="r=1" /> and area <img src="https://latex.codecogs.com/gif.latex?A_{circle}=\pi&space;r^2&space;=&space;\pi" title="A_{circle}=\pi r^2 = \pi" />. The area of the square is <img src="https://latex.codecogs.com/gif.latex?A_{square}=2\times&space;2" title="A_{square}=2\times 2" />. Therefore the probability that any random point <img src="https://latex.codecogs.com/gif.latex?P_{x,y}" title="P_{x,y}" /> in <img src="https://latex.codecogs.com/gif.latex?S" title="S" /> is within the circle <img src="https://latex.codecogs.com/gif.latex?C" title="C" /> is:
	
	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;P(P_{x,y}&space;\in&space;C\&space;|\&space;P_{x,y}&space;\in&space;S)&space;=&space;\frac{A_{circle}}{A_{square}}&space;=&space;\frac{\pi}{4}" title="\large P(P_{x,y} \in C\ |\ P_{x,y} \in S) = \frac{A_{circle}}{A_{square}} = \frac{\pi}{4}" /></div>

	This function reads as such: *The probability that a point <img src="https://latex.codecogs.com/gif.latex?P_{x,y}" title="P_{x,y}" /> is within the circle <img src="https://latex.codecogs.com/gif.latex?C" title="C" />  given that it is within the area of the square <img src="https://latex.codecogs.com/gif.latex?S" title="S" /> is equal to the ratio of the areas of <img src="https://latex.codecogs.com/gif.latex?C" title="C" /> and <img src="https://latex.codecogs.com/gif.latex?S" title="S" />*. If we can calculate this probability <img src="https://latex.codecogs.com/gif.latex?P" title="P" /> then we can invert this equation to find the value of <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" />:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;\pi&space;=&space;4P" title="\large \pi = 4P" /></div>

	In order to estimate the value of <img src="https://latex.codecogs.com/gif.latex?P" title="P" /> and consequently the value of <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" />, we can start by randomly generating a list of <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> points in <img src="https://latex.codecogs.com/gif.latex?S" title="S" />, and checking how many are within the circle <img src="https://latex.codecogs.com/gif.latex?C" title="C" /> (we can call this number <img src="https://latex.codecogs.com/gif.latex?N_C" title="N_C" />). The estimated probability then becomes:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;P&space;=&space;\frac{N_C}{N}" title="\large P = \frac{N_C}{N}" /></div>

	which increases in accuracy as the number of sample points <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> increases. Use the package NumPy (Numerical Python) to generate points in the range <img src="https://latex.codecogs.com/gif.latex?(-1,\&space;1)\times&space;(-1,\&space;1)" title="(-1,\ 1)\times (-1,\ 1)" /> and check whether they are in the circle. Remember that a point <img src="https://latex.codecogs.com/gif.latex?P_{x,y}&space;=&space;(x,\&space;y)" title="P_{x,y} = (x,\ y)" /> will be in a circle of radius <img src="https://latex.codecogs.com/gif.latex?r" title="r" /> when:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;x^2&space;&plus;&space;y^2&space;\leq&space;r^2" title="\large x^2 + y^2 \leq r^2" /></div>

	Note: In order to do this problem, you will need to install both `numpy` and `matplotlib`. You can install both of these packages from the command line via:

	```
		pip install numpy
		pip install matplotlib
	```