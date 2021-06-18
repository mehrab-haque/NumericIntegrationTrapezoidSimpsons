import numpy as np

def trapezoid(func,x1,x2,n):
    dx=(x2-x1)/n
    xs=np.arange(x1,x2,dx)
    area=0
    for x in xs:
        area+=0.5*dx*(func(x)+func(x+dx))
    return area

def simpsons(func,x1,x2,n):
    dx = (x2 - x1) / n
    xs = np.arange(x1, x2, dx)
    area = 0
    for x in xs:
        area += (dx/6)*(func(x)+4*func(x+dx/2)+func(x+dx))
    return area