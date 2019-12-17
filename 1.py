import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,20,0.01)
def diff_func(z, t):
    theta,omega=z
    dtheta_dt=omega
    domega_d=-np.sin(theta)*omega-3*theta*t-5
    return dtheta_dt,domega_d
theta0=np.pi-0.1
omega0=0.05
z0=theta0, omega0
b=0.25
c=5.0  
sol=odeint(diff_func,z0,t)
plt.plot(sol[:,0], 'g', label='theta(omega)')
plt.legend()
plt.show()