import numpy as np
import matplotlib.pyplot as plt

"""
DET ER LAGT INN f=4 FOR CO2, SPØR PÅ LAB OM DETTE ER RIKTIG, BURDE VÆRT 5 SYNS JEG
"""


def c_id(T,f,M_mol):
    return np.sqrt(((f+2)*R*T)/(f*M_mol))

R = 8.3144598 #J/Kmol

#first value is M_mol, second is f
atom_values = {"Hydrogen":[2.01588 * 1e-3, 3],\
"Helium":[4.002602 * 1e-3, 3],\
"Neon":[20.12 * 1e-3, 3],\
"Argon":[39.948 * 1e-3, 3],\
"Nitrogen":[14.0067 * 1e-3, 3],\
"Oxygen":[15.999 * 1e-3, 3],\
"Air":[28.97 * 1e-3, 5],\
"CO2":[44.009 * 1e-3, 5],\
"Amonia":[17.0304 * 1e-3, 6]}

#amonia er ikke linear, air er linear, co2 er ?
"""
N = int(1E4)
T = np.linspace(100,1000,N)

for i in atom_values:
    M_mol_ = atom_values[i][0]
    f_ = atom_values[i][1]
    plt.plot(T,c_id(T,f_,M_mol_),label="%s"%(i))
plt.xlabel("T [K]",FontSize=14)
plt.ylabel(r"$c_{id}(T)$",FontSize=14)
plt.legend()
plt.savefig("mol_mot_f.png")
plt.clf()
"""


"""
outfile = open("mol_k.txt","w+")
outfile.write('\\begin{table}[h!]\n')
outfile.write("\\caption{tabell}\\label{table:mol_k}\n")
outfile.write("\\begin{tabular}{|c|c|c|}\n")
outfile.write("\\hline\n")
outfile.write("Molecule & Molecular weight [kg/mol] & Degree of freedom \\\ \n")

for i in atom_values:
    x,y = atom_values[i]
    outfile.write("%s & %.4f & %g \\\ \n"%(i,x,y))
    outfile.write("\\hline \n")

outfile.write("\\end{tabular}\n")
outfile.write("\\end{table}")
outfile.close()
"""
