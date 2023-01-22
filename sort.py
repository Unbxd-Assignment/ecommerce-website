#for applying sort by price - ascending and descending, sort by relevancy

import mysql 

def sortbyprice_asc():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * products ORDER BY price ASC")
    products = cur.fetchall()
    cur.close()

def sortbyprice_desc():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * products ORDER BY price DESC")
    products = cur.fetchall()
    cur.close()

#def sortby_relevancy():
