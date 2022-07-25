#########################################################################################
#
#					Emre Karagöz
#				    İstanbul university
#				Astronomy and Space Scienci
#				emrekaragoz1@ogr.iu.edu.tr
#				    +90 507 515 24 13
##########################################################################################
from os import sep
import pandas as pd
import numpy as np
import glob
import os

os.chdir("../data/panda")

a = glob.glob("*-b")
a.sort()
d = open("panda-nei3.0-tek-new.txt","a")
d.write("id,chi,r-chi,dof,r-dof,kT,kT-err,kT+err,O,O-err,O+err,Ne,Ne-err,Ne+err,Mg,Mg-err,Mg+err,Si,Si-err,Si+err,Fe,Fe-err,Fe+err,Tau_u,Tau_u-err,Tau_u+err,nH,nH-err,nH+err,Norm,Norm-err,Norm+err")

for i in a:
    d.write("\n")
    d.write(i[:-2]+",")
    print(i)
    print(i[4:-2])
    print("ISM"+i[4:-2]+"-nei3.0.dat")
    print("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat")    
    os.chdir(i)
#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- chi-square" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- dof" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- kT" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- O" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- Ne" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- Mg" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- Si" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- Fe" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- Tau" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- nH" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

#    b =open("ISM"+i[4:-2]+"-nei2.0.dat", "r")
#    b =open("ISM"+i[4:-2]+"-nei3.0.4.dat", "r")
    b=open("panda"+i[5:-2]+"-tek-m-respect-nei3.0.dat","r")
    for line in b:
        if "--- Norm" in line:
            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()




    os.chdir("../")
