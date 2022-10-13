import numpy as np
import math
from methods.newtons import Newton
from methods.secant import Secant

import sys

class Qn3_2__3():
    '''
    Find the positive minimum point of the function f(x)=tanx/(x^2)
    by computing the zeros of f' using Newton's method.
    '''
    def __init__(self) -> None:
        self.minim_zero = 1e10
        self.zero = 1e10

    def function(self, x:float) -> float:
        f = np.tan(x)/(x**2 + 1e-20)
        return f

    def function_der(self, x:float) -> float:
        fd = 1.0/((np.cos(x)**2) * (x**2) + 1e-20) - 2*np.tan(x)/(x**3 + 1e-20)
        return fd

    def function_der_der(self, x:float) -> float:
        fd = 1.0/((np.cos(x)**2) * (x**2) + 1e-20) - 2*np.tan(x)/(x**3 + 1e-20)
        fdd = 2.0*np.tan(x)/((x**2)*(np.cos(x)**2) + 1e-20) - 4.0/((x**3)*(np.cos(x)**2) + 1e-20) + 6.0*np.tan(x)/(x**4 + 1e-20)
        return fd, fdd


    def forward(self, method="Newton") -> float:
        for i in range(-10,10):
            print(f"\n\n\n\n*************************** Using initial value x0={i} ***************************")
            if method=="Newton":
                obj = Newton(i, self.function_der_der)
            elif method=="Secant":
                obj = Secant(i, i-1, self.function_der)
            else:
                raise ValueError
            x = obj.forward()
            val = self.function(x)
            print("\n\n\n\n\n\n", "x : ", x, ", val : ", val, "\n\n\n\n\n")
            if val<self.minim_zero and val>1e-2:
                self.minim_zero=val
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

        # Array for holding the roots of the polynomial
        self.zeros = {}

        # Estimate of the value near to which roots exist and window to search within for the problem
        self.z0_avg = 0.1
        self.w = 8

        # Polynomial coefficients
        self.ak = np.array([2, 24, 61, -16, 1])[::-1]
    
    def function(self, z):
        p = 0
        for i in range(len(self.ak)):
            p += self.ak[i] * (z**i)
        return p

    def forward(self) -> list:
        for z0 in np.linspace(self.z0_avg-2*self.w, self.z0_avg+self.w, 50):
            obj = Newton(z0, None)
            z = obj.forward(use_horner=True, ak=self.ak)
            if round(z, 5) not in self.zeros:
                self.zeros[round(z, 5)] = z
        return self.zeros

if __name__=="__main__":

    if sys.argv[1]=="Qn3_2__3" and sys.argv[2]=="Newtons":
        obj = Qn3_2__3()
        zero = obj.forward(method="Newton")
        print(" \n\n ------------- Qn3_2__3 Newtons ------------- \n")
        print(f"\tzero occurs at x = ", zero)
        print("\n\tf(x) = ", obj.function(zero))
        print("\n\tf'(x) = ", obj.function_der(zero))

    elif sys.argv[1]=="Qn3_2__14b":
        obj = Qn3_2__14b()
        zero = obj.forward()
        print(" \n\n ------------- Qn3_2__14b Newtons ------------- \n")
        print(f"\tzero occurs at x = ", zero.reshape(-1))
        print("\n\tf(x) = ", obj.function_der(zero)[0].reshape(-1))

    elif sys.argv[1]=="Qn3_2__3" and sys.argv[2]=="Secant":
        obj = Qn3_2__3()
        zero = obj.forward(method="Secant")
        print(" \n\n ------------- Qn3_2__3 Secant ------------- \n")
        print(f"\tzero occurs at x = ", zero)
        print("\n\tf(x) = ", obj.function(zero))
        print("\n\tf'(x) = ", obj.function_der(zero))

    elif sys.argv[1]=="Qn3_2__5":
        obj = Qn3_2__5()
        zero = obj.forward()
        print(" \n\n ------------- Qn3_2__5 Newton's + Horner's ------------- \n")
        print("All zero's of the polynomial : ", list(zero.values()), "\n")
        for key in zero.keys():
            print("{:<20} \t{:<20}".format(f"f({zero[key]})", f"= {obj.function(zero[key])}"))

        print("\n\n Zeros close to 0.1 are : ")
        for key in zero.keys():
            if abs(key-0.1)<1:
                print(f" x = {zero[key]}, f({zero[key]}) = {obj.function(zero[key])}")

    else:
        print("Please provide the question number. Check Makefile for examples on how to run main.py")
        raise ValueError