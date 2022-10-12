import numpy as np
import math
from methods.newtons import Newton

class Qn3_2__3():
    '''
    Find the positive minimum point of the fucntion f(x)=tanx/(x^2)
    by computing the zeros of f' using Newton's method.
    '''
    def __init__(self) -> None:
        self.zero = 1e10

    def f(self, x:float) -> float:
        return np.tan(x)/(x**2)

    def fd(self, x:float) -> float:
        return 1.0/((np.cos(x)**2) * (x**2)) - 2*np.tanx/(x**3)

    def forward(self) -> float:
        for i in range(10):
            obj = Newton(i, self.f, self.fd)
            x = obj.forward()
            if x<self.zero and x>0:
                self.zero=x
        return self.zero


class Qn3_2__14b():
    '''
    Using Newton's method, find the roots of the nonlinear systems:
        x + e^{-1x} + y^3 = 0
        x^2 + 2xy - y^2 + tan(x) = 0
    '''
    def __init__(self) -> None:
        self.zero = 1e10

    def f(self, x:float, y:float) -> float:
        return np.array([[x + math.exp(-x) + y**3], [x**2 + 2*x*y - y**2 + np.tan(x)]])

    def fd(self, x:float, y:float) -> float:
        return np.array([[1 - math.exp(-x),             3*(y**2)], 
                        [2*x + 2*y -1.0/(np.cos(x)**2), 2*x - 2*y]])

    def forward(self) -> float:
        obj = Newton(i, self.f, self.fd)
        self.zero = obj.forward()
        return self.zero
