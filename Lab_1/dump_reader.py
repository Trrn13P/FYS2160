import sys
def dumpreader(filename):
    infile_dump = open(filename,"r")
    path = filename.split("dump")[0]

    for i in range(3):
        infile_dump.readline()
    num_atoms = eval(infile_dump.readline())

    v_sqrd_average = []
    v_sqrd_current = 0
    infile_dump.readline()
    V = 1
    for i in range(3):
        V *= eval(infile_dump.readline().split()[-1])

    infile_dump.readline()
    for i in range(500):
        line = infile_dump.readline().split()
        vx = eval(line[4])
        vy = eval(line[5])
        vz = eval(line[6])
        v_sqrd_current = vx**2 + vy**2 + vz**2 + v_sqrd_current
    v_sqrd_average.append(v_sqrd_current/num_atoms)


    def reader():
        v_sqrd_current = 0
        for i in range(9):
            infile_dump.readline()
        for i in range(500):
            line = infile_dump.readline().split()
            vx = eval(line[4])
            vy = eval(line[5])
            vz = eval(line[6])
            v_sqrd_current = vx**2 + vy**2 + vz**2 + v_sqrd_current
        return v_sqrd_current/num_atoms

    for i in range(1000):
        v_sqrd_average.append(reader())

    infile_dump.close()


    outfile = open(path+"v_avg_sqrd.txt","w+",)
    outfile.write("Natoms= %g \n"%(num_atoms))
    outfile.write("Volume= %.4f\n"%(V))
    outfile.write("v_sqrd:\n")
    for i in v_sqrd_average:
        outfile.write("%.10f\n"%(i))
    outfile.close()
