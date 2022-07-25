import os
import glob


os.chdir("../reduce-chi/panda-çift")

a = glob.glob("*_chi_sq.txt")
a.sort()
d = open("../../result/sherpa-panda-çift.txt", "a")
d.write("id,"+"r-chi,"+"kT,"+"O,"+"Ne,"+"Mg,"+"Si,"+"Fe,"+"Tau_u,"+"ejekta-norm,"+"ism-norm")

for i in a:
    print(i)
#    d.write("\n")
    print(i[:-18])
    d.write(i[:-18]+",")
    search=open(i,"r")
    for line in search:
        if  "Reduced statistic" in line:
####            print(line)
            c = line.split(sep=" ")
            print(c[7][:-1])
            d.write(c[7][:-1]+",")

        if "vp3.norm" in line:
####             print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[10])
                d.write(c[10]+",")

        if "vp4.kT" in line:
####            print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[12])
                d.write(c[12]+",")

        if "vp4.O" in line:
#########            print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[13])
                d.write(c[13]+",")

        if "vp4.Ne" in line:
####             print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[12])
                d.write(c[12]+",")

        if "vp4.Mg" in line:
####            print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[12])
                d.write(c[12]+",")

        if "vp4.Si" in line:
####             print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[12])
                d.write(c[12]+",")

        if "vp4.Fe" in line:
####             print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[12])
                d.write(c[12]+",")

        if "vp4.Tau_u" in line:
####             print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[9])
                d.write(c[9]+",")

        if "vp4.norm" in line:
####             print(line)
            if "WARNING" in line:
                print(line)
            else:    
                c = line.split(sep=" ")
                print(c[10])
                d.write(c[10]+",")
                




###         if "abs2.nH " in line:
### ####             print(line)  
###             c = line.split(sep=" ")
###             print(c[8])
         

