# Newton-Raphson, Secant Method and Horner's Algorithm

## Overview
### 1. Newton's method
Newton-Raphson iteration can be used to find the zero of a real valued function of a real variable.

For funtion $f(x)$, we can find its zero using the following iteration :

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \quad  ; n>=0$$
      
where $f(x_n)$ is the value of the function at $x_n$ and $f'(x_n)$ is the value of the derivative of $f(x)$ at $x_n$.
      
We can also use it for solving a system of non-linear equations by linearizing it and using matrices.

For example, 

$$f_1(x_1, x_2) = 0$$

$$f_2(x_1, x_2) = 0$$

$$X = \begin{bmatrix}
x_1\\
x_2
\end{bmatrix}$$

$$F(X) = \begin{bmatrix} 
f_1(x_1, x_2) \\ 
f_2(x_1, x_2) \end{bmatrix}$$

$$F'(X) = \begin{bmatrix}
\frac{df_1}{dx_1} & \frac{df_1}{dx_2} \\
\frac{df_2}{dx_1} & \frac{df_2}{dx_2} 
\end{bmatrix}$$

        
We use the iteration :
      
$$X_{n+1} = X_n - F'(X_n)^{-1} \cdot F(X_n)$$
      
      
### 2. Secant Method
Secant method is also used to find the zero of a real valued function of a real variable.

One of the drawbacks of Newton's method is that it involves derivative of the function whose zero is sought. 
To overcome this disadvantage, one of the ways is to use secant method.

For funtion f(x), we can find its zero using the following iteration :
      
$$x_{n+1} = x_n - f(x_n) * \bigg(\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}\bigg) \quad ; n>=1$$
      
      
### 3. Horner's Algorithm

Horner's algorithm is to used to efficiently compute values of a polynomial. 
The method is also known as 'nested multiplcation' or 'synthetic division'.

The algorithm has several usecases. For example : 
1. Given a complex number $z_0$ and polynomial $p$ find the values of $p(z_0)$ and it's derivatives.
2. Find the deflation factors, ie., removing linear factor from polynomial like $p(z) = (z-z_0) \cdot q(z) + r$ by computing $r$
3. Find coefficients of Taylor series expansion of the polynomial $p$ around $z_0$ (complete Horner's algorithm)


Here, given $z_0$ and coefficients of polynomial $p(z) = a_n x^n + a_{n-1} x^{n-1} + ... a_1 x + a_0$ we use Horner's algorithm to compute :
1. $\alpha = p(z_0)$ 
2. $\beta  = p'(z_0)$

by starting with $\alpha = a_n$ and $\beta=0$ and using the following iteration from $k=n-1$ to $0$:
      
$$\beta = \alpha + z_0 \times \beta$$  

$$\alpha = a_k + z_0 \times \alpha$$


## Getting started
Inorder to run the code for the following questions taken from *"David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society"*, navigate to this directory (**/Newtons_Secant_Horners/**) and use the instructions that follow:

1. Section 3.2 Qn.3 : Find the positive minimum point of the function $f(x)=\tan(x)/(x^2)$ by computing the zeros of $f'$ using Newton's method.
           
           make Qn3_2__3_Newtons
           
           make Qn3_2__3_Secant
           
           
2. Section 3.2 Qn.5 : The equation $2(x^4) + 24(x^3) + 61(x^2) - 16x + 1 = 0$ has $2$ roots near 0.1. Determine them by means of Newton's method. Use Horner’s algorithm to compute value of the funciton and it's derivative
           
           make Qn3_2__5   
           
3. Section 3.2 Qn.14b : Using Newton's method, find the roots of the nonlinear systems:
        $$x + e^{-1x} + y^3 = 0$$
        $$x^2 + 2xy - y^2 + tan(x) = 0$$
           
           make Qn3_2__14b


## References
*David, K., & Ward, C.(2009). Numerical Analysis : Mathematics of scientific computing, third edition. American Mathematical Society*
