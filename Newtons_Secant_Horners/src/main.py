import numpy as np
import math
from methods.newtons import Newton
from methods.secant import Secant

class Qn3_2__3():
    '''
    Find the positive minimum point of the fucntion f(x)=tanx/(x^2)
    by computing the zeros of f' using Newton's method.
    '''
    def __init__(self) -> None:
        self.zero = 1e10

    def function(self, x:float) -> float:
        f = np.tan(x)/(x**2 + 1e-20)
        return f

    def function_der(self, x:float) -> float:
        f = np.tan(x)/(x**2 + 1e-20)
        fd = 1.0/((np.cos(x)**2) * (x**2) + 1e-20) - 2*np.tan(x)/(x**3 + 1e-20)
        return f, fd


    def forward(self, method="Newton") -> float:
        for i in range(-10,10):
            if method=="Newton":
                obj = Newton(i, self.function_der)
            elif method=="Secant":
                obj = Secant(i, i-1, self.function)
            else:
                raise ValueError
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

    def function_der(self, x) -> np.ndarray:
        f = np.array([x[0,0] + math.exp(-x[0,0]) + x[1,0]**3, 
                      x[0,0]**2 + 2*x[0,0]*x[1,0] - x[1,0]**2 + math.tan(x[0,0])]).reshape(2,1)
        fd = np.array([[1 - math.exp(-x[0,0]),                                    3*(x[1,0]**2)], 
                       [2*x[0,0] + 2*x[1,0] + 1.0/(math.cos(x[0,0])**2 + 1e-20),  2*x[0,0] - 2*x[1,0]]])
        return f, fd

    def forward(self) -> np.ndarray:
        x = np.ones((2,1), dtype=float)
        obj = Newton(x, self.function_der)
        self.zero = obj.forward()
        return self.zero

class Qn3_2__5():
    '''
    The equation 2(x^4) + 24(x^3) + 61(x^2) - 16x + 1 = 0 has 2 roots near 0.1.
    Determine them by means of Newton's method.
    Note : use Horner’s algorithm to compute value of the funciton and it's derivative
    '''
    def __init__(self) -> None:
        self.zero = 1e10

    def f(self, x:float) -> float:
        return np.tan(x)/(x**2 + 1e-20)

    def fd(self, x:float) -> float:
        return 1.0/((np.cos(x)**2) * (x**2) + 1e-20) - 2*np.tan(x)/(x**3 + 1e-20)

    def forward(self, method="Newton") -> float:
        for i in range(-10,10):
            if method=="Newton":
                obj = Newton(i, self.f, self.fd)
            elif method=="Secant":
                obj = Secant(i, i-1, self.f)
            else:
                raise ValueError
            x = obj.forward()
            if x<self.zero and x>0:
                self.zero=x
        return self.zero

if __name__=="__main__":
    print(" \n\n Qn3_2__3 Newtons : ")
    obj = Qn3_2__3()
    zero = obj.forward(method="Newton")
    print("zero : ", zero)
    print("f val : ", obj.function_der(zero)[0])

    print(" \n\n Qn3_2__14b Newtons : ")
    obj = Qn3_2__14b()
    zero = obj.forward()
    print("zero : ", zero)
    print("f val : ", obj.function_der(zero)[0])

    print(" \n\n Qn3_2__3 Secant : ")
    obj = Qn3_2__3()
    zero = obj.forward(method="Secant")
    print("zero : ", zero)
    print("f val : ", obj.function_der(zero)[0])