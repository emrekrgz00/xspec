import os
import glob
from re import X

os.chdir("../data/reg/panda")

a = glob.glob("*.reg")
a.remove("bkg.reg")

print(len(a))

for i in a:
    print(i)
    b =open(i,"r")
    for line in b:
        c=line[4:-2]
        d=c.split(sep=",")
        x=d[2]
        y=d[3]
        z=d[0]
        v=d[1]
        f=d[4]
        g=d[5]
        aa = (x[:-1])
        ab = (y[:-1])
        print(aa)
        print(ab)




#     # c =b[5:-3].split(sep=",")
#     # x = float(c[2])
#     # y = float(c[3])
#     # print(x)
#     # print(y)
