from dump_reader import dumpreader
from log_reader import logreader
from P_calc import P_calc
from plots_data import plot_data
"""
filename1 = "./HeatcapLJ/dump.lammpstrj"
dumpreader(filename1)

filename2 = "./HeatcapLJ/log.lammps"
logreader(filename2)
"""
path = "./HeatcapLJ"
k = 1
m = 1
f = 3
#P_calc(path,k,m,f)

N = 500
plot_data(path,k,N,f)
