import matplotlib.pyplot as plt
import numpy as np
def circle(r=1,title='Circle', a=3,b=1):
    ''' функция для эллипса
    '''
    x=np.arange(-2,2,0.1)
    y=np.arange(-2,2,0.1)
    x,y=np.meshgrid(x,y)
    fxy=x**2 + y**2
    plt.contour(x,y,fxy,levels=[r])
    d=x**2/a**2 + y**2/b**2
    plt.contour(x,y,d,levels=1)
    plt.show()
circle(3)


