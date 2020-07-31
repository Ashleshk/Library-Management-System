import pymysql

con = pymysql.connect('localhost', 'root', 
    'root', 'rcpl_db')

with con:
    
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))