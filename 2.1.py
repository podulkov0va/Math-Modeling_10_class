import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,20,0.01)
def diff_func(z, t):
    s,omega=z
    ds_dt=omega
    domega_d=- g*np.sin(s/l)-k*omega/m
    return ds_dt,domega_d
s0=1
m=3
k=0.5
l=2
g=10
omega0=0.05
z0=s0, omega0 
sol=odeint(diff_func,z0,t)
plt.plot(sol[:,0], 'g')
plt.legend()
plt.show()  