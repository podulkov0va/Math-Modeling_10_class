import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,100,0.1)
def skorost(v,t):
    dvdt=f/m - a*v**2/m
    return dvdt
v_0=0
a1=0.5
a=a1
f=10
m=100
solve_sk=odeint(skorost,v_0,t)
plt.plot(t,solve_sk[:,0], label='Изменение скорости')
plt.show()
