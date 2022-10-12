from typing import Type
import numpy as np

'''
N E W T O N ' S     M E T H O D :

    Newton-Raphson iteration to find the zero of a real valued function of a real variable.
        For funtion f(x), we can find its zero using the following iteration :
            x_{n+1} = x_n - f(x_n)/f'(x_n)  ; n>=0

    We can also use it for solving a system of non-linear equations by linearizing it and using matrices.
        Example, for 
                    f1(x1, x2) = 0
                    f2(x1, x2) = 0

        Let X = [[x1], 
                 [x2]]

            F(X) = [[f1(x1, x2)], 
                    [f2(x1, x2)]]
            
            F'(X) = [[df1/dx1, df1/dx2], 
                     [df2/dx1, df2/dx2]]
        
        We use the iteration :
                    X_{n+1} = X_n - Inv{F'(X_n)} * F(X_n)
'''
class Newton:
    def __init__(self, x0, function) -> None:
        # Initial value - staring point
        if isinstance(x0, (int, float)):
            self.x = float(x0)
        elif isinstance(x0, np.ndarray) and x0.dtype in (int, float):
            self.x = x0.astype(float)
        else:
            raise TypeError

        # Function for which we're computing the zero. Ex : tan(x)/(x^2)
        # And it's derivative. Ex : tan(x)/(x^2)
        self.function = function

    def forward(self, eps=1e-32, max_iter=10000):
        
        # To find zero of function f
        if isinstance(self.x, float):
            for i in range(max_iter):
                # Compute values of the function and it's derivative at self.x
                f, fd = self.function(self.x)
                
                # Update rule
                x_new = self.x - f/(fd+1e-20)
                
                # Stopping criterion
                if abs(x_new-self.x)<eps:
                    return x_new

                self.x = x_new

        # To solve non-linear equations in column matrix F
        elif isinstance(self.x, np.ndarray):
            for i in range(max_iter):
                # Compute values of matrices F and it's derivative Fd at vector self.x
                F, Fd = self.function(self.x)

                # Update rule
                x_new = self.x - np.linalg.inv(Fd) @ F

                # Stopping criterion
                if abs(np.sum(x_new-self.x))<eps:
                    return x_new

                self.x = x_new
        # If self.x is neither a number of a numoy array
        else:
            raise TypeError

        return self.x