# Newton-Raphson, Secant Method and Horner's Algorithm

## 1. Newton's method
Newton-Raphson iteration can be used to find the zero of a real valued function of a real variable.

For funtion f(x), we can find its zero using the following iteration :

      x_{n+1} = x_n - f(x_n)/f'(x_n)  ; n>=0
      
where f(x_n) is the value of the function at x_n and f'(x_n) is the value of the derivative of f(x) at x_n.
      
We can also use it for solving a system of non-linear equations by linearizing it and using matrices.

Example, for 

      f1(x1, x2) = 0
      f2(x1, x2) = 0

      X = [[x1], 
           [x2]]

      F(X) = [[f1(x1, x2)], 
              [f2(x1, x2)]]

      F'(X) = [[df1/dx1, df1/dx2], 
               [df2/dx1, df2/dx2]]
        
We use the iteration :
      
      X_{n+1} = X_n - Inv{F'(X_n)} * F(X_n)
      
      
## 2. Secant Method
Secant method is also used to find the zero of a real valued function of a real variable.

One of the drawbacks of Newton's method is that it involves derivative of the function whose zero is sought. 
To overcome this disadvantage, one of the ways is to use secant method.

For funtion f(x), we can find its zero using the following iteration :
      
      x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1})) ; n>=1
      
      
## 3. Horner's Algorithm

Horner's algorithm is to used to efficiently compute values of a polynomial. 
The method is also known as 'nested multiplcation' or 'synthetic division'.

The algorithm has several usecases. For example : 
1. Given a complex number z0 and polynomial p find the values of p(z0) and it's derivatives.
2. Find the deflation factors, ie., removing linear factor from polynomial like p(z) = (z-z0) * q(z) + r by computing r
3. Find coefficients of Taylor series expansion of the polynomial p around z0 (complete Horner's algorithm)


Here, given $z_0$ and coefficients of polynomial $p(z) = a_n x^n + a_{n-1} x^{n-1} + ... a_1 x + a_0$ we use Horner's algorithm to compute :
1. $\alpha = p(z_0)$ 
2. $\beta  = p'(z_0)$

by starting with $\alpha = a_n$ and $\beta=0$ and using the following iteration from $k=n-1 to 0:
      
$\beta = \alpha + z_0 \times \beta$      
$\alpha = a_k + z_0 \times \alpha$
