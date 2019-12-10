import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange (0,300,0.1)
def bacteria(k,t):
    dkdt=a*k
    return dkdt
k_0=2
a1=0.02
a=a1
solve_bac=odeint(bacteria,k_0,t,)
plt.plot(t,solve_bac[:,0], label='Размножение бактерий')
plt.show()
