import numpy as np

class Newton:
    def __init__(self, x0, f, fd) -> None:
        # Initial value - staring point
        self.x = x0

        # Function for which we're computing the zero. Ex : tan(x)/(x^2)
        self.f = f

        # Derivative of f. Ex : tan(x)/(x^2)
        self.fd = fd
        
    def forward(self, eps=1e-10, max_iter=1000):
            
        if isinstance(self.x, (int, float)):
            for i in range(max_iter):
                x_new = self.x - self.f(self.x)/self.fd(self.x)
                if abs(x_new-self.x)<eps:
                    return x_new
                self.x = x_new
        elif isinstance(self.x, np.ndarray):
            x_new = self.x - np.linalg.inv(self.fd(self.x)) @ self.f(self.x)
            if np.sum(x_new-self.x)<eps:
                return x_new
            self.x = x_new
        else:
            raise TypeError

        return self.x

