import matplotlib.pyplot as plt
import numpy as np
"""

N_ = 30000
q = np.linspace(100,N_,N_-100+1)
print(q)

N = 100
omega = ((q+N)/q)**q * ((q+N)/N)**N


#S = q*np.log(N)
#S = N*np.log(q)

#plt.plot(q,np.log(omega))
#plt.plot(q,S)
#plt.show()
"""

N_ = 50
N = 100
q = np.linspace(1,N_,N_)

omega_low = (N*np.exp(1)/q)**q
omega_low_approx = N**q

#plt.plot(q,np.log(omega_low),label="foreles")
#plt.plot(q,np.log(omega_low_approx),label="Approx")
#plt.legend()
#plt.show()

N_ = 1000
q = np.linspace(N_,N_+50,51)
omega_high_approx = q**N

from scipy.constants import k
omega_high = (q*np.exp(1)/N)**N


plt.plot(q,omega_high,label="foreles")
#plt.plot(q,omega_high_approx,label="Approx")
plt.legend()
plt.show()
