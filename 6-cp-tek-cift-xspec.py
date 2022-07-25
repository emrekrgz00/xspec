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
import pandas as pd
import numpy as np
import os
import subprocess
import string
###########################################################################################

bashcp1="cp -i xspec-çift-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-cift/ism"
bashcp2="cp -i xspec-çift-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
bashcp3="cp -i xspec-çift-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-cift/özel2"
bashcp4="cp -i xspec-çift-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-cift/panda"

os.system(bashcp1)
os.system(bashcp2)
os.system(bashcp3)
os.system(bashcp4)

bashcp5="cp -i xspec-tek-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-tek/ism"
bashcp6="cp -i xspec-tek-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
bashcp7="cp -i xspec-tek-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-tek/özel2"
bashcp8="cp -i xspec-tek-m-script.tcl /media/selcuk/Elements/emre-TEZ/xspec-tek/panda"

os.system(bashcp5)
os.system(bashcp6)
os.system(bashcp7)
os.system(bashcp8)



