import sqlite3 as sdb
import warnings


def creatdb_sqlite():

    # SET UP THE CONNECTION
    try:
        con = sdb.connect('testdb.db')
        print ("Creat database testdb")
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print ("SQLite version: %s" % data)
        return con

    except:
        print("Error")