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
a.remove("panda-1-1-b")
a.remove("panda-1-2-b")
a.remove("panda-1-3-b")
a.remove("panda-1-4-b")
a.remove("panda-1-5-b")
a.remove("panda-1-6-b")
a.remove("panda-1-7-b")
a.remove("panda-1-8-b")
a.remove("panda-1-9-b")
a.remove("panda-1-10-b")
a.remove("panda-1-11-b")
a.remove("panda-1-12-b")
a.remove("panda-1-13-b")
a.remove("panda-1-14-b")
a.remove("panda-1-15-b")
a.remove("panda-1-16-b")
a.remove("panda-1-17-b")
a.remove("panda-1-18-b")
a.remove("panda-1-19-b")
a.remove("panda-1-20-b")
a.remove("panda-1-21-b")
a.remove("panda-1-22-b")
a.remove("panda-1-23-b")
a.remove("panda-1-24-b")
a.remove("panda-1-25-b")
a.remove("panda-1-26-b")
a.remove("panda-1-27-b")
a.remove("panda-1-28-b")
a.remove("panda-1-29-b")
a.remove("panda-1-30-b")
a.remove("panda-1-31-b")
a.remove("panda-2-1-b")
a.remove("panda-2-2-b")
a.remove("panda-2-3-b")
a.remove("panda-2-4-b")
a.remove("panda-2-5-b")
a.remove("panda-2-6-b")
a.remove("panda-2-7-b")
a.remove("panda-2-8-b")
a.remove("panda-2-9-b")
a.remove("panda-2-10-b")
a.remove("panda-2-11-b")
a.remove("panda-2-12-b")
a.remove("panda-2-13-b")
a.remove("panda-2-14-b")
a.remove("panda-2-15-b")
a.remove("panda-2-16-b")
a.remove("panda-2-17-b")
a.remove("panda-2-18-b")
a.remove("panda-2-19-b")
a.remove("panda-2-20-b")
a.remove("panda-2-21-b")
a.remove("panda-2-22-b")
a.remove("panda-3-1-b")
a.remove("panda-3-2-b")
a.remove("panda-3-3-b")
a.remove("panda-3-4-b")
a.remove("panda-3-5-b")
a.remove("panda-3-6-b")
a.remove("panda-3-7-b")
a.remove("panda-3-8-b")
a.remove("panda-3-9-b")
a.remove("panda-3-10-b")
a.remove("panda-3-11-b")
a.remove("panda-3-12-b")
a.remove("panda-3-13-b")
a.remove("panda-3-14-b")
a.remove("panda-3-15-b")
a.remove("panda-3-16-b")
a.remove("panda-3-17-b")
a.remove("panda-3-18-b")
a.remove("panda-3-19-b")
a.remove("panda-3-20-b")
a.remove("panda-3-21-b")
a.remove("panda-3-22-b")
a.remove("panda-3-23-b")
a.remove("panda-3-24-b")
a.remove("panda-3-25-b")
a.remove("panda-3-26-b")
a.remove("panda-4-9-b")
a.remove("panda-4-10-b")
a.remove("panda-4-11-b")
a.remove("panda-4-12-b")
a.remove("panda-4-13-b")
a.remove("panda-4-14-b")
a.remove("panda-4-15-b")
a.remove("panda-4-16-b")
a.remove("panda-4-17-b")
a.remove("panda-4-18-b")
a.remove("panda-4-19-b")
a.remove("panda-4-20-b")
a.remove("panda-4-21-b")
a.remove("panda-5-1-b")
a.remove("panda-5-2-b")
a.remove("panda-5-3-b")
a.remove("panda-5-4-b")
a.remove("panda-5-5-b")
a.remove("panda-5-6-b")
a.remove("panda-5-7-b")
a.remove("panda-5-8-b")
a.remove("panda-5-9-b")
a.remove("panda-5-10-b")
a.remove("panda-5-11-b")
a.remove("panda-5-12-b")
a.remove("panda-5-13-b")
a.remove("panda-5-14-b")
a.remove("panda-5-15-b")
a.remove("panda-5-16-b")
a.remove("panda-5-17-b")
a.remove("panda-5-18-b")
a.remove("panda-5-19-b")
a.remove("panda-5-20-b")
a.remove("panda-5-21-b")
a.remove("panda-5-22-b")
a.remove("panda-5-23-b")
a.remove("panda-5-24-b")
a.remove("panda-6-1-b")
a.remove("panda-6-2-b")
a.remove("panda-6-3-b")
a.remove("panda-6-4-b")
a.remove("panda-6-5-b")
a.remove("panda-6-6-b")
a.remove("panda-6-7-b")
a.remove("panda-6-8-b")
a.remove("panda-6-9-b")
a.remove("panda-6-10-b")
a.remove("panda-6-11-b")
a.remove("panda-6-12-b")
a.remove("panda-6-13-b")
a.remove("panda-6-14-b")
a.remove("panda-6-15-b")
a.remove("panda-6-16-b")
a.remove("panda-6-17-b")
a.remove("panda-6-18-b")
a.remove("panda-6-19-b")
a.remove("panda-6-20-b")


a.sort()
d = open("panda-nei3.0-çift-just4.txt","a")
d.write("id,chi,dof,kT,kT-err,kT+err,O,O-err,O+err,Ne,Ne-err,Ne+err,Mg,Mg-err,Mg+err,Si,Si-err,Si+err,Fe,Fe-err,Fe+err,Tau_u,Tau_u-err,Tau_u+err,nH,nH-err,nH+err,Norm,Norm-err,Norm+err")

for i in a:
    d.write("\n")
    d.write(i[:-2]+",")
    print(i)
    print(i[6:-2])
    print("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat")
    os.chdir(i)
############### CHİ-SQUARE    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-chi-square" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-chi-square" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

##############   DOF
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-dof" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-dof" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()    

################# KT
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-kT" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-kT-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-kT+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-kT" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-kT-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-kT+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()     

####################### Oksijen    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-O" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-O-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-O+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-O" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-O-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-O+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()     

####################### NEON  
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-Ne" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Ne-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Ne+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-Ne" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Ne-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Ne+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

####################### Magnezyum  
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-Mg" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Mg-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Mg+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-Mg" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Mg-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Mg+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

####################### Silisyum
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-Si" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Si-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Si+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-Si" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Si-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Si+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

####################### Demir
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-Fe" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Fe-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Fe+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-Fe" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Fe-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-rerror-Fe+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close() 

####################### TAu_u
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-Tau_u" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Tau_u-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-Tau_u+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-thaw-53-Tau_u" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "----low53-thaw-53-rerror-Tau_u-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "----low53-thaw-53-rerror-Tau_u+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[1])
            d.write(c[1]+",")
    b.close()     

########################### NORM

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-ejekta-norm " in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-ejekta-norm-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---high53-rerror-ejekta-norm+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()


    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "---low53-thaw-53-ejekta-norm" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 

    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "----low53-thaw-53-rerror-ejekta-norm-err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close() 
    
    b =open("panda-"+i[6:-2]+"-cift-m-newnei3.0.dat", "r")
    for line in b:
        if "----low53-thaw-53-rerror-ejekta-norm+err" in line:
#            print(line)
            c = line.split(sep=" ")
            print(c[2])
            d.write(c[2]+",")
    b.close()     
    
    os.chdir("../")