from scipy import stats
import numpy as np

def linfit(X,Y):
    list = stats.linregress(X,Y)  # list = [a,b,r,t,delta_a]
    a = list[0]
    b = list[1]
    delta_a = list[-1]
    x = np.linspace(X[0],X[-1],len(X))
    y = a*x + b
    return a,b,delta_a, x,y
