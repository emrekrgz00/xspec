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
os.mkdir("../xspec-tek/panda/")
os.mkdir("../xspec-cift/panda/")
os.chdir("../data")

a =glob.glob("*panda*")
print(len(a))

for i in a:
    print(i)
    os.chdir(i)
    bashcdarf = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-tek/panda"
    bashcdrmf = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-tek/panda"
    bashcdpi  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-tek/panda"
    os.system(bashcdarf)
    os.system(bashcdrmf)
    os.system(bashcdpi)
    bashcdarf2 = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-cift/panda"
    bashcdrmf2 = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-cift/panda"
    bashcdpi2  = "cp -i *.pi  media/selcuk/Elements/emre-TEZ/xspec-cift/panda"
    os.system(bashcdarf2)
    os.system(bashcdrmf2)
    os.system(bashcdpi2)
    os.chdir("../")


os.mkdir("../xspec-tek/özel/")
os.mkdir("../xspec-cift/özel/")

b = glob.glob("*kulak*")
print(len(b))

c = glob.glob("*kuyruk*")
print(len(b))

for i in b:
    print(i)
    os.chdir(i)
    bashcdarf = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
    bashcdrmf = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
    bashcdpi  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
    os.system(bashcdarf)
    os.system(bashcdrmf)
    os.system(bashcdpi)
    bashcdarf2 = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
    bashcdrmf2 = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
    bashcdpi2  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
    os.system(bashcdarf2)
    os.system(bashcdrmf2)
    os.system(bashcdpi2)
    os.chdir("../")

for i in c:
    print(i)
    os.chdir(i)
    bashcdarf = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
    bashcdrmf = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
    bashcdpi  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-tek/özel"
    os.system(bashcdarf)
    os.system(bashcdrmf)
    os.system(bashcdpi)
    bashcdarf2 = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
    bashcdrmf2 = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
    bashcdpi2  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-cift/özel"
    os.system(bashcdarf2)
    os.system(bashcdrmf2)
    os.system(bashcdpi2)
    os.chdir("../")

os.mkdir("../xspec-tek/ism/")
os.mkdir("../xspec-cift/ism/")
d = glob.glob("*ısm*")

for i in d:
    os.chdir(i)
    bashcdarf = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-tek/ism"
    bashcdrmf = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-tek/ism"
    bashcdpi  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-tek/ism"
    os.system(bashcdarf)
    os.system(bashcdrmf)
    os.system(bashcdpi)
    bashcdarf2 = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-cift/ism"
    bashcdrmf2 = "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-cift/ism"
    bashcdpi2  = "cp -i *.pi  /media/selcuk/Elements/emre-TEZ/xspec-cift/ism"
    os.system(bashcdarf2)
    os.system(bashcdrmf2)
    os.system(bashcdpi2)
    os.chdir("../")

os.mkdir("../xspec-tek/özel2/")
os.mkdir("../xspec-cift/özel2/")
j = 0
for i in range(1,12,1):
    j +=1
    os.chdir(str(j)+"-b")
    print(str(j)+"-b")
    bashcp = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-cift/özel2"
    bashcp1= "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-cift/özel2"
    bashcp2= "cp -i *.pi /media/selcuk/Elements/emre-TEZ/xspec-cift/özel2"

    bashcp3 = "cp -i *.arf /media/selcuk/Elements/emre-TEZ/xspec-tek/özel2"
    bashcp4= "cp -i *.rmf /media/selcuk/Elements/emre-TEZ/xspec-tek/özel2"
    bashcp5= "cp -i *.pi /media/selcuk/Elements/emre-TEZ/xspec-tek/özel2"

    os.system(bashcp)
    os.system(bashcp1)
    os.system(bashcp2)
    os.system(bashcp3)
    os.system(bashcp4)
    os.system(bashcp5)

    os.chdir("../")
