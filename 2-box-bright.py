#########################################################################################
#
#					Emre Karagöz
#				    İstanbul university
#				Astronomy and Space Scienci
#				emrekaragoz1@ogr.iu.edu.tr
#				    +90 507 515 24 13
##########################################################################################
from ciao_contrib.runtool import *
from ciao_contrib.runtool import acis_process_events, dmstat, dmmerge
import ciao_contrib.runtool
import ciao_contrib.runtool as rt
from ciao_contrib.cda.data import download_chandra_obsids
import os
import glob
import shutil
import pandas as pd
import numpy as np
import os
import subprocess
import string
###########################################################################################
os.chdir("../obsid")

a = glob.glob("*")
a.remove("obj_box.reg")
a.remove("bright_c7.reg")
#print(a)
for i in a:
    print(i)
    shutil.copy("obj_box.reg", "/media/selcuk/NA/deneme/obsid/"+i+"/repro/")
    shutil.copy("bright_c7.reg", "/media/selcuk/NA/deneme/obsid/"+i+"/repro/")

    os.chdir(i+"/repro/")
    b = glob.glob("*_repro_evt2.fits")
    print(b)
    print(b[0])
    dmcopy(infile=b[0]+"[energy=300:10000,sky=region(obj_box.reg)]",
    outfile=b[0][:-5]+"_03-10_obj-box.fits"  )

    dmextract(infile=b[0][:-5]+"_03-10_obj-box.fits[exclude sky=region(bright_c7.reg)][bin time=::500]",
    outfile="lc_"+b[0][:-5]+"_c7.fits", opt="ltc1")

    deflare(infile="lc_"+b[0][:-5]+"_c7.fits", outfile="lc_"+b[0][:-5]+"_c7.txt",
    method="sigma", plot="yes", nsigma=3,
    save="lc_"+b[0][:-5]+"_c7.png")
    
    dmlist("lc_"+b[0][:-5]+"_c7.fits"+"[GTI7]", opt="data", outfile="lc_"+b[0][:-5]+"_data.txt" )

    f = open("lc_"+b[0][:-5]+"_data.txt", "r")
    g = open("lc_"+b[0][:-5]+"_data2.txt", "a")
    for line in f:
        if "1" in line:
            print(line)
            g.write(line)
            g.close()
            d = pd.read_csv("lc_"+b[0][:-5]+"_data2.txt", sep="\s+", usecols=[0,1,2], index_col=False)
            d.to_csv("lc_"+b[0][:-5]+"_data3.txt",index_label=None,index=False)
            h = np.loadtxt("lc_"+b[0][:-5]+"_data3.txt", delimiter=",")
            print("lc_"+b[0][:-5]+"_data3.txt  bu texte göre temizleme yap.")
            print("""
            punlearn dmcopy
            dmcopy "b[0][:-5]+"_03-10_obj-box.fits"[time=173910843.83588001:173956843.83588001,
            173957343.83588001:173966343.83588001]" acisf04440_repro_evt2_obj-box3_dmcopy.fits

            dmkeypar acisf04440_repro_evt2_obj-box3_dmcopy.fits EXPOSURE echo+
            """)
    os.chdir("../../")