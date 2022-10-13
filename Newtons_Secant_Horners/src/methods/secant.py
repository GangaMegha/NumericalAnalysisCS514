'''
S E C A N T    M E T H O D :

    Secant method is used to find the zero of a real valued function of a real variable.

    One of the drawbacks of Newton's method is that it involves derivative of the function whose zero is sought.
    To overcome this disadvantage, one of the ways is to use secant method.

    For funtion f(x), we can find its zero using the following iteration :
        x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1})) ; n>=1
'''


class Secant:

    def __init__(self, x1:float, x2:float, function=None) -> None:

        # Initial value - staring point
        if isinstance(x1, (int, float)) and isinstance(x2, (int, float)):
            self.x1 = float(x1)
            self.x2 = float(x2)
        else:
            raise TypeError

        # Function for which we're computing the zero. Ex : tan(x)/(x^2)
        self.function = function

        # Compute values of the function at x1 and x2    
        self.f1 = self.function(self.x1)
        self.f2 = self.function(self.x2)
        
    def forward(self, eps=1e-10, max_iter=100):
            
        print("\n\n--------------------- Beginning Secant Method ---------------------\n\n")
        if isinstance(self.f1, (float)) and isinstance(self.f2, (float)):

            for i in range(max_iter):
                # Update rule
                x_new = self.x2 - self.f2 * (self.x2 - self.x1)/(self.f2 - self.f1)

                print(f"n = {i+1: <10} : \t x_(n-1) = {self.x1: <20}, \t x_(n) = {self.x2: <20}, \t x_(n+1) = {x_new: <20}, \t error = |x_(n+1) - x_(n)| = {abs(x_new-self.x2): <20}")
                
                # Stopping criterion
                if abs(x_new-self.x2)<eps:
                    return x_new

                # Re-initialize x1 and x2 based on newly obtained value x_new
                self.x1 = self.x2
                self.f1 = self.f2
                
                self.x2 = x_new
                self.f2 = self.function(self.x2)

            return self.x2
        else:
            raise TypeError