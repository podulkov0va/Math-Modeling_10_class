import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,14,0.1)
def invest(i,t):
    didt=-k*i*t
    return didt
i_0=1000
k1=0.08
k=k1
solve_inv=odeint(invest,i_0,t)
plt.plot(t,solve_inv[:,0], label='Изменение инвестиций')
plt.show()

