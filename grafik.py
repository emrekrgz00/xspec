from cmath import tau
import numpy as np
from astropy.io import ascii
import pandas as pd
import matplotlib.pyplot as plt

# data = ascii.read("../data/panda/"+"emre.csv", delimiter="\s+")
# data = ascii.read("../data/panda/"+"panda-nei3.0-çift.txt", delimiter="\s+")

#data = pd.read_excel("../data/panda/"+"panda-çift-tek.ods")

data = pd.read_csv("../data/panda/"+"panda-nei3.0-çift-4-5.txt", delimiter="\t" )


# name = np.array(data["id"])

name = np.arange(1,9,1)
kt = np.array(data["kT"])
tau_u = np.array(data["Tau_u"])
O = np.array(data["O"])
Ne = np.array(data["Ne"])
Mg = np.array(data["Mg"])
Si = np.array(data["Si"])
Fe = np.array(data["Fe"])

# plt.axline(xy1=(31,0), xy2=(31,0.4), slope=None, linewidth=2, color="r")
# plt.axline(xy1=(53,0), xy2=(53,0.4), slope=None, linewidth=2, color="r")
# plt.axline(xy1=(79,0), xy2=(79,0.4), slope=None, linewidth=2, color="r")
# plt.axline(xy1=(99,0), xy2=(99,0.4), slope=None, linewidth=2, color="r")
# plt.axline(xy1=(123,0), xy2=(123,0.4), slope=None, linewidth=2, color="r")
# plt.axline(xy1=(145,0), xy2=(145,0.4), slope=None, linewidth=2, color="r")

plt.plot(name, tau_u)
plt.title("Tau_u")
plt.xlabel("Toplam_Bölge")
plt.ylabel("Tau_u")
# plt.savefig("../figures/"+"total-Tau_u.png")


plt.show()
