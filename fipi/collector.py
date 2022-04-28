import sys
sys.path.insert(0, '/Users/pluttan/Desktop/проекты/sDAYege/sql/')
from sql import *
import json

data1 = select("fipi",col_to_get=None,no_col="all")
data2 = json.load(open('fipi/fipi.json', 'r'))
for i in data1:
    f=open("fipi/zadania/"+i["idzad"]+".html","w")
    f.write(open("fipi/matcodeforfipi.html").read()+data2[i["zad"]]+"</body></html>")
    f.close()