import numpy as np

class Newton:
    def __init__(self, x1, x2, f) -> None:
        # Initial value - staring point
        self.x1 = x1
        self.x2 = x2

        # Function for which we're computing the zero. Ex : tan(x)/(x^2)
        self.f = f
        
    def forward(self, eps=1e-10, max_iter=1000):
            
        if isinstance(self.x, float):
            f1 = self.f(self.x1)
            f2 = self.f(self.x2)
            for i in range(max_iter):
                x_new = self.x2 - f2 * (self.x2 - self.x1)/(f2 - f1)
                if abs(x_new-self.x2)<eps:
                    return x_new

                # re-initialize x1 and x2 based on newly obtained value
                self.x1 = self.x2
                f1 = f2
                self.x2 = x_new
                f2 = self.f(self.x2)
        else:
            raise TypeError

        return self.x2

