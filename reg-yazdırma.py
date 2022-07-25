import os
import glob



os.chdir("../data/panda")

a = glob.glob("*panda-6-*")
a.sort()
b = open("toplu-6-direction.reg", "a")
print(len(a))

for i in a:
    print(i)
    search=open(i,"r")
    for line in search:
        if "pie" in line:
            b.write(line[:-1]+" "+"#"+i+"\n")
            print(line)