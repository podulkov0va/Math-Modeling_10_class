import matplotlib.pyplot as plt
import numpy as np
def parabola(a=1, b=1, c=0):
    '''Функция для параболы
    '''
  
    x = np.arange(-10,10,0.01)
    x[1000]=0.01
    y = a*x**2 + b*x + c
    plt.plot(x,y, color='k', label='parabola')
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.title('parabola')
    plt.legend()
    k=1/x 
    plt.plot(x,k)
    plt.show()
parabola()   
     
   