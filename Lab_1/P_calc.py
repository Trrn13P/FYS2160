import numpy as np

def P_calc(path,k,m,f):
    infile = open(path + "/v_avg_sqrd.txt","r")

    N = eval(infile.readline().split()[1])
    V = eval(infile.readline().split()[1])

    v_sqrd_ave = []
    for line in infile:
        v_sqrd_ave.append( eval(infile.readline()))
    infile.close()
    v_sqrd_ave = np.asarray(v_sqrd_ave)


    T = m*v_sqrd_ave/(f*k)
    P = N*k*T/V

    outfile = open(path + "/dump_pressure.txt","w+")
    outfile.write("Pressure: Temperature: \n")
    for i,j in zip(P,T):
        outfile.write("%.10f %.10f\n"%(i,j))
    outfile.close()
