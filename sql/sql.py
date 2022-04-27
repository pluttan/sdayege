import pymysql.cursors  #doks: https://pypi.org/project/PyMySQL/
from time import time
from obrmes import conv_to_dict

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
    for i in range(noper):per+=", {"+str(i)+"}"  
    return sql.format(table,per[2:])

def select(table,whatcol=None,wherecol=None,where=None):
    sql="select {0} from "+table
    if where!=None:
        sql+=" where "+wherecol+"="+str(where)
    print(sql.format(whatcol if whatcol!=None else "*"))
    return onbase([sql.format(whatcol if whatcol!=None else "*")])[0]['uid']


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
