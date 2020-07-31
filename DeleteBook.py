# -*- coding: utf-8 -*-
"""
J.A.R.V.I.S Says Hello

@author: Ashlesh
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="rcpl_db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table


def deleteBook():
    
    bid = en1.get()
    
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
    except:
        messagebox.showinfo("Check Credentials","Please check Book ID")
    
    print(bid)

    en1.delete(0, END)

    
