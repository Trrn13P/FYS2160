import numpy as np
import matplotlib.pyplot as plt

N = 1e2
N_len = int(1e3)

q = np.linspace(1,N_len,N_len)
omega_lowT = (N*np.exp(1)/q)**q
omega_highT = (q*np.exp(1)/N)**N
omega_stirling = ((q+N)/q)**q * ((q+N)/N)**N

plt.plot(q,np.log(omega_lowT),label=r"$\Omega_{low\ T}$, N=%g"%(N))
plt.plot(q,np.log(omega_highT),label=r"$\Omega_{high\ T}$, N=%g"%(N))
plt.plot(q,np.log(omega_stirling),label=r"$\Omega_{Stirling}$, N=%g"%(N))
plt.xlabel("q",FontSize=15)
plt.ylabel("S/k",FontSize=15)
plt.legend()
plt.savefig("../figures/omegas.png")
plt.clf()
