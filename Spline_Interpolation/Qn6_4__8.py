import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

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

def get_S_points(t, y, z, h, x_arr):
    S = np.zeros(len(x_arr))
    
    for idx, x in enumerate(x_arr):
        for j in range(len(t)-1):
            if x-t[j]>=0 and x-t[j+1]<0:
                i = j
                break
        A = 1.0/(6*h[i]) * (z[i+1] - z[i])
        B = z[i]/2.0
        C = -h[i]/6.0 * z[i+1] - h[i]/3.0 * z[i] + 1.0/h[i] * (y[i+1] - y[i])
        S[idx] = y[i] + (x - t[i]) * (C + (x-t[i]) * (B + (x-t[i])*A) )

    return S

def get_langrange(x, x_i, x_list):
    return np.prod((x-x_list)/(x_i - x_list + 1e-15))

def get_polynomial_interpolation_val(x_arr, y_arr, x):
    p = 0
    for i in range(len(x_arr)):
      x_list = list(x_arr)
      x_list.remove(x_arr[i])
      p += y_arr[i]*get_langrange(x, x_arr[i], np.array(x_list))
    return p

def get_f_arr(x_arr):
    return 1.0/(1 + 6.0 * x_arr**2)

def get_polynomial_interpolation_df(x_arr, y_arr, x_vals):
    p = []
    for i, x in enumerate(x_vals):
        p.append(get_polynomial_interpolation_val(x_arr, y_arr, x))

    df = pd.DataFrame()
    f = get_f_arr(x_vals)
    df["f(x)"] = f
    df["p(x)"] = p
    df["f(x)-p(x)"] = f - np.array(p)
    return df
    

# Section 6.4 Question 8a
x_arr = np.linspace(-1, 1, 21)
y_arr = get_f_arr(x_arr)

df = get_polynomial_interpolation_df(x_arr, y_arr, np.linspace(-1, 1, 41))
df.to_csv("/csv/Qn6.4_8a.csv")

# Section 6.4 Question 8b
x_arr = np.linspace(1, 21, 21)
x_arr = np.cos((x_arr - 1.0)*np.pi/20.0)
y_arr = get_f_arr(x_arr)

df = get_polynomial_interpolation_df(x_arr, y_arr, np.linspace(-1, 1, 41))
df.to_csv("/csv/Qn6.4_8b.csv")


# Section 6.4 Question 8c : With 21 equally spaced knots, repeat the experiment using a cubic interpolating spline. 
t = np.linspace(-1, 1, 21)
n = len(t)
y_arr = get_f_arr(t)

z_y, h_y = get_z_h(n, t, y_arr)

x_vals = np.linspace(-1, 1, 41)
S_y = get_S_points(t, y_arr, z_y, h_y, x_vals)
df = pd.DataFrame()
df["f(x)"] = get_f_arr(x_vals)
df["Sy(x)"] = S_y
df["f(x)-Sy(x)"] = get_f_arr(x_vals) - S_y
df.to_csv("/csv/Qn6.4_8c.csv")
