import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k
from scipy.constants import R


k = 1;

infile = open("../data_files/numerical_data.txt","r")
N = infile.readline().split("=")[-1]
N = eval(N)

q = []
omega_numerical = []
S_numerical = []
T_numerical = []
Cv_over_Nk_numerical = []

for line in infile:
    line = line.split()
    q.append(eval(line[0]))
    omega_numerical.append(eval(line[1]))
    S_numerical.append(eval(line[2]))
    T_numerical.append(eval(line[3]))
    Cv_over_Nk_numerical.append(eval(line[4]))
infile.close()
q = np.asarray(q)
omega_numerical = np.asarray(omega_numerical)
S_numerical = np.asarray(S_numerical)
T_numerical= np.asarray(T_numerical)
Cv_over_Nk_numerical= np.asarray(Cv_over_Nk_numerical)

plt.yticks()
for epsilon in range(200,5001,500):
    plt.plot(T_numerical*epsilon,Cv_over_Nk_numerical*N*k/R,label="epsilon=%g"%(epsilon))
plt.xlabel("T [K]",FontSize=15)
plt.ylabel(r"$C_V/R$ [J/K]",FontSize=15)
plt.legend()
plt.savefig("../figures/C_comparrison.png")
plt.clf()
