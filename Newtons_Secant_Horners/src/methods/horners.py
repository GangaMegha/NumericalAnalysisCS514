import numpy as np
from decimal import Decimal

'''
H O R N E R ' S    A L G O R I T H M :

    Hormer's algorithm is to used to efficiently compute values of a polynomial. 
    The method is also known as 'nested multiplcation' or 'synthetic division'.

    The algorithm has several usecases. For example : 
        1. Given a complex number z0 and polynomial p find the values of p(z0) and it's derivatives.
        2. Find the deflation factors, ie., removing linear factor from polynomial like p(z) = (z-z0) * q(z) + r by computing r
        3. Find coefficients of Taylor series expansion of the polynomial p around z0 (complete Horner's algorithm)


    Here, the Horner class uses Horner's algorithm to compute the below values given z0 and coefficients of polynomial p(z)
        1. alpha = p(z0) 
        2. beta = p'(z0)
'''
class Horner:

    def __init__(self, z0:float, ak:np.ndarray) -> None:

        # Initial value - staring point
        if isinstance(z0, (int, float, Decimal)):
            # self.z0 = float(z0)
            self.z0 = z0
        else:
            raise TypeError

        # Coefficients of the polynomial p(z) = a_n z^n + a_{n-1} z^{n-1} +...a_1 z + a_0
        # in the order [a0, a1, ..., a_{n-1}, a_n]
        if isinstance(ak, np.ndarray) and ak.dtype in (int, float, Decimal):
            # self.ak = ak.astype(float)
            self.ak = ak
        else:
            raise TypeError
                
        # alpha and beta hold current estimates of p(z0) and p'(z0)   
        self.alpha = ak[-1]
        self.beta = 0.0

        # Index of coefficient of highest degree
        self.n = len(ak)-1
               
    def forward(self, eps=1e-32, max_iter=10000):

        for k in np.arange(self.n-1, -1, step=-1):
            # Update rule
            self.beta = self.alpha + self.z0 * self.beta
            self.alpha = self.ak[k] + self.z0 * self.alpha

        # Computed values of alpha = p(z0) and beta = p'(z0)
        return self.alpha, self.beta