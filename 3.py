import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,200,0.1)
def dift_func(z,t):
    s, v = z
    ds_dt = v 
    domega_dt=-G*M/R**2
    return ds_dt, domega_dt

M=5.97*10**24
R0=6371000
G=6.67418478*10**(-11)

v0=5
z0=R0,v0
sol=odeint(dift_func,z0,t)
plt.plot(t,sol[:,0],'b')

