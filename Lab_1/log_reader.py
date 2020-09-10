import sys
def logreader(filename):
    path = filename.split("log")[0]

    pressure = []
    E_tot = []
    infile_log = open(filename,"r")
    for i in range(134):
        infile_log.readline()
    for line in infile_log:
        if line[0]=="L":
            break
        else:
            pressure.append(eval(line.split()[-1]))
            E_tot.append(eval(line.split()[-2]))
    infile_log.close()

    outfile = open(path+"log_pressure.txt","w+")
    outfile.write("Pressure:\n")
    for i in pressure:
        outfile.write("%.10f\n"%(i))
    outfile.close()

    outfile = open(path+"log_E.txt","w+")
    outfile.write("E:\n")
    for i in E_tot:
        outfile.write("%.10f\n"%(i))
    outfile.close()
