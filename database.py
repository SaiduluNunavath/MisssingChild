import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="mc")
    c = _conn.cursor()

    return c, _conn



def viewadata():
    c, conn = db_connect()
    c.execute("select image,uid from aupload  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def getmail(uid):
    c, conn = db_connect()
    c.execute("select email from authority where uid ='"+uid+"'   ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def vm1(uid):
    c, conn = db_connect()
    c.execute("select * from message where uid ='"+uid+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def vc1(uid):
    c, conn = db_connect()
    c.execute("select * from aupload where uid ='"+uid+"'   ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result
# -------------------------------Registration-----------------------------------------------------------------

def inc_reg(oname,uid,password,email,mobile):
    try:
        c, conn = db_connect()
        print(oname,uid,password,email,mobile)
        id="0"
        status = "pending"
        j = c.execute("insert into authority (oname,uid,password,email,mobile) values ('"+oname +
                      "','"+uid+"','"+password+"','"+email+"','"+mobile+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def owner_reg(cname,city,landmarks,remarks,mobile,image,uid):
    try:
        c, conn = db_connect()
        print(cname,city,landmarks,remarks,mobile,image)
        id="0"
        status = "pending"
        j = c.execute("insert into aupload (cname,city,landmarks,remarks,mobile,image,uid) values ('"+cname +
                      "','"+city+"','"+landmarks+"','"+remarks+"','"+mobile+"','"+image+"','"+uid+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def owner_reg1(cname,city,landmarks,remarks,mobile,image,uid):
    try:
        c, conn = db_connect()
        print(cname,city,landmarks,remarks,mobile,image)
        id="0"
        status = "pending"
        j = c.execute("insert into message (cname,city,landmarks,remarks,mobile,image,uid) values ('"+cname +
                      "','"+city+"','"+landmarks+"','"+remarks+"','"+mobile+"','"+image+"','"+uid+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


# def vp():
#     c, conn = db_connect()
#     c.execute("select * from owner ")
#     result = c.fetchall()
#     conn.close()
#     print("result")
#     return result

def ins_loginact(uid, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from authority where uid='" +
                      uid+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        print(".....")
        print(c)
        return j
    except Exception as e:
        return(str(e))

