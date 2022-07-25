import os
import glob


os.chdir("../reduce-chi/ism")

a = glob.glob("*_chi_sq.txt")
a.sort()
d = open("../../result/sherpa-ism-tek.txt", "a")
d.write("id,"+"r-chi,"+"kT,"+"O,"+"Ne,"+"Mg,"+"Si,"+"Fe,"+"Tau_u,"+"norm")

for i in a:
    print(i)
    d.write("\n")
    print(i[:-21])
    d.write(i[:-21]+",")
    search=open(i,"r")
    for line in search:
        if  "Reduced statistic" in line:
####            print(line)
            c = line.split(sep=" ")
            print(c[7])
            d.write(c[7][:-1]+",")

        if "vp3.kT" in line:
####            print(line)
            c = line.split(sep=" ")
            print(c[12])
            d.write(c[12]+",")

        if "vp3.O" in line:
####             print(line)
            c = line.split(sep=" ")
            print(c[13])
            d.write(c[13]+",")

        if "vp3.Ne" in line:
####             print(line)
            c = line.split(sep=" ")
            print(c[12])
            d.write(c[12]+",")

        if "vp3.Mg" in line:
####            print(line)
            c = line.split(sep=" ")
            print(c[12])
            d.write(c[12]+",")

        if "vp3.Si" in line:
####             print(line)
            c = line.split(sep=" ")
            print(c[12])
            d.write(c[12]+",")

        if "vp3.Fe" in line:
####             print(line)
            c = line.split(sep=" ")
            print(c[12])
            d.write(c[12]+",")

        if "vp3.Tau_u" in line:
####             print(line)
            c = line.split(sep=" ")
            print(c[9])
            d.write(c[9]+",")

        if "vp3.norm" in line:
####             print(line)
            c = line.split(sep=" ")
            print(c[10])
            d.write(c[10]+",")


###         if "abs2.nH " in line:
### ####             print(line)  
###             c = line.split(sep=" ")
###             print(c[8])
         
                 