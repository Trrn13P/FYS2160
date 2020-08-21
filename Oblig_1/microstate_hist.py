import numpy as np
import random
import matplotlib.pyplot as plt

M = int(1e4); N = 60
S = np.zeros(M).astype(int)

for j in range(0,M):
    for i in range(0,N):
        #microstates[i,j] = random.choice([-1,1])
        #microstates_spins[i] += microstates[i,j]
        S[j] += random.choice([-1,1])

#setter opp gaussisk sannsynlighetsfunksjon
mean_S = np.sum(S)/M
sum = 0
for i in range(0,M):
    sum  += (S[i]-mean_S)**2

sigma = np.sqrt(1/(M-1)*sum)

h = np.linspace(-50,50,M)
P = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(h-mean_S)**2/(2*sigma**2))

plt.plot(h,P,linewidth=2)
plt.hist(S, bins = 30,edgecolor='black',density=True)
plt.xlabel('S')
plt.ylabel('Intensitet')
plt.show()
