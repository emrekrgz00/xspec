#########################################################################################
#
#					Emre Karagöz
#				    İstanbul university
#				Astronomy and Space Scienci
#				emrekaragoz1@ogr.iu.edu.tr
#				    +90 507 515 24 13
##########################################################################################
from audioop import avg
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
os.chdir("../data/panda")
# data = glob.glob("*-b")
data=[]
data.append("panda-5-11-b")
data.append("panda-5-12-b")
data.append("panda-5-13-b")
data.append("panda-5-14-b")
data.append("panda-5-15-b")
data.append("panda-5-16-b")
data.append("panda-5-17-b")
data.append("panda-5-18-b")
data.append("panda-5-19-b")
data.append("panda-5-20-b")
data.append("panda-5-21-b")
data.append("panda-5-22-b")
data.append("panda-5-23-b")
data.append("panda-5-24-b")
data.append("panda-6-1-b")
data.append("panda-6-2-b")
data.append("panda-6-3-b")
data.append("panda-6-4-b")
data.append("panda-6-5-b")
data.append("panda-6-6-b")
data.append("panda-6-7-b")
data.append("panda-6-8-b")
data.append("panda-6-9-b")
data.append("panda-6-10-b")
data.append("panda-6-11-b")
data.append("panda-6-12-b")
data.append("panda-6-13-b")
data.append("panda-6-14-b")
data.append("panda-6-15-b")
data.append("panda-6-16-b")
data.append("panda-6-12-b")
data.append("panda-6-17-b")
data.append("panda-6-18-b")
data.append("panda-6-19-b")
data.append("panda-6-20-b")
print(len(data))

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
    ignore(None, 0.3)
    ignore(3.0, None)
    set_xlog()
    set_ylog()
    plot_data()  

########### Çift-Model
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
    abs2.nH.freeze()
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
    vp3.kT = 0.59
    vp3.H = 1.0
    vp3.He = 0.89
    vp3.C = 0.303
    vp3.N = 0.123
    vp3.O= 0.17
    vp3.Ne = 0.30
    vp3.Mg = 0.24
    vp3.Si = 0.40
    vp3.S = 0.31
    vp3.Ar = 0.537
    vp3.Ca = 0.339
    vp3.Fe = 0.14
    vp3.Ni = 0.618
    vp3.Tau_l = 0.0
    vp3.Tau_u = 1.32E+11
    vp3.redshift = 0.000875
    vp3.norm = 1
    vp3.kT.freeze()
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
    vp3.Tau_u.freeze()
    vp3.redshift.freeze()
    vp3.norm.thaw()

    vp4 = xsvpshock.vp4()
    vp4.kT = 0.50
    vp4.H = 1.0
    vp4.He = 0.89
    vp4.C = 0.303
    vp4.N = 0.123
    vp4.O = 0.13
    vp4.Ne = 0.20
    vp4.Mg = 0.20
    vp4.Si = 0.28
    vp4.S = 0.31
    vp4.Ar = 0.537
    vp4.Ca = 0.339
    vp4.Fe = 0.15
    vp4.Ni = 0.618
    vp4.Tau_l = 0.0
    vp4.Tau_u = 2.5e+11
    vp4.redshift = 0.000875
    vp4.norm = 1.0
    vp4.kT.thaw()
    vp4.H.freeze()
    vp4.He.freeze()
    vp4.C.freeze()
    vp4.N.freeze()
    vp4.O.freeze()
    vp4.Ne.freeze()
    vp4.Mg.freeze()
    vp4.Si.freeze()
    vp4.S.freeze()
    vp4.Ar.freeze()
    vp4.Ca.freeze()
    vp4.Fe.freeze()
    vp4.Ni.freeze()
    vp4.Tau_l.freeze()
    vp4.Tau_u.freeze()
    vp4.redshift.freeze()
    vp4.norm.thaw()

    model = (abs1 * abs2 * (vp3 + vp4))
    set_model(model)
        # First values
    # aa = vp4.kT.val
    # ab = vp4.O.val
    # ac = vp4.Ne.val
    # ad = vp4.Mg.val
    # ae = vp4.Si.val
    # af = vp4.Fe.val
    # ag = vp4.Tau_u.val
    # # Max-Min values 
    # a = vp4.kT.min
    # b = vp4.kT.max
    # c = vp4.O.min
    # d = vp4.O.max
    # e = vp4.Ne.min
    # f = vp4.Ne.max
    # g = vp4.Mg.min
    # h = vp4.Mg.max
    # k = vp4.Si.min
    # l=  vp4.Si.max
    # m = vp4.Fe.min
    # n = vp4.Fe.max
    # u = vp4.Tau_u.min
    # ü = vp4.Tau_u.max
    fit()

    # vp4.Tau_u.thaw()

    vp4.O.thaw()
    fit()
    vp4.Tau_u.thaw()
    fit()
    vp4.Ne.thaw()
    vp4.Mg.thaw()
    vp4.Si.thaw()
    vp4.Fe.thaw()
    fit()



    show_model(outfile='../../../output/panda-çift/'+str(i[:-2])+'-çift-m_abun.txt', clobber=True)
    show_fit(outfile='../../../reduce-chi/panda-çift/'+str(i[:-2])+'-çift-m_chi_sq.txt', clobber=True)
    # plot_fit_delchi(xlog=True,ylog=False, yerrorbars=False, xerrorbars=False)
    # plt.savefig('../../figures/'+str(i[1:])+'-çift-m.png', dpi=480)
    plot_fit_delchi(xlog=True,ylog=True, yerrorbars=True, xerrorbars=True)
    plt.savefig('../../../figures/panda-çift/'+str(i[:-2])+'-çift-m.png', dpi=480)

#     set_conf_opt("sigma", 2.6)
#     set_conf_opt("max_rstat", 40)
#     #set_conf_opt("verbose", "1")
#     #set_conf_opt('soft_limits', True)
#     #set_conf_opt('parallel', False)
#     conf(vp3.norm,vp4.O, vp4.Ne, vp4.Mg, vp4.Si, vp4.Fe, vp4.kT, vp4.Tau_u, vp4.norm)
#     show_conf(outfile='../../../output/'+str(i[:-11])+'-çift-m-_confi_err.txt', clobber=True)

#     set_covar_opt('sigma', 2.6)
#     set_covar_opt('maxiters', 200)
#     #set_covar_opt('soft_limits', True)
#     covar(vp3.norm,vp4.O, vp4.Ne, vp4.Mg, vp4.Si, vp4.Fe, vp4.kT, vp4.Tau_u, vp4.norm)
#     show_covar(outfile='../../../output/'+str(i[:-11])+'-çift-m_covar.txt', clobber=True)


    # #set_proj_opt('parallel', False)
    # #set_proj_opt('soft_limits', True)
    # set_proj_opt("max_rstat", 40)
    # set_proj_opt("sigma", 2.0)
    # proj(vp3.norm,vp4.O, vp4.Ne, vp4.Mg, vp4.Si, vp4.Fe, vp4.kT, vp4.Tau_u, vp4.norm)
    # show_conf(outfile='../../output/'+str(i[:-11])+'-çift-m_proj_err.txt', clobber=True)

#######################################################################################    
    
#     clean()  
    os.chdir("../") 
