import sys
import numpy as np

# from Interpolation_CubicSpline_LagrangePolynomial.Qn6_4__7 import get_z_h
def get_z_h(n, t, y):
    h, b = np.zeros(n), np.zeros(n)
    for i in range(n-1):
        h[i] = t[i+1]-t[i]
        b[i] = 6.0 * (y[i+1] - y[i]) / h[i]
    
    u, v = np.zeros(n), np.zeros(n)

    u[1] = 2.0 * (h[0] + h[1])
    v[1] = b[1] - b[0]

    for i in range(2, n-1):
        u[i] = 2.0 * (h[i] + h[i-1]) - (h[i-1]**2)/u[i-1]
        v[i] = b[i] - b[i-1] - (h[i-1] * v[i-1])/u[i-1]

    z = np.zeros(n)

    for i in range(n-2, 0, -1):
        z[i] = (v[i] - h[i]*z[i+1])/u[i]

    return z, h

'''
We know,
S_i(x) = \frac{z_i}{6h_i} (t_{i+1} - x)^3 
         + \frac{z_{i+1}}{6h_i} (x - t_i)^3 
         + ( \frac{y_{i+1}}{h_i} - \frac{z_{i+1} h_i}{6} ) (x - t_i)
         + ( \frac{y_i}{h_i} - \frac{z_i h_i}{6} ) (t_{i+1} - x)

Integrating S_i(x),
IS_i(x) = \int S_i(x) dx 
        =   - \frac{z_i}{6h_i} \frac{1}{4} (t_{i+1} - x)^4
            + \frac{z_{i+1}}{6h_i} \frac{1}{4} (x - t_i)^4
            + ( \frac{y_{i+1}}{h_i} - \frac{z_{i+1} h_i}{6} ) \frac{1}{2} (x - t_i)^2
            - ( \frac{y_i}{h_i} - \frac{z_i h_i}{6} ) \frac{1}{2} (t_{i+1} - x)^2

Therefore, 
\int_{t_0}^{t_n} S(x) dx = \sum_{i=0}^{n-1} \int_{t_i}^{t_{i+1}} S_i(x) dx
                         = \sum_{i=0}^{n-1} IS_i(t_{i+1}) - IS_i(t_{i})
'''
def get_integral_S_i(x, z, h, t, y, i):
    val = - z[i]/(6*h[i]) * (1/4) * (t[i+1] - x)**4 \
            + z[i+1]/(6*h[i]) * (1/4) * (x - t[i])**4 \
                + ( y[i+1]/h[i] - (z[i+1]*h[i]/6) ) * (1/2) * (x - t[i])**2 \
                    - ( y[i]/h[i] - (z[i]*h[i]/6) ) * (1/2) * (t[i+1] - x)**2
    return val
                
def get_integral_S(z, h, t, y):
    result = 0
    for i in range(n-1):
        result += (get_integral_S_i(t[i+1], z, h, t, y, i) - get_integral_S_i(t[i], z, h, t, y, i))
    return result

def get_f_arr_a(n):
    x = np.linspace(0, 1, n+1)
    return x, (4/np.pi) * 1.0/(1 + x**2)

def get_f_arr_b(n):
    x = np.linspace(1, 3, n+1)
    return x, (1.0/np.log(3)) * 1.0/(x+1e-15)

def main(q, n):
    if q=="a":
        t, y = get_f_arr_a(n)
    elif q=="b":
        t, y = get_f_arr_b(n)
    else:
        print("Please choose question from options : (a, b)")
        raise ValueError

    z_y, h_y = get_z_h(n+1, t, y)
    integral = get_integral_S(z_y, h_y, t, y)
    print(f"\n\n\nn = {n} \t Integral = {integral} \t Error = {abs(1 - integral)}\n\n\n")

if __name__=="__main__":
    q = sys.argv[1]
    n = int(sys.argv[2])

    main(q, n)