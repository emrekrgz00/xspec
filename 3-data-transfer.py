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
os.chdir("../obsid/777/repro/")

bashcommandlis = "cp -i *.lis /media/selcuk/Elements/emre-TEZ/data"
bashcommandfits = "cp -i *.fits /media/selcuk/Elements/emre-TEZ/data"
os.system(bashcommandlis)
os.system(bashcommandfits)