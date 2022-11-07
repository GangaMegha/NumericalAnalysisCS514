# Spline Interpolation

## Overview


## Getting started
Inorder to run the code for the following questions taken from *"David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society"*, navigate to this directory (**/Newtons_Secant_Horners/**) and use the instructions that follow:

1. Section 6.4 Qn.7 : Draw a script letter, such as the one shown in Figure 6.7. Then reproduce it with the aid of cubic splines and a plotter. Proceed as follows: Select a modest number of points on the curve, say n = 11. Label these t = 1, 2,... , n. For each point, obtain the corresponding x- and y-coordinates. Then fit $x = S_x(t)$ and $y = S_y(t)$, using cubic spline interpolating functions $S_x$ and $S_y$. This will produce a parametric representation of the original curve. Compute a large number of values of $S_x(t)$ and $S_y(t)$ to give to the plotter. To learn more about how spline curves are used in designing typefaces, the reader should consult Knuth [1979].


![Fig 6.7](/images/Fig6_7.png)

           
           python Spline_Interpolation/Qn6_4__7.py
           
           
2. Section 6.4 Qn.8 : Interpret the results of the following numerical experiment and draw some conclusions.
a. Define p to be the polynomial of degree 20 that interpolates the function $f(x) =(1 + 6x^2)^{-1} at 21 equally spaced nodes in the interval [—1, 1]. Include the endpoints as nodes. Print a table of f(x), p(x), and f(x) — p(x) at 41 equally spaced points on the interval.
b. Repeat the experiment using the Chebyshev nodes given by $$x_i = cos[(i - 1)\pi/20] \quad \quad (1 < i < 21) $$
c. With 21 equally spaced knots, repeat the experiment using a cubic interpolating spline
           
           python Spline_Interpolation/Qn6_4__8.py
           



## References
*David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society*
