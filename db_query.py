import db_config
import sqlite3 as sdb
import warnings
import urllib
from urllib import request

temp = []

# def getLiveCount():
#     url = "'"+ temp.row[1] +"'"
#     file = urllib. request. urlopen(url)
#     for line in file:
#         decoded_line = line.decode("utf-8")
#         print(decoded_line)


# CREATE A NEW TABLE

def createTable_sqlite(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Counter")
        cur.execute("CREATE TABLE Counter(Id INTEGER PRIMARY KEY AUTOINCREMENT, Link VARCHAR(255),Count VARCHAR(25));")
        print ('Counter Table created')

# # INSERT VALUES


def insertTable_sqlite(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS Counter(Id INTEGER PRIMARY KEY AUTOINCREMENT, Link VARCHAR(255),Count VARCHAR(25));")
                warnings.filterwarnings('ignore', 'unknown table')

            Link = input("Enter the Link ")
            Count = input("Enter Your College Name")
            cur.execute("INSERT INTO Counter(Link, Count) VALUES (?, ?)",
                        (Link, Count))
            print ("Record Inserted")
        except Exception as e:
            print (e)


# RETRIEVE TABLE ROWS
def retrieveTable_sqlite(con):
    with con:

        cur = con.cursor()
        con.row_factory = sdb.Row
        cur.execute("SELECT * FROM Counter")

        rows = cur.fetchall()
        for row in rows:
            if row == None:
                print ('Please Insert Record')
                break
            else:
                # print('ID: {0} Link: {1} Count: {2}'.format(row[0], row[1], row[2]))
                url = row[1]
                file = urllib. request. urlopen(url)
                for line in file:
                    decoded_line = line.decode("utf-8")
                    temp.append(decoded_line)
                    for item in (temp):
                        count = item([x[9:-1] for x in temp])
                        # stringcount = str(count)
                        print(item(url + " : " + str(count) + "\n"))

# # UPDATE ROW
def updateRow_sqlite(con):
    with con:

        try:
            cur = con.cursor()
            con.row_factory = sdb.Row
            cur.execute("SELECT * FROM Counter")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Link: {1} Count: {2}'.format(
                    row[0], row[1], row[2]))

            id = input("Enter ID for Update Record")
            link = input("Enter Name for Update Record")
            count = input("Enter College Name for Update Record")
            cur.execute("UPDATE Counter SET Link = ?, Count = ? WHERE Id = ?",
                        (link, count, id))
            print ("Number of rows updated:",  cur.rowcount)
            if cur.rowcount == 0:
                print ('Record Not Updated')
        except TypeError as e:
            print ('ID Not Exist ')

#  DELETE ROW


def deleteRow_sqlite(con):
    with con:

        try:
            cur = con.cursor()
            con.row_factory = sdb.Row
            cur.execute("SELECT * FROM Counter")
            rows = cur.fetchall()
            for row in rows:
                print ('Table Data:', row["Id"], row["Link"], row["Count"])

            id = input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Counter WHERE Id =  ?", (id,))
            print ("Number of rows deleted:", cur.rowcount)

        except TypeError as e:
            print ('ID Not Exist ')