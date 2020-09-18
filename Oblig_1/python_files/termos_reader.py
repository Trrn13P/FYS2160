import matplotlib.pyplot as plt
import numpy as np
path_data = "../data_files/"

infile = open(path_data+"termokopper.txt","r")

kopp1 = []
kopp2 = []
t = []

for line in infile:
    line = line.split()
    t.append(eval(line[0]))
    kopp1.append(eval(line[1]))
    kopp2.append(eval(line[2]))
infile.close()

t = np.asarray(t)
kopp1 = np.asarray(kopp1)
kopp2 = np.asarray(kopp2)*1.12



plt.plot(t,kopp1,label="Bodum mug")
plt.plot(t,kopp2,label="Temperfect mug")
plt.xlabel("t $[s]$",FontSize=15)
plt.ylabel(r"T $[^{\circ}C]$",FontSize=15)
plt.legend()
plt.savefig("../figures/mugs.png")
plt.clf()

plt.plot(t,kopp1,label="Bodum mug")
plt.plot(t,kopp2,label="Temperfect mug")
plt.xlabel("t $[s]$",FontSize=15)
plt.ylabel(r"T $[^{\circ}C]$",FontSize=15)
plt.xlim(0,150)
plt.ylim(85,90)
plt.legend()
plt.savefig("../figures/mugs_2.png")
plt.clf()
