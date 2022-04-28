import pymysql.cursors  #doks: https://pypi.org/project/PyMySQL/
from time import time
import sys
sys.path.insert(0, '/Users/pluttan/Desktop/проекты/sDAYege/')
from obrmes import conv_to_dict
import json

# Connect to the database


def onbase(r):
    print(type(r))
    if str(type(r))[8:12]!="list":r=[r]
    connection = pymysql.connect(host='localhost',
                                user='root',
                                read_default_file="/opt/homebrew/etc/my.cnf",
                                password='Pluttan2004',
                                database='mainbot',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        res = []
        for i in r:
            with connection.cursor() as cursor:
                cursor.execute(i)
                while True:
                    a=cursor.fetchone()
                    if a!=None:res.append(a)
                    else:break
                    
            connection.commit()
    return res


def newuser(d):
    sql = insert("users",4)
    sql2 = 'SELECT * FROM users;'
    p=onbase(sql2)
    print(p[-1]['uid'])
    onbase(sql.format(d['from_user']['id'],
                       p[-1]['uid']+1,
                       d['from_user']['first_name'],
                       d['from_user']['last_name'],
                       time()))
    return "new user "+d['from_user']['first_name']


def getuser(d):
    sql = 'SELECT * FROM users WHERE userid="{0}";'
    ans = onbase([sql.format(d['from_user']['id'])])
    if ans == []:
        return newuser(d)
    else:
        return ans

def insert(table,noper):
    sql="INSERT INTO {0} VALUES ({1})"
    per=""
    for i in range(noper):per+=", '{"+str(i)+"}'"  
    return sql.format(table,per[2:])

def select(table,whatcol=None,wherecol=None,where=None,col_to_get="uid",no_col=0):
    sql="select {0} from "+table
    if where!=None:
        sql+=" where "+wherecol+"="+str(where)
    sql.format(whatcol if whatcol!=None else "*")
    try:
        a=onbase([sql.format(whatcol if whatcol!=None else "*")])
        if no_col=="all":
            if col_to_get!=None:return [i[col_to_get] for i in a]
            else:return a
        else:
            if col_to_get!=None:return a[no_col][col_to_get]
            else:return a[no_col]
    except IndexError:return {}

def newmessage(d):
    sql = insert("messages",6)
    onbase(sql.format(d['from_user']['id'],
                       getuid(d),
                       d['message_id'],
                       1 if d['reply_to_message']!="null" else 0,
                       time(),
                       "'{}'".format(d["text"])))
    
def getuid(d):
    return select("users","uid","userid",d['from_user']['id'])

def insertzadan():
    data1 = json.load(open('fipi/fipi.json', 'r'))
    for k, v in data1.items():
        data2 =select("fipi",col_to_get=None,no_col="all")
        mas=[]
        for i in data2:
            mas.append(int(i["idzad"]))
            if k==i["zad"]:break
        else:
            id=str(max(mas)+1)
            while len(id)<6:id="0"+id
            onbase(insert("fipi", 2).format(id,k))
#insertzadan()