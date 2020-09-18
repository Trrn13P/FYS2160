import numpy as np
import matplotlib.pyplot as plt

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


S_analytical = N*k*np.log(2*q/N+1)
plt.plot(q,S_analytical)
plt.plot(q,S_numerical)
plt.show()
