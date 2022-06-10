from cProfile import label
from cgitb import text
import csv
from enum import auto

from itertools import count
from pydoc import describe
import shutil
from sqlite3 import Cursor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from turtle import clear, color, width
from unittest.util import _count_diff_all_purpose
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser

from setuptools import Command
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date,datetime, timedelta
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
from tkPDFViewer import tkPDFViewer as pdf# For pdf view

#saiju
import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel
from matplotlib.widgets import Cursor
from dateutil.relativedelta import relativedelta
import pendulum

from pathlib import Path
import pandas as pd
from tkinter import messagebox
from tkinter import *
from docx import Document
from fpdf import FPDF
import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import pdfkit
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email import encoders

import win32api
import win32print
from tkinter import filedialog
from pyautogui import alert
import os
import tempfile
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image




# ##########################################################################################################
# fbilldb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
# )
# fbcursor = fbilldb.cursor()
##########################################################################################################
def reset():
  global root
  root.destroy()

root=Tk()
root.geometry("1360x730")

root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
customermain=Frame(tab7, relief=GROOVE, bg="#f8f8f2")
customermain.pack(side="top", fill=BOTH)

CusmidFrame=Frame(customermain, bg="#f5f3f2", height=60)
CusmidFrame.pack(side="top", fill=X)

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=(5, 2))
cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=(0, 5))

ad_usr = PIL.Image.open("images/user_add.png")
cus_addcustomerIcon=ImageTk.PhotoImage(ad_usr)

cus_addcustomerLabel = Button(CusmidFrame,compound="top", text="Add new\nCustomer",relief=RAISED,  command="add_customer",          image=cus_addcustomerIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
cus_addcustomerLabel.pack(side="left", pady=3, ipadx=4)

usr_edit = PIL.Image.open("images/user_edit.png")
cus_editcustomerIcon=ImageTk.PhotoImage(usr_edit)
cus_editcustomerLabel = Button(CusmidFrame,compound="top", text="Edit/View\nCustomer",relief=RAISED,command="edit_customer", image=cus_editcustomerIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_editcustomerLabel.pack(side="left")

usr_del = PIL.Image.open("images/user_delete.png")
cus_deletecustomerIcon=ImageTk.PhotoImage(usr_del)
cus_deletecustomerLabel = Button(CusmidFrame,compound="top", text="Delete\nSelected",relief=RAISED, command="delete_customer",image=cus_deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_deletecustomerLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_pre = PIL.Image.open("images/priewok.png")
cus_previewinvoiceIcon=ImageTk.PhotoImage(usr_pre)
cus_previewinvoiceLabel = Button(CusmidFrame,compound="top",command="previewinvoice_customer", text="Preview\nInvoice List",relief=RAISED,               image=cus_previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_previewinvoiceLabel.pack(side="left")

usr_print = PIL.Image.open("images/printer.png")
cus_printinvoiceIcon=ImageTk.PhotoImage(usr_print)
cus_printinvoiceLabel = Button(CusmidFrame,compound="top", text="Print\n Invoice List",relief=RAISED,  command="printinvoice_customer", image=cus_printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_printinvoiceLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_em = PIL.Image.open("images/gmail.png")
cus_emailinviceIcon=ImageTk.PhotoImage(usr_em)
cus_emailinviceLabel = Button(CusmidFrame,compound="top",command="emailinvoice_customer", text="E-mail\nInvoice List",relief=RAISED,               image=cus_emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_emailinviceLabel.pack(side="left")

usr_sms = PIL.Image.open("images/text-message.png")
cus_smsIcon=ImageTk.PhotoImage(usr_sms)
cus_smsLabel = Button(CusmidFrame,compound="top", text="Send SMS\nNotification",command="customersms", relief=RAISED, image=cus_smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_smsLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_imp = PIL.Image.open("images/import.png")
cus_importcustomerIcon=ImageTk.PhotoImage(usr_imp)
cus_importcustomerLabel = Button(CusmidFrame,compound="top", text="Import\nCustomers",command="import_customer",relief=RAISED, image=cus_importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_importcustomerLabel.pack(side="left")

usr_exp = PIL.Image.open("images/export.png")
cus_exportcustomerIcon=ImageTk.PhotoImage(usr_exp)
cus_exportcustomerLabel = Button(CusmidFrame,compound="top", text="Export\nCustomers",command="export_customer",relief=RAISED, image=cus_exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_exportcustomerLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_srh = PIL.Image.open("images/search-icon.png")
cus_customersearchIcon=ImageTk.PhotoImage(usr_srh)
cus_customersearchLabel = Button(CusmidFrame,compound="top",command="search_customers", text="Search in\nCustomers",relief=RAISED,               image=cus_customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_customersearchLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_rfs= PIL.Image.open("images/refresh.png")
cus_refreshcustomerIcon=ImageTk.PhotoImage(usr_rfs)
cus_refreshcustomerLabel = Button(CusmidFrame,compound="top", command="refresh_customers",text="Refresh\ncustomer list",relief=RAISED,               image=cus_refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_refreshcustomerLabel.pack(side="left")

cus_invoi1label = Label(customermain, text="Customers", font=("arial", 18), bg="#f8f8f2")
cus_invoi1label.place(x=0,y=65)
cus_invoi1label = Label(customermain, text="Right click on datagrid row for more options.", font=("arial", 10), bg="#f8f8f2")
cus_invoi1label.pack(side="left", padx=(825,0))

cus_invoi1label = Label(customermain, text="Category ", font=("arial", 15), bg="#f8f8f2")
cus_invoi1label.pack(side="right", padx=(0,120))

cus_inv_s=ttk.Style()
cus_inv_s.configure('Treeview.Heading',background='white')
cus_inv_tree=ttk.Treeview(tab7,selectmode='browse')
cus_inv_tree.place(x=0,y=95,height=280)
cus_inv_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
cus_inv_vertical_bar.place(x=1083,y=95,height=280)
cus_inv_tree["columns"]=("1","2","3","4","5","6","7","8")
cus_inv_tree["show"]='headings'
cus_inv_tree.column("1",width=30,anchor='c')
cus_inv_tree.column("2",width=140,anchor='c')
cus_inv_tree.column("3",width=190,anchor='c')
cus_inv_tree.column("4",width=176,anchor='c')
cus_inv_tree.column("5",width=176,anchor='c')
cus_inv_tree.column("6",width=120,anchor='c')
cus_inv_tree.column("7",width=130,anchor='c')
cus_inv_tree.column("8",width=120,anchor='c')
cus_inv_tree.heading("1",text="")
cus_inv_tree.heading("2",text="Customer ID")
cus_inv_tree.heading("3",text="Category")
cus_inv_tree.heading("4",text="Customer Name")
cus_inv_tree.heading("5",text="Contact Persion")
cus_inv_tree.heading("6",text="Customer Tel.")
cus_inv_tree.heading("7",text="SMS Number")
cus_inv_tree.heading("8",text="Type")

# cus_s=ttk.Style()
# cus_s.configure('Treeview.Heading',background='white')
# cus_tree=ttk.Treeview(tab7,selectmode='browse')
# cus_tree.place(x=0,y=353,height=20)

# cus_tree["columns"]=("1","2","3","4","5","6","7","8")
# cus_tree["show"]='headings'
# cus_tree.column("1",width=30,anchor='c')
# cus_tree.column("2",width=140,anchor='c')
# cus_tree.column("3",width=190,anchor='c')
# cus_tree.column("4",width=176,anchor='c')
# cus_tree.column("5",width=176,anchor='c')
# cus_tree.column("6",width=120,anchor='c')
# cus_tree.column("7",width=130,anchor='c')
# cus_tree.column("8",width=120,anchor='c')
# cus_tree.heading("1",text="")
# cus_tree.heading("2",text="Customer(S)")
# cus_tree.heading("3",text="")
# cus_tree.heading("4",text="")
# cus_tree.heading("5",text="")
# cus_tree.heading("6",text="")
# cus_tree.heading("7",text="")
# cus_tree.heading("8",text="")

#----------------------------------------------------------------------------Button bottam table-----
cus_btn=Button(tab7, text="Invoices", width=15)
cus_btn.place(x=7, y=390)
cus_btn=Button(tab7, text="Orders", width=15)
cus_btn.place(x=125, y=390)
cus_btn=Button(tab7, text="Estimates", width=15)
cus_btn.place(x=243, y=390)
cus_btn=Button(tab7, text="Statement", width=15)
cus_btn.place(x=361, y=390)
cus_btn=Button(tab7, text="Payments", width=15)
cus_btn.place(x=479,y=390)
cus_btn=Button(tab7, text="Purchase O.", width=15)
cus_btn.place(x=597, y=390)

#-------------------------------------------------------------------------Bottom Table one-------------
cus_s=ttk.Style()
cus_s.configure('Treeview.Heading',background='white')
cus_tree=ttk.Treeview(tab7,selectmode='browse')
cus_tree.place(x=0,y=415,height=280)
cus_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
cus_vertical_bar.place(x=1083,y=415,height=280)
cus_tree["columns"]=("1","2","3","4","5","6","7","8","9")
cus_tree["show"]='headings'


cus_tree.column("1",width=20,anchor='c')
cus_tree.column("2",width=140,anchor='c')
cus_tree.column("3",width=110,anchor='c')
cus_tree.column("4",width=110,anchor='c')
cus_tree.column("5",width=120,anchor='c')
cus_tree.column("6",width=120,anchor='c')
cus_tree.column("7",width=160,anchor='c')
cus_tree.column("8",width=160,anchor='c')
cus_tree.column("9",width=140,anchor='c')
cus_tree.heading("1",text="")
cus_tree.heading("2",text="#ID")
cus_tree.heading("3",text="Issue Date")
cus_tree.heading("4",text="Due Date")
cus_tree.heading("5",text="Recurring")
cus_tree.heading("6",text="Status")
cus_tree.heading("7",text="Invoice Total")
cus_tree.heading("8",text="Total Paid")
cus_tree.heading("9",text="Balance")

#-----------------------------------------------------------Bottom 
# cus_s=ttk.Style()
# cus_s.configure('Treeview.Heading',background='white')
# cus_tree=ttk.Treeview(tab7,selectmode='browse')
# cus_tree.place(x=0,y=670,height=20)
# cus_tree["columns"]=("1","2","3","4","5","6","7","8","9")
# cus_tree["show"]='headings'


# cus_tree.column("1",width=20,anchor='c')
# cus_tree.column("2",width=140,anchor='c')
# cus_tree.column("3",width=110,anchor='c')
# cus_tree.column("4",width=110,anchor='c')
# cus_tree.column("5",width=120,anchor='c')
# cus_tree.column("6",width=120,anchor='c')
# cus_tree.column("7",width=160,anchor='c')
# cus_tree.column("8",width=160,anchor='c')
# cus_tree.column("9",width=140,anchor='c')
# cus_tree.heading("1",text="")
# cus_tree.heading("2",text="Invoice(s)")
# cus_tree.heading("3",text="")
# cus_tree.heading("4",text="")
# cus_tree.heading("5",text="")
# cus_tree.heading("6",text="")
# cus_tree.heading("7",text="")
# cus_tree.heading("8",text="")
# cus_tree.heading("9",text="")


#------------------------------------------------------------Right side table list box in main----------------
cus_tree1=ttk.Treeview(tab7,selectmode='browse')
cus_tree1.place(height=600,width=254,
                      x=1099,y=95
                      )
cus_tree1["columns"]=("1")
cus_tree1["show"]='headings'
cus_tree1.column("1",width=254,anchor='c')
cus_tree1.heading("1",text="View filter by category")
cus_listbox = Listbox(tab7,height =8,  
                      width = 29,  
                      bg = "white",
                      activestyle = 'dotbox',  
                      fg = "black",
                      highlightbackground="white")  
cus_listbox.insert(0, "  View all records")
cus_listbox.insert(1, "  View only Client/Vendor Type")
cus_listbox.insert(2, "  View only Client Type")
cus_listbox.insert(3, "  View only Vendor Type")

cus_listbox.place(x=1099,y=120,height=545,width=254)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



root.mainloop()