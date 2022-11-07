import numpy as np
import matplotlib.pyplot as plt 

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

def get_S_points(t, y, z, h, num_points):
    S = np.zeros(num_points)
    x_arr = np.linspace(min(t), max(t), num_points)
    
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
        

#Capital A : https://www.geogebra.org/m/HmnV33gj
coordinates = [(4.2,4.83), 
                (4.78,4.83), 
                (5.68,4.87), 
                (5.66,5.57), 
                (5,6), 
                (4,6), 
                (3.64,5.51), 
                (3.56,4.73),
                (3.84,3.73),
                (4.66,3.41),
                (5.5,3.51)
              ]

t = []
x = []
y = []
for i, elem in enumerate(coordinates):
    t.append(i)
    x.append(elem[0])
    y.append(elem[1])

n = len(t)
z_x, h_x = get_z_h(n, t, x)
z_y, h_y = get_z_h(n, t, x)

S_x = get_S_points(t, x, z_x, h_x, num_points=50)
S_y = get_S_points(t, y, z_y, h_y, num_points=50)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
axes[0].scatter(x, y)
axes[0].set_title("Original samples")
axes[0].set_xlabel("Sampled x")
axes[0].set_ylabel("Sampled y")
axes[1].scatter(S_x, S_y)
axes[1].set_title("Cubic spline interpolation")
axes[1].set_xlabel(r"x from $S_x$")
axes[1].set_ylabel(r"y from $S_y$")
fig.tight_layout()
plt.show()