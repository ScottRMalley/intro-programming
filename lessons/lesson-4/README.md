# Assignment 4

This assignment is slightly different in structure than the previous ones. First read the problem descriptions below and the complete the assignment by completing the functions in the following Python files:
* [Part 1](problem1.py)
* [Part 2](problem2.py)

There are further hints and instructions in the comments of the python files.

## Different ways of calculating the value of <img src="https://latex.codecogs.com/gif.latex?\LARGE&space;\pi" title="\LARGE \pi" />
   
1. The value of <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /> can be calculated by plotting random points on a graph in the range <img src="https://latex.codecogs.com/gif.latex?S&space;=&space;(-1,\&space;1)\times&space;(-1,\&space;1)" title="S = (-1,\ 1)\times (-1,\ 1)" /> and checking whether they are within the unit circle <img src="https://latex.codecogs.com/gif.latex?C" title="C" />. Remember that the unit circle has a radius <img src="https://latex.codecogs.com/gif.latex?r=1" title="r=1" /> and area <img src="https://latex.codecogs.com/gif.latex?A_{circle}=\pi&space;r^2&space;=&space;\pi" title="A_{circle}=\pi r^2 = \pi" />. The area of the square is <img src="https://latex.codecogs.com/gif.latex?A_{square}=2\times&space;2" title="A_{square}=2\times 2" />. Therefore the probability that any random point <img src="https://latex.codecogs.com/gif.latex?P_{x,y}" title="P_{x,y}" /> in <img src="https://latex.codecogs.com/gif.latex?S" title="S" /> is within the circle <img src="https://latex.codecogs.com/gif.latex?C" title="C" /> is:
	
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
2. The equation for a circle in Cartesian coordinates can be expressed as:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;x^2&space;&plus;&space;y^2&space;=&space;r^2" title="\large x^2 + y^2 = r^2" /></div>

	if we solve the above equation for <img src="https://latex.codecogs.com/gif.latex?y" title="y" /> we can express the y-coordinate as a function of <img src="https://latex.codecogs.com/gif.latex?x" title="x" />, ie:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;f(x)&space;=&space;y&space;=&space;\sqrt{r^2&space;-&space;x^2}" title="\large f(x) = y = \sqrt{r^2 - x^2}" /></div>
	
	if we choose <img src="https://latex.codecogs.com/gif.latex?r&space;=&space;1" title="r=1" /> and plot the above function on the interval <img src="https://latex.codecogs.com/gif.latex?[0,\&space;1)" title="[0,\ 1)" /> we get the following graph.

	![Figure 1](images/figure1.png?raw=true "Title")


	We can see immediately that this is the equation for one quadrant of a circle. Knowing that the area of a circle is <img src="https://latex.codecogs.com/gif.latex?\pi&space;r^2" title="\pi r^2" /> and that this represents one quarter of the area of the circle, we can see immediately that since <img src="https://latex.codecogs.com/gif.latex?r&space;=&space;1" title="r=1" /> , the area under this curve should be:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;A_{curve}&space;=&space;\frac{1}{4}A_{circle}&space;=&space;\frac{1}{4}\pi&space;(1)^2&space;=&space;\frac{\pi}{4}" title="\large A_{curve} = \frac{1}{4}A_{circle} = \frac{1}{4}\pi (1)^2 = \frac{\pi}{4}" /></div>

	From calculus, we know that the integral of a function within certain limits is equal to the area under the curve. Therefore, since we already know the area under <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" />  on the interval <img src="https://latex.codecogs.com/gif.latex?[0,\&space;1)" title="[0,\ 1)" />, we also know the value of the integral:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;\int\limits_{0}^{1}&space;\sqrt{1-x^2}\&space;dx&space;=&space;\frac{\pi}{4}" title="\large \int\limits_{0}^{1} \sqrt{1-x^2}\ dx = \frac{\pi}{4}" /></div>
	
	We also know that the average value of a function over a range is equal to the integral of the function divided by that range. More precisely:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;\text{Ave}[f(x)]&space;=&space;\frac{1}{b-a}\int\limits_a^b&space;f(x)\&space;dx" title="\large \text{Ave}[f(x)] = \frac{1}{b-a}\int\limits_a^b f(x)\ dx" /></div>

	For our function on the range <img src="https://latex.codecogs.com/gif.latex?[0,\&space;1)" title="[0,\ 1)" /> the average value is therefore:

	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large\text{Ave}[f(x)]&space;=&space;\frac{1}{1-0}\underbrace{\int_0^1&space;\sqrt{1-x^2}\&space;dx}_{\pi/4}&space;=&space;\frac{1}{1-0}\left(\frac{\pi}{4}&space;\right)&space;=&space;\frac{\pi}{4}" title="\text{Ave}[f(x)] = \frac{1}{1-0}\underbrace{\int_0^1 \sqrt{1-x^2}\ dx}_{\pi/4} = \frac{1}{1-0}\left(\frac{\pi}{4} \right) = \frac{\pi}{4}" /></div>

	This means that if we can estimate an average value for the function we have derived, we can estimate the value of <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /> as:
	
	<div style="text-align:center"><img src="https://latex.codecogs.com/gif.latex?\large&space;\pi&space;=&space;4\times\text{Ave}[f(x)]" title="\large \pi = 4\times\text{Ave}[f(x)]" /></div>

Solutions can be found here:
* [Problem 1 Solution](./solutions/problem1_solution.py)
* [Problem 2 Solution](./solutions/problem2_solution.py)