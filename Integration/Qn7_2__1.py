'''
Write a program for computing \int_0^x e^{-t^2} dt by summing an appropriate Taylor Series 
until individual terms fall below 10^{-8} in magnitude. Test your program by calculating the 
values of this integral for x = 0.0, 0.1, 0.2, ..., 1.0.
'''
import numpy as np
import math

fact_dict = {}
def fact(k):
    if k in fact_dict:
        return fact_dict[k]
    elif k==1 or k==0:
        return 1
    else :
        return k*fact(k-1)

'''
Taylor expansion of e^{-x^2} = \sum_{k=0}^{\infty} * (-1)^k \frac{x^{2k}}{k!}
Integration =>                 \sum_{k=0}^{\infty} * (-1)^k \frac{x^{2k+1}}{(2k+1) k!}
'''
def Taylor_exp_term(x, k):
    return (x**(2*k+1))/((2*k+1)*fact(k))

def Taylor_exp(x, eps = 1e-8):
    result = 0
    k = 0
    val = Taylor_exp_term(x, k)

    while(abs(val)>eps):
        result+=val
        k+=1
        val = ((-1)**k) * Taylor_exp_term(x, k)

    return result

for x in np.arange(0, 1.1, 0.1):
    val = Taylor_exp(x)
    print(round(x, 1), "\t", val, "\t", abs(0.5 * np.sqrt(np.pi) * math.erf(x)-val))
