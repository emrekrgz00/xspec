#########################################################################################
#
#					Emre Karagöz
#				    İstanbul university
#				Astronomy and Space Scienci
#				emrekaragoz1@ogr.iu.edu.tr
#				    +90 507 515 24 13
##########################################################################################
from tabnanny import verbose
from ciao_contrib.runtool import *
from ciao_contrib.runtool import acis_process_events, dmstat, dmmerge
import ciao_contrib.runtool
import ciao_contrib.runtool as rt
from ciao_contrib.cda.data import download_chandra_obsids
import os
import glob
import shutil
#import pandas as pd
import numpy as np
import os
import subprocess
import string
###########################################################################################

os.chdir("../data/ism")
a = glob.glob("*.reg")
a.remove("bkg.reg")
a.remove("ISM-1.reg")
a.remove("ISM-2.reg")
a.remove("ISM-3.reg")
a.remove("ISM-4.reg")
a.remove("ISM-5.reg")
a.remove("ISM-6.reg")

print(len(a))

for i in a:
    print(i)
    print(i[:-4]+"-b")
    os.mkdir(i[:-4]+"-b")
    specextract(infile="acisf00777_repro_evt2_obj-box_dmcopy.fits[sky=region("+i+")]", 
    outroot=i[:-4]+"-b/"+i[:-4], 
    bkgfile="acisf00777_repro_evt2_obj-box_dmcopy.fits[sky=region(bkg.reg)]",
    asp="pcadf00777_000N001_asol1.fits", mskfile="acisf00777_000N005_msk1.fits",
    badpixfile="acisf00777_repro_bpix1.fits", weight="yes", correct="no", combine="yes",
    grouptype="NUM_CTS", binspec=20, verbose=2, clobber="no")

    dmgroup(infile=i[:-4]+"-b/"+i[:-4]+"_grp.pi", outfile=i[:-4]+"-b/"+i[:-4]+"_src_grp.pi",
    grouptype="NUM_CTS", grouptypeval=int(20), binspec="", 
    xcolumn="channel", ycolumn="counts")

