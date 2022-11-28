# Numerical Integration

## Overview
### 1. Integral using Taylor Series Expansion

Taylor expansion of $$e^{-x^2} = \sum_{k=0}^{\infty} (-1)^k \frac{x^{2k}}{k!}$$
Integrating this gives us, $$\int_0^x e^{-t^2} dt = \sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{(2k+1) \cdot k!}$$
      
      
### 2. Integral using Cubic splines
Suppose $$\int_a^b f(x) dx \sim \int_a^b S(x) dx$$

We know,
$$S_i(x) = \frac{z_i}{6h_i} (t_{i+1} - x)^3 + \frac{z_{i+1}}{6h_i} (x - t_i)^3  + ( \frac{y_{i+1}}{h_i} - \frac{z_{i+1} h_i}{6} ) (x - t_i) + ( \frac{y_i}{h_i} - \frac{z_i h_i}{6} ) (t_{i+1} - x)$$

Integrating $S_i(x)$,

$$ IS_i(x) = \int S_i(x) dx = - \frac{z_i}{6h_i} \frac{1}{4} (t_{i+1} - x)^4 + \frac{z_{i+1}}{6h_i} \frac{1}{4} (x - t_i)^4 + ( \frac{y_{i+1}}{h_i} - \frac{z_{i+1} h_i}{6} ) \frac{1}{2} (x - t_i)^2 - ( \frac{y_i}{h_i} - \frac{z_i h_i}{6} ) \frac{1}{2} (t_{i+1} - x)^2 $$

Therefore, 

$$\int_{t_0}^{t_n} S(x) dx = \sum_{i=0}^{n-1} \int_{t_i}^{t_{i+1}} S_i(x) dx $$

$$\int_{t_0}^{t_n} S(x) dx = \sum_{i=0}^{n-1} IS_i(t_{i+1}) - IS_i(t_{i}) $$
      
     

## Getting started
Inorder to run the code for the following questions taken from *"David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society"*, navigate to this directory (**/Integration/**) and use the instructions that follow:

1. Section 7.2 Qn.1 : Write a program for computing $\int_0^x e^{-t^2} dt$ by summing an appropriate Taylor Series until individual terms fall below $10^{-8}$ in magnitude. Test your program by calculating the values of this integral for $x = 0.0, 0.1, 0.2, ..., 1.0$.
           
           make Qn7_2__1
           
           
2. Section 7.2 Qn.2 : Write a computer program that estimates $\int_a^b f(x) dx$ by $\int_a^b S(x) dx$ where $S$ is the natural cubic spline having knots $a+ih$ and interpolating $f$ at these knots. Here $0 \leq i \leq n$ and $h = (b-a)/n$. First obtain a formula for $$\int_{t_0}^{t_n} S(x) dx$$ starting with Equation (7) in section 6.4 (p.351). Then write the subprogram to compute this. Test your code on these well known integrals: $$\boldsymbol{a.} \frac{4}{\pi} \int_0^1 (1 + x^2)^{-1} dx$$ $$\boldsymbol{b.} \frac{1}{\log{3}} \int_1^3 x^{-1} dx$$
           
           make Qn7_2__2_a 
           
           make Qn7_2__2_b
           
           make Qn7_2__2
           
## References
*David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society*
