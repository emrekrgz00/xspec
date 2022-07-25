import os
import glob

os.chdir("../data/panda")

a = glob.glob("*-b")

for i in a:
    print(i)
    os.chdir(i)
    bashc = "rm *-m-nei3.0.dat"
    os.system(bashc)
    os.chdir("../")