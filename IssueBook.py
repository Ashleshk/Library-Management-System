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
issueTable = "issuedetail" #Issue Table
bookTable = "books" #Book Table
stuTable = "studetail" #Student Table
empTable = "empdetail" #Employee Table
    
allRoll = [] #List To store all Roll Numbers
allEmpId = [] #List To store all Employee IDs
allBid = [] #List To store all Book IDs

def issue():
    
    global issueBtn,labelFrame,lb1,en1,en2,en3,quitBtn,root,Canvas1,status
    
    bid = en1.get()
    issueto = en2.get()
    issueby = en3.get()
    
    issueBtn.destroy()
    quitBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    en1.destroy()
    en2.destroy()
    en3.destroy()
    
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    extractRollno = "select rollno from "+stuTable
    try:
        cur.execute(extractRollno)
        con.commit()
        for i in cur:
            allRoll.append(i[0])
        
        if issueto in allRoll:
            pass
        else:
            messagebox.showinfo("Error","Roll No not present")
    except:
        messagebox.showinfo("Error","Can't fetch Roll No")
        
    extractEmpID = "select empid from "+empTable
    try:
        cur.execute(extractEmpID)
        con.commit()
        for i in cur:
            allEmpId.append(i[0])
        
        if issueby in allEmpId:
            pass
        else:
            messagebox.showinfo("Error","Emp ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Emp IDs")
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.25
    
    Label(labelFrame, text="%-20s%-30s%-30s"%('BID','Issued To','Issued By'),bg='black',fg='white').place(relx=0.27,rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------",bg='black',fg='white').place(relx=0.2,rely=0.2)
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"','"+issueby+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allBid and issueto in allRoll and issueby in allEmpId and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
        else:
            allBid.clear()
            allEmpId.clear()
            allRoll.clear()
            return
        con.commit()
        cur.execute(show)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-30s"%(i[0],i[1],i[2]),bg='black',fg='white').place(relx=0.27,rely=y)
            y += 0.1
            print(i)
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    print(issueby)
    
    allBid.clear()
    allEmpId.clear()
    allRoll.clear()
    
    backBtn = Button(root,text="< Back",bg='#455A64', fg='white', command=issueBook)
    backBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    
