import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k
from math import factorial

k = 1

N = int(300)
N_len = 800
q = np.linspace(1,N_len,N_len)
dq = (q[-1]-q[0])/(len(q)-1)


omega = np.zeros(N_len)
for i in range(0,N_len):
    omega[i] = factorial(int(q[i])+N-1)/(factorial(int(q[i]))*factorial(N-1))
S = k*np.log(omega)

dqdS = np.zeros(N_len)

for i in range(1,N_len):
    dqdS[i] = dq/(S[i]-S[i-1])
T = dqdS

Cv = np.zeros(N_len)
for i in range(1,N_len):
    Cv[i] = dq/(T[i]-T[i-1])


plt.plot(q,Cv/N,label=r"$N=%g$"%(N_len))
plt.xlabel("q",FontSize=15)
plt.ylabel(r"$C_V/Nk$",FontSize=15)
plt.legend()
plt.savefig("../figures/C_mot_q.png")
plt.clf()

plt.plot(q,S,label=r"$N=%g$"%(N_len))
plt.xlabel("q",FontSize=15)
plt.ylabel(r"$S/k$",FontSize=15)
plt.legend()
plt.savefig("../figures/S_mot_q.png")
plt.clf()

outfile = open("../data_files/numerical_data.txt","w+")
outfile.write("q Omega S T Cv/Nk N=%g\n"%(N_len))
for i in range(N_len):
    outfile.write("%g %.5f %.5f %.5f %.5f\n"%(q[i],omega[i],S[i],T[i],Cv[i]/N))
outfile.close()
