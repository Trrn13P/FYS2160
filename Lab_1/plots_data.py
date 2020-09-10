import matplotlib.pyplot as plt
import numpy as np
from linfit import linfit

def plot_data(path,k,N,f):

    infile1 = open(path +"/log_pressure.txt","r")
    infile2 = open(path +"/dump_pressure.txt","r")

    infile1.readline()
    infile2.readline()

    P_from_T = []
    P_from_log = []
    T = []

    for i in infile1:
        P_from_log.append(eval(i))
    for j in infile2:
        P_from_T.append(eval(j.split()[0]))
        T.append(eval(j.split()[1]))
    infile1.close()
    infile2.close()

    infile3 = open(path + "/log_E.txt","r")
    infile3.readline()
    E = []
    for k in infile3:
        E.append(eval(k))

    P_from_log_new = []
    E_new = []
    for i in range(0,len(P_from_log),2):
        P_from_log_new.append(P_from_log[i])
        E_new.append(E[i])


    P_from_log = P_from_log_new
    E = E_new


    plt.xlabel("T")
    plt.ylabel("P(T)")
    plt.plot(T,P_from_T,label="P(T) from calculation")
    plt.plot(T,P_from_log,label="P(T) from logfile")
    plt.legend()
    plt.savefig(path + "/figures/T_P.png")
    plt.clf()

    k = 1
    N = 500
    f = 3

    Cv_analytical = 1/2*N*f*k+N*k




    a,b,delta_a,x,y = linfit(T,E)

    outfile = open(path + "/data/Heatcap.txt","w+")
    outfile.write("Heat capacity:\n")
    outfile.write("Numerical: %.10f +- %.10f\n"%(a,delta_a))
    outfile.write("Analytical: %.10f"%(Cv_analytical))


    plt.xlabel("T")
    plt.ylabel("E(T)")
    plt.plot(T,E,label="E(T) from LJ")
    plt.plot(x,y,label="Linfit")
    plt.legend()
    plt.savefig(path + "/figures/E_T.png")
    plt.clf()
