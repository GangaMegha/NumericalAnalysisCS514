import numpy as np

from methods.horners import Horner

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
    def __init__(self, x0, function=None) -> None:
        '''
            x0          : numerical value for computing zero of function
                          column matrix of numeric elements for solving non-linear equations

            fucntion    : function(x) should return the values of the function and it's derivative at x
                          ie, f(x) and f'(x)
        '''
        # Initial value - staring point
        if isinstance(x0, (int, float)):
            self.x = float(x0)
        elif isinstance(x0, np.ndarray) and x0.dtype in (int, float):
            self.x = x0.astype(float)
        else:
            print("Please provide an initial value x0 which is numeric for computing zero of function \n\
                or provide initial value x0 as column matrix for solving non-linear equations.")
            raise TypeError

        # Function for which we're computing the zero. Ex : tan(x)/(x^2)
        # And it's derivative. Ex : tan(x)/(x^2)
        self.function = function

    def forward(self, use_horner=False, ak=None, eps=1e-10, max_iter=100):
        '''
            use_horner  : If True, uses Horner's algorithm to compute value and derivative of the polynomial 

            ak          : Only used when use_horner=True
                          A numpy array with coefficients [a0, a1, ..., a_{n-1}, a_n]
                          of the polynomial p(z) = a_n z^n + a_{n-1} z^{n-1} +...a_1 z + a_0

            Note : use_horner is set to True only when self.function is None. 
                   ie., no external python function for returning the function and it's derivatives are provided

            eps  
        '''

        print("\n\n--------------------- Beginning Newton's Iteration ---------------------\n\n")
        # To find zero of function f
        if isinstance(self.x, float):

            for i in range(max_iter):
                # Compute values of the function and it's derivative at self.x

                # Use horner's algorithm to compute p(x) and p'(x)
                if use_horner and len(ak)>0 and self.function==None:
                    f, fd = Horner(self.x, ak).forward()

                # Use provided funciton in self.function to compute f(x) and f'(x)
                elif self.function!=None:    
                    f, fd = self.function(self.x)
                else:
                    print("self.function cannot be None if use_horner is False. \n \
                            Please initialize self.function to a python function that returns \n \
                            the function value and it;s derivative, so that we can perform Newton's iteration.")
                    raise ValueError
                
                # Update rule
                x_new = self.x - f/(fd+1e-20)

                print(f"n = {i: <10} : \t x_(n) = {self.x: <20}, \t x_(n+1) = {x_new: <20}, \t error = |x_(n+1) - x_(n)| = {abs(x_new-self.x): <20}")
                
                # Stopping criterion
                if abs(x_new-self.x)<eps:
                    return x_new

                self.x = x_new

        # To solve non-linear equations in column matrix F
        elif isinstance(self.x, np.ndarray):
            for i in range(max_iter):
                # Compute values of matrices F and it's derivative Fd at vector self.x

                if self.function!=None:    
                    F, Fd = self.function(self.x)
                else:
                    print("self.function cannot be None if x is a vector that corresponds to non-linear equations. \n \
                            Please initialize self.function to a python function that returns \n \
                            the function value and it's derivative, so that we can perform Newton's iteration.")
                    raise ValueError

                # Update rule
                x_new = self.x - np.linalg.inv(Fd) @ F

                s1 = ", ".join(list(self.x.astype(str).reshape(-1)))
                s2 = ", ".join(list(x_new.astype(str).reshape(-1)))
                print(f"n = {i: <10} : \t x_(n) = [{s1: <40}], \t x_(n+1) = [{s2: <40}], \t error = sum(|x_(n+1) - x_(n)|) = {np.sum(np.abs(x_new-self.x)): <20}")
                
                # Stopping criterion
                if np.sum(np.abs(x_new-self.x))<eps:
                    return x_new

                self.x = x_new
        # If self.x is neither a number of a numoy array
        else:
            print("self.x is expected to be a number or a numpy matrix that contains numerical values")
            raise TypeError

        return self.x