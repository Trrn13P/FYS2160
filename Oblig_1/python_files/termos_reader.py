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
import matplotlib.pyplot as plt
plt.plot(t,kopp1)
plt.plot(t,kopp2)
plt.show()
