# Spline Interpolation

## Overview


## Getting started
Inorder to run the code for the following questions taken from *"David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society"*, navigate to this directory (**/Newtons_Secant_Horners/**) and use the instructions that follow:

1. Section 6.4 Qn.7 : Draw a script letter, such as the one shown in Figure 6.7. Then reproduce it with the aid of cubic splines and a plotter. Proceed as follows: Select a modest number of points on the
curve, say n = 11. Label these t = 1, 2,... , n. For each point, obtain the corresponding
x- and y-coordinates. Then fit x = Sx(t) and y = Sy(t), using cubic spline interpolating
functions Sx and Sy. This will produce a parametric representation of the original curve.
Compute a large number of values of Sx(t) and Sy(t) to give to the plotter. To learn more
about how spline curves are used in designing typefaces, the reader should consult Knuth
[1979].
![alt text](/Images/Fig6.7.png)
           
           make Qn3_2__3_Newtons
           
           make Qn3_2__3_Secant
           
           
2. Section 3.2 Qn.5 : The equation $2 \cdot x^4 + 24 \cdot x^3 + 61 \cdot x^2 - 16 \cdot x + 1 = 0$ has $2$ roots near 0.1. Determine them by means of Newton's method. Use Horner’s algorithm to compute value of the funciton and it's derivative
           
           make Qn3_2__5   
           
3. Section 3.2 Qn.14b : Using Newton's method, find the roots of the nonlinear systems:
        $$x + e^{-1x} + y^3 = 0$$
        $$x^2 + 2xy - y^2 + tan(x) = 0$$
           
           make Qn3_2__14b


## References
*David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society*
