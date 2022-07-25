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
import matplotlib.pyplot as plt
###########################################################################################
os.chdir("../data/ism")
data = glob.glob("*-b")
data.sort()
#print(data)



for i in data:
    print(i)
    print(i[:-2])
    os.chdir(i)
    a =glob.glob("*_src_grp.pi")

    print(a[0])
    load_pha(a[0])
    set_xsxset("NEIVERS", "3.0.4")
    set_stat("Chi2Xspecvar")
    subtract()
    set_analysis("energy")
    ignore(None, 0.34)
    ignore(3.0, None)
    set_xlog()
    set_ylog()
    plot_data()
   
    abs1 = xsphabs.abs1()
    abs1.nH = 0.17
    abs1.nH.freeze()
    
    abs2 = xsvphabs.abs2()
    abs2.nH = 0.03
    abs2.He = 0.89
    abs2.C = 0.303
    abs2.N = 0.123
    abs2.O = 0.13
    abs2.Ne = 0.20
    abs2.Na = 0.30
    abs2.Mg = 0.20
    abs2.Al = 0.30
    abs2.Si = 0.28
    abs2.S = 0.31
    abs2.Cl = 0.31
    abs2.Ar = 0.537
    abs2.Ca = 0.339
    abs2.Cr = 0.61
    abs2.Fe = 0.15
    abs2.Co = 0.30
    abs2.Ni = 0.618
    abs2.nH.thaw()
    abs2.He.freeze()
    abs2.C.freeze()
    abs2.N.freeze()
    abs2.O.freeze()
    abs2.Ne.freeze()
    abs2.Na.freeze()
    abs2.Mg.freeze()
    abs2.Al.freeze()
    abs2.Si.freeze()
    abs2.S.freeze()
    abs2.Cl.freeze()
    abs2.Ar.freeze()
    abs2.Ca.freeze()
    abs2.Cr.freeze()
    abs2.Fe.freeze()
    abs2.Co.freeze()
    abs2.Ni.freeze()
    
    vp3 = xsvpshock.vp3()
    vp3.kT = 0.30
    vp3.H = 1.0
    vp3.He = 0.89
    vp3.C = 0.303
    vp3.N = 0.123
    vp3.O= 0.13
    vp3.Ne = 0.20
    vp3.Mg = 0.20
    vp3.Si = 0.28
    vp3.S = 0.31
    vp3.Ar = 0.537
    vp3.Ca = 0.339
    vp3.Fe = 0.15
    vp3.Ni = 0.618
    vp3.Tau_l = 0.0
    vp3.Tau_u = 1.0e+10
    vp3.redshift = 0.000875
    vp3.norm = 1
    vp3.kT.thaw()
    vp3.H.freeze()
    vp3.He.freeze()
    vp3.C.freeze()
    vp3.N.freeze()
    vp3.O.freeze()
    vp3.Ne.freeze()
    vp3.Mg.freeze()
    vp3.Si.freeze()
    vp3.S.freeze()
    vp3.Ar.freeze()
    vp3.Ca.freeze()
    vp3.Fe.freeze()
    vp3.Ni.freeze()
    vp3.Tau_l.freeze()
    vp3.Tau_u.thaw()
    vp3.redshift.freeze()
    vp3.norm.thaw()
    
    model = (abs1 * abs2 * vp3)
    
    set_model(model)
    fit()
    thaw(vp3.O)
    fit()
    thaw(vp3.Ne)
    fit()
    thaw(vp3.Mg)
    fit()
    thaw(vp3.Si)
    fit()
    #thaw(vp3.S)
    #fit()
    thaw(vp3.Fe)
    fit()
   
    show_model(outfile="../../../output/ism/"+str(i[:-2])+"_tek-model.txt", clobber=True)
    show_fit(outfile="../../../reduce-chi/ism/"+str(i[:-2])+"_tek-model_chi_sq.txt", clobber=True)
    plot_fit_delchi(xlog=True ,ylog=True, yerrorbars=True, xerrorbars=True)
    plt.savefig('../../../figures/ism/'+str(i[:-2])+'_tekmodel'+'.png', dpi=480)
    
    # # set_covar_opt('sigma', 2.6)
    # # set_covar_opt('maxiters', 200)
    # # ##set_covar_opt('soft_limits', True)
    # # covar(abs2.nH, vp3.O, vp3.Ne, vp3.Mg, vp3.Si, vp3.Fe, vp3.kT, vp3.Tau_u, vp3.norm)
    # # show_covar(outfile='../../../output/'+str(i[:-2])+'_tek-model_covar.txt', clobber=True)
    
    # # set_conf_opt("sigma", 2.6)
    # # set_conf_opt("max_rstat", 40)
    # # ##set_conf_opt('soft_limits', True)
    # # ##set_conf_opt('parallel', False)
    # # conf(abs2.nH,vp3.O, vp3.Ne, vp3.Mg, vp3.Si, vp3.Fe, vp3.kT, vp3.Tau_u, vp3.norm)
    # # show_conf(outfile='../../../output/'+str(i[:-2])+'_tek-model_confi.txt', clobber=True)       
    
    # # set_proj_opt('parallel', False)
    # # set_proj_opt('soft_limits', True)
    # # set_proj_opt("max_rstat", 40)
    # # set_proj_opt("sigma", 2.0)
    # # proj(vp3.O, vp3.Ne)
    # # show_conf(outfile='../../../output/'+str(i[:-2])+'_tek-model_proj_err.txt', clobber=True)
    # clean()

    os.chdir("../")
