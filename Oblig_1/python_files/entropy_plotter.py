import numpy as np
import matplotlib.pyplot as plt

def C(T):
    if T<=273.15:
        return 2.03 * 1e3
    elif T>=373.15:
        return 1.998 * 1e3
    else:
        return 4.184 * 1e3

N = int(1e4)
T = np.linspace(100,500,N)
dSdT = np.zeros(N)
for i in range(N):
    dSdT[i] = C(T[i])/T[i]


S = np.zeros(N)
sum = 0

dT = (T[-1]-T[0])/N
for i in range(N):
    S[i] = sum
    sum += C(T[i])/T[i]*dT
"""
plt.plot(T,S)
plt.show()
"""
plt.plot(T,dSdT)
plt.show()