import sys
sys.path.insert(0, '/Users/pluttan/Desktop/проекты/sDAYege/sql/')
from sql import *
import json
from getfileofipi import getfipi

getfipi('http://ege.fipi.ru/os11/xmodules/qprint/qsearch.php?theme_guid=9485b6199541e311a27d001fc68344c9&proj_guid=AC437B34557F88EA4115D2F374B0A07B', 
        'http://ege.fipi.ru/os11/xmodules/qprint/index.php?proj_guid=AC437B34557F88EA4115D2F374B0A07B&theme_guid=9485b6199541e311a27d001fc68344c9&md=qprint&groupno=', 
        0, 
        45)
insertzadan()
data1 = select("fipi",col_to_get=None,no_col="all")
data2 = json.load(open('fipi/fipi.json', 'r'))
for i in data1:
    f=open("fipi/zadania/"+i["idzad"]+".html","w")
    f.write(open("fipi/matcodeforfipi.html").read().replace('hereherehere',data2[i["zad"]]))
    f.close()