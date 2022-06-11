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

selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")
color = PhotoImage(file="images/font_color.png")

photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")
photo11 = PhotoImage(file = "images/export excel.png")


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

cus_addcustomerLabel = Button(CusmidFrame,compound="top", text="Add new\nCustomer",relief=RAISED,  command=lambda:cus_add_customer(),          image=cus_addcustomerIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
cus_addcustomerLabel.pack(side="left", pady=3, ipadx=4)

usr_edit = PIL.Image.open("images/user_edit.png")
cus_editcustomerIcon=ImageTk.PhotoImage(usr_edit)
cus_editcustomerLabel = Button(CusmidFrame,compound="top", text="Edit/View\nCustomer",relief=RAISED,command=lambda:cus_edit_customer(), image=cus_editcustomerIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_editcustomerLabel.pack(side="left")

usr_del = PIL.Image.open("images/user_delete.png")
cus_deletecustomerIcon=ImageTk.PhotoImage(usr_del)
cus_deletecustomerLabel = Button(CusmidFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=lambda:cus_delete_customer(),image=cus_deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_deletecustomerLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_pre = PIL.Image.open("images/priewok.png")
cus_previewinvoiceIcon=ImageTk.PhotoImage(usr_pre)
cus_previewinvoiceLabel = Button(CusmidFrame,compound="top",command=lambda:cus_previewinvoice_customer(), text="Preview\nInvoice List",relief=RAISED,               image=cus_previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_previewinvoiceLabel.pack(side="left")

usr_print = PIL.Image.open("images/printer.png")
cus_printinvoiceIcon=ImageTk.PhotoImage(usr_print)
cus_printinvoiceLabel = Button(CusmidFrame,compound="top", text="Print\n Invoice List",relief=RAISED,  command=lambda:cus_printinvoice_customer(), image=cus_printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_printinvoiceLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_em = PIL.Image.open("images/gmail.png")
cus_emailinviceIcon=ImageTk.PhotoImage(usr_em)
cus_emailinviceLabel = Button(CusmidFrame,compound="top",command=lambda:cus_addemail_order(), text="E-mail\nInvoice List",relief=RAISED,               image=cus_emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_emailinviceLabel.pack(side="left")

usr_sms = PIL.Image.open("images/text-message.png")
cus_smsIcon=ImageTk.PhotoImage(usr_sms)
cus_smsLabel = Button(CusmidFrame,compound="top", text="Send SMS\nNotification",command=lambda:cus_customersms(), relief=RAISED, image=cus_smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_smsLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_imp = PIL.Image.open("images/import.png")
cus_importcustomerIcon=ImageTk.PhotoImage(usr_imp)
cus_importcustomerLabel = Button(CusmidFrame,compound="top", text="Import\nCustomers",command=lambda:cus_import_customer(),relief=RAISED, image=cus_importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_importcustomerLabel.pack(side="left")

usr_exp = PIL.Image.open("images/export.png")
cus_exportcustomerIcon=ImageTk.PhotoImage(usr_exp)
cus_exportcustomerLabel = Button(CusmidFrame,compound="top", text="Export\nCustomers",command=lambda:cus_export_customer(),relief=RAISED, image=cus_exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_exportcustomerLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_srh = PIL.Image.open("images/search-icon.png")
cus_customersearchIcon=ImageTk.PhotoImage(usr_srh)
cus_customersearchLabel = Button(CusmidFrame,compound="top",command=lambda:cus_search_customers(), text="Search in\nCustomers",relief=RAISED,               image=cus_customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_customersearchLabel.pack(side="left")

cus_pn = Canvas(CusmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
cus_pn.pack(side="left", padx=5)

usr_rfs= PIL.Image.open("images/refresh.png")
cus_refreshcustomerIcon=ImageTk.PhotoImage(usr_rfs)
cus_refreshcustomerLabel = Button(CusmidFrame,compound="top", command=lambda:cus_refresh_customers(self),text="Refresh\ncustomer list",relief=RAISED,               image=cus_refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
cus_refreshcustomerLabel.pack(side="left")

cus_invoi1label = Label(customermain, text="Customers", font=("arial", 18), bg="#f8f8f2")
cus_invoi1label.place(x=0,y=65)
cus_invoi1label = Label(customermain, text="Right click on datagrid row for more options.", font=("arial", 10), bg="#f8f8f2")
cus_invoi1label.pack(side="left", padx=(825,0))

cus_invoi1label = Label(customermain, text="Category ", font=("arial", 15), bg="#f8f8f2")
cus_invoi1label.pack(side="right", padx=(0,160))

cus_fltr = StringVar()
cus_flt=ttk.Combobox(customermain, textvariable=cus_fltr)
cus_flt.place(x=1210, y=75)
cus_flt["values"]=("Default")
cus_flt.current(0)

cus_main_s=ttk.Style()
cus_main_s.configure('Treeview.Heading',background='white')
cus_main_tree=ttk.Treeview(tab7,selectmode='browse')
cus_main_tree.place(x=0,y=95,height=280)
cus_main_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
cus_main_vertical_bar.place(x=1083,y=95,height=280)
cus_main_tree["columns"]=("1","2","3","4","5","6","7","8")
cus_main_tree["show"]='headings'
cus_main_tree.column("1",width=30,anchor='c')
cus_main_tree.column("2",width=140,anchor='c')
cus_main_tree.column("3",width=190,anchor='c')
cus_main_tree.column("4",width=176,anchor='c')
cus_main_tree.column("5",width=176,anchor='c')
cus_main_tree.column("6",width=120,anchor='c')
cus_main_tree.column("7",width=130,anchor='c')
cus_main_tree.column("8",width=120,anchor='c')
cus_main_tree.heading("1",text="")
cus_main_tree.heading("2",text="Customer ID")
cus_main_tree.heading("3",text="Category")
cus_main_tree.heading("4",text="Customer Name")
cus_main_tree.heading("5",text="Contact Persion")
cus_main_tree.heading("6",text="Customer Tel.")
cus_main_tree.heading("7",text="SMS Number")
cus_main_tree.heading("8",text="Type")

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


#***************************************************************************************Functions
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$((Top Button Functions))
#---------------------------------------------------------------------------------Mail
def cus_send_mails():

      cus_sender_email = "saijuinfox@gmail.com"    
      cus_sender_password = "8848937577" 

      cus_server = smtplib.SMTP('smtp.gmail.com', 587)
    
      cus_server.starttls()

      cus_server.login(cus_sender_email, cus_sender_password)

    
      cus_carbcopy_info = cus_carcopyem_address.get()
      

    
      cus_msg = MIMEMultipart()
      cus_msg['Subject'] = cus_email_subject.get() 
    
      cus_mail_content  = cus_mframe.get('1.0','end-1c') 
      cus_msg['From'] = cus_email_from.get()
      cus_msg['To'] = cus_email_address.get()
    
        
      cus_gettingimg=cus_lstfrm.get()
      cus_lst_data = cus_gettingimg[1:-1].split(',')


      cus_msg.attach(MIMEText(cus_mail_content, 'plain'))

      for i in cus_lst_data:
          if len(i.strip()[1:-1])>1:

              with open('images/'+ i.strip()[1:-1], "rb") as attachment:
    
                  cus_part = MIMEBase("application", "octet-stream")
                  cus_part.set_payload(attachment.read())

                  encoders.encode_base64(cus_part)
                  cus_part.add_header('Content-Disposition', "attachment; filename= %s" % 'images/'+ i.strip()[1:-1]) 

      
                  cus_msg.attach(cus_part)
        

      cus_server.sendmail(cus_email_from.get(),cus_email_address.get(),cus_msg.as_string())
      cus_server.sendmail(cus_email_from.get(), cus_carbcopy_info,cus_msg.as_string()) 
def cus_empsfile_image(event):
            global cus_yawn
            for i in cus_htcodeframe.curselection():
              print("hloo",cus_htcodeframe.get(i))
              cus_yawn=cus_htcodeframe.get(i)        
              edit_window_img = Toplevel()
              edit_window_img.title("View Image")
              edit_window_img.geometry("700x500")
              image = Image.open("images/"+cus_yawn)
              resize_image = image.resize((700, 500))
              image = ImageTk.PhotoImage(resize_image)
              cus_psimage = Label(edit_window_img,image=image)
              cus_psimage.photo = image
              cus_psimage.pack()
def cus_file(event):
      win32api.ShellExecute(0,"",cus_filenamez,None,".",0)
def cus_UploadAction(event=None):
        global cus_filenamez
        cus_filenamez = askopenfilename(filetypes=(('PDF', '*.pdf',),("png file ",'.png'),("jpg file", ".jpg"),  ("All files", "*.*"),))
        shutil.copyfile(cus_filenamez, os.getcwd()+'/images/'+cus_filenamez.split('/')[-1])
        cus_htcodeframe.insert(0, cus_filenamez.split('/')[-1]) 
def cus_addemail_order():

          cus_mailDetail=Toplevel()
          cus_mailDetail.title("Send E-mail")
          cus_mailDetail.geometry("1080x550")
          cus_mailDetail.resizable(False, False)

          style = ttk.Style()
          style.theme_use('default')
          style.configure('TNotebook.Tab', background="#999999", padding=5)
          cus_email_Notebook = ttk.Notebook(cus_mailDetail)
          cus_email_Frame = Frame(cus_email_Notebook, height=500, width=1080)
          cus_account_Frame = Frame(cus_email_Notebook, height=550, width=1080)
          cus_email_Notebook.add(cus_email_Frame, text="E-mail")
          cus_email_Notebook.add(cus_account_Frame, text="Account")
          cus_email_Notebook.place(x=0, y=0)

          cus_messagelbframe=LabelFrame(cus_email_Frame,text="Message", height=500, width=730)
          cus_messagelbframe.place(x=5, y=5)
          global cus_email_address, cus_email_subject, cus_email_from,cus_email_pswrd,cus_carcopyem_address,cus_mframe,cus_htcodeframe,cus_lstfrm,cus_langs
          cus_email_address = StringVar() 
          cus_email_subject = StringVar()

          cus_email_from = StringVar()
          cus_email_pswrd = StringVar()
          cus_carcopyem_address = StringVar()

          cus_lbl_emailtoaddr=Label(cus_messagelbframe, text="Email to address").place(x=5, y=5)
          cus_emailtoent=Entry(cus_messagelbframe, width=50,textvariable=cus_email_address)
          cus_emailtoent.place(x=120, y=5)
        
          cus_sendemail_btn=Button(cus_messagelbframe, text="Send Email", width=10, height=1, command=cus_send_mails).place(x=600, y=10)

          cus_lbl_carcopyto=Label(cus_messagelbframe, text="Carbon copy to").place(x=5, y=32)
          cus_carcopyent=Entry(cus_messagelbframe, width=50,textvariable=cus_carcopyem_address)
          cus_carcopyent.place(x=120, y=32)

          cus_lbl_subject=Label(cus_messagelbframe, text="Subject").place(x=5, y=59)
          cus_subent=Entry(cus_messagelbframe, width=50, textvariable=cus_email_subject)
          cus_subent.place(x=120, y=59)
          cus_subjectinsrt='ORD_'+str("")
          cus_subent.delete(0,'end')
          cus_subent.insert(0, cus_subjectinsrt)

          
          style = ttk.Style()
          style.theme_use('default')
          style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
          cus_mess_Notebook = ttk.Notebook(cus_messagelbframe)
          cus_emailmessage_Frame =Frame(cus_mess_Notebook, height=350, width=710)
          cus_htmlsourse_Frame = Frame(cus_mess_Notebook, height=350, width=710)
          cus_mess_Notebook.add(cus_emailmessage_Frame, text="E-mail message")

          cus_mess_Notebook.add(cus_htmlsourse_Frame, )
          cus_mess_Notebook.place(x=5, y=90)
          

          

          from tkinter import font,colorchooser
          fontSize=16
          fontStyle='Arial'
          
          def cus_font_style(event):
              global fontStyle
              fontStyle=font_family_variable.get()
              cus_mframe.config(font=(fontStyle,fontSize))

          def cus_font_size(event):
              global fontSize
              
              fontSize=size_variable.get()
              
              
              cus_mframe.config(font=(fontStyle,fontSize))

          def cus_bold_text():
              bold_font = font.Font(cus_mframe, cus_mframe.cget("font"))
              bold_font.configure(weight="bold")

              cus_mframe.tag_configure("bold", font=bold_font)

              current_tags = cus_mframe.tag_names("sel.first")

              if "bold" in current_tags:
                cus_mframe.tag_remove("bold", "sel.first", "sel.last")
              else:
                cus_mframe.tag_add("bold", "sel.first", "sel.last")    
          
          def cus_italic_text():
              italic_font = font.Font(cus_mframe, cus_mframe.cget("font"))
              italic_font.configure(slant="italic")

              cus_mframe.tag_configure("italic", font=italic_font)

              current_tags = cus_mframe.tag_names("sel.first")

              if "italic" in current_tags:
                cus_mframe.tag_remove("italic", "sel.first", "sel.last")
              else:
                cus_mframe.tag_add("italic", "sel.first", "sel.last")

          def cus_underline_text():
            try:
                if cus_mframe.tag_nextrange('underline_selection', 'sel.first', 'sel.last') != ():
                    cus_mframe.tag_remove('underline_selection', 'sel.first', 'sel.last')
                else:
                    cus_mframe.tag_add('underline_selection', 'sel.first', 'sel.last')
                    cus_mframe.tag_configure('underline_selection', underline=True)
            except TclError:
                pass

          def cus_color_select():
              color=colorchooser.askcolor()[1]
              if color:
            # if color:

                color_font = font.Font(cus_mframe, cus_mframe.cget("font"))

                cus_mframe.tag_configure("colored", font=color_font, foreground=color)

                current_tags = cus_mframe.tag_names("sel.first")

              if "colored" in current_tags:
                cus_mframe.tag_remove("colored", "sel.first", "sel.last")
              else:
                cus_mframe.tag_add("colored", "sel.first", "sel.last")

          def cus_align_right():
              data=cus_mframe.get(0.0,END)
              cus_mframe.tag_config('right',justify=RIGHT)
              cus_mframe.delete(0.0,END)
              cus_mframe.insert(INSERT,data,'right')

          def cus_align_left():
              data=cus_mframe.get(0.0,END)
              cus_mframe.tag_config('left',justify=LEFT)
              cus_mframe.delete(0.0,END)
              cus_mframe.insert(INSERT,data,'left')

          def cus_align_center():
              data=cus_mframe.get(0.0,END)
              cus_mframe.tag_config('center',justify=CENTER)
              cus_mframe.delete(0.0,END)
              cus_mframe.insert(INSERT,data,'center')

          def add_link():
              # from tkHyperLinkManager import HyperlinkManager
              # import webbrowser
              # from functools import partial
              
              hghf=cus_mframe.selection_get()
              content=hghf
              
              
            #   content.configure(foreground="red")
              cus_mframe.insert(END, " "+content)
              
              # cus_mframe.delete(1.0,END)
              
              
              
          def callback(url):
              webbrowser.open_new_tab_url(url)

          def addlinkbox():
              global top
              top = Toplevel()
              top.title('Hyperlink')
              top.geometry("400x100")
              hyp_lbl = LabelFrame(top,text="Hyperlink Information", height=80, width=300)
              hyp_lbl.place(x=10, y=5)

              hyp_lbl1 = Label(top,text="Type:")
              hyp_lbl1.place(x=18, y=24)
              
              def comb_select(event):
                  hyper = cb_comb.get()
                  if hyper == "(other)":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "(other)")
                  elif hyper == "file://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "file://")
                  elif hyper == "ftp://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "ftp://") 
                  elif hyper == "http://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "http://") 
                  elif hyper == "https://":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "https://") 
                  elif hyper == "mailto:":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "mailto:") 
                  elif hyper == "telnet:":
                      hyp= Entry(top,width=35)
                      hyp.place(x=90,y=55)
                      hyp.insert(END,  "telnet:")


              cb_comb = StringVar()
              cb1=ttk.Combobox(top,textvariable=cb_comb,width=15)
              cb1.grid(row=1,column=1,padx=90,pady=30)
              cb1['values']=('(other)','file://','ftp://','http://','https://','mailto:','news:','telnet:')
              cb1.current(0)
              cb1.bind('<<ComboboxSelected>>',comb_select)


              hyp_lbl2 = Label(top,text="URL:")
              hyp_lbl2.place(x=18, y=55)
              global cus_hyper
              cus_hyper = StringVar()
              
              hyp= Entry(top,textvariable=cus_hyper,width=35)
              hyp.place(x=90,y=55)

              

              hypbtn1 = Button(top,text="OK",width=10, command=add_link)
              hypbtn1.place(x=315,y=8)

              hypbtn2 = Button(top,text="Cancel",width=10)
              hypbtn2.place(x=315,y=35)

         

          cus_mframe=Text(cus_emailmessage_Frame,undo=True,width=84, bg="white", height=20)
          cus_mframe.pack(padx=0,pady=28,expand=False)


          cus_scrollbar1 = Scrollbar(cus_emailmessage_Frame,orient=VERTICAL,command=cus_mframe.yview)
          cus_scrollbar3= Scrollbar(cus_emailmessage_Frame,orient=HORIZONTAL,command=cus_mframe.xview, width=0)
          cus_scrollbar3.place(x=0, y=340, height=20,width=690)
          cus_scrollbar2= Scrollbar(cus_mframe,orient=HORIZONTAL,command=cus_mframe.xview, width=0)
          cus_scrollbar2.pack(fill=X,expand=True,side=BOTTOM,padx=310,pady=155)
        #   cus_scrollbar2.place(x=0, y=310, height=20,width=670)
          cus_mframe.config(xscrollcommand=cus_scrollbar2.set)
          cus_mframe.config(yscrollcommand=cus_scrollbar1.set)
          cus_scrollbar1.config(command=cus_mframe.yview)
          cus_scrollbar1.place(x =690, y=0, height=360)
          cus_scrollbar2.config(command=cus_mframe.xview)


          cus_btn1=Button(cus_emailmessage_Frame,width=20,height=20,compound = LEFT,image=selectall,command=lambda :cus_mframe.event_generate('<Control a>'))
          cus_btn1.place(x=0, y=1)

                  
          cus_btn2=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut,command=lambda :cus_mframe.event_generate('<Control x>'))
          cus_btn2.place(x=36, y=1)

          cus_btn3=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy,command=lambda :cus_mframe.event_generate('<Control c>'))
          cus_btn3.place(x=73, y=1)

          cus_btn4=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste,command=lambda :cus_mframe.event_generate('<Control v>'))
          cus_btn4.place(x=105, y=1)
          cus_btn5=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo, command=lambda:cus_mframe.event_generate("<<Undo>>")).place(x=140, y=1)

          cus_btn6=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo, command=lambda:cus_mframe.event_generate("<<Redo>>")).place(x=175, y=1)

          cus_btn7=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold,command=cus_bold_text)
          cus_btn7.place(x=210, y=1)

          cus_btn8=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics,command=cus_italic_text)
          cus_btn8.place(x=245, y=1)

          cus_btn9=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline,command=cus_underline_text)
          cus_btn9.place(x=280, y=1)

          cus_btn10=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=left,command=cus_align_left)
          cus_btn10.place(x=315, y=1)

          cus_btn11=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=right,command=cus_align_right)
          cus_btn11.place(x=350, y=1)

          cus_btn12=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=center,command=cus_align_center)
          cus_btn12.place(x=385, y=1)

          cus_btn14=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove,command=lambda :cus_mframe.delete(0.0,END))
          cus_btn14.place(x=455, y=1)
          
          cus_btn15=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=color,command=cus_color_select)
          cus_btn15.place(x=420, y=1)
          cus_btn16=Button(cus_emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink, command="addlinkbox")
          cus_btn16.place(x=491, y=1)
          global size_variable
          size_variable=IntVar()

          cus_dropcomp11 = ttk.Combobox(cus_emailmessage_Frame, width=6, textvariable=size_variable, values=tuple(range(8,17)))
          
          cus_dropcomp11.place(x=530, y=5)
        #   cus_dropcomp11.bind('<<ComboboxSelected>>',frmar)
          
          font_family_variable=StringVar()
          font_familyes=font.families()
          # dropcompo147 = ttk.Combobox(cus_emailmessage_Frame, width=10, textvariable=font_family_variable, values=font_familyes)
          # dropcompo147.place(x=600, y=5)
          # dropcompo147.current(font_familyes.index('Arial'))
          # dropcompo147.bind('<<ComboboxSelected>>', cus_font_style)
          cus_dropcomp11.bind('<<ComboboxSelected>>', cus_font_size)
          
          cus_attachlbframe=LabelFrame(cus_email_Frame,text="Attachment(s)", height=350, width=280)
          cus_attachlbframe.place(x=740, y=5)

          cus_lstfrm=StringVar()  
          cus_htcodeframe=Listbox(cus_attachlbframe, height=13, width=43,listvariable=cus_lstfrm, bg="white")
          cus_htcodeframe.place(x=5, y=5)
          cus_htcodeframe.bind('<Double-Button-1>' , cus_file)

          def cus_deslist():
              cus_laa=cus_htcodeframe.curselection()
              print("hloo",cus_htcodeframe.get(cus_laa))
              cus_yawn=cus_htcodeframe.get(cus_laa)        
              cus_htcodeframe.delete(ACTIVE)

          cus_lbl_btn_info=Label(cus_attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
          cus_btn17=Button(cus_attachlbframe, width=20, text="Add attachment file...", command=cus_UploadAction).place(x=60, y=260)
          cus_btn18=Button(cus_attachlbframe, width=20, text="Remove attachment",command=cus_deslist).place(x=60, y=295)
          cus_lbl_tt_info=Label(cus_email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
          cus_lbl_tt_info.place(x=740, y=370)

          cus_ready_frame=Frame(cus_mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
          
          cus_sendatalbframe=LabelFrame(cus_account_Frame,text="E-Mail(Sender data)",height=140, width=600)
          cus_sendatalbframe.place(x=240, y=165 )
          cus_lbl_sendermail=Label(cus_sendatalbframe, text="Company email address").place(x=5, y=10)
          cus_sentent=Entry(cus_sendatalbframe, width=40, textvariable=cus_email_from)
          cus_sentent.place(x=195, y=10)

          cus_lbl_sendecusswrd=Label(cus_sendatalbframe, text="Email Password").place(x=5, y=40)
          cus_pswrdent=Entry(cus_sendatalbframe, width=40, textvariable=cus_email_pswrd,show="*")
          cus_pswrdent.place(x=195, y=40)
#------------------------------------------------------------------------------------Add Customer
def cus_add_customer():
    add_customer = Toplevel()  
    add_customer.title("Add new Customer ")
    p2 = PhotoImage(file = "images/fbicon.png")
    add_customer.iconphoto(False, p2)
    add_customer.geometry("775x580+300+100")
    Labelframe1=LabelFrame(add_customer,text="Customer")
    Labelframe1.place(x=10,y=10,width=755,height=525)
    a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
    a2=Label(Labelframe1,text="Category:")
    a3=Label(Labelframe1,text="Status :")
    a3.place(x=620,y=7)
    b1=Entry(Labelframe1)
    ca=StringVar() 
    b2=ttk.Combobox(Labelframe1,textvariable = ca )    
    b2['values'] = ('Default')  
    b2.place(x=390,y=220) 
    b2.current(0)
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)   
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 0, offvalue = 1)
    chkbtn1.place(x=670,y=6)
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
    Labelframe2.place(x=10,y=35,width=340,height=125)
    a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
    b1=Entry(Labelframe2).place(x=110,y=10,width=210)
    b2=Entry(Labelframe2).place(x=110,y=35,width=210,height=63)  
    btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=85,height=20)
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
    Labelframe3.place(x=400,y=35,width=340,height=125)
    a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
    b11=Entry(Labelframe3).place(x=110,y=10,width=210)
    b21=Entry(Labelframe3).place(x=110,y=35,width=210,height=63)
    Labelframe4=LabelFrame(Labelframe1,text="Contact")
    Labelframe4.place(x=10,y=170,width=340,height=137)
    a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
    a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
    b11=Entry(Labelframe4).place(x=110,y=10,width=210)
    b21=Entry(Labelframe4).place(x=110,y=35,width=210)
    b31=Entry(Labelframe4).place(x=110,y=60,width=90)
    b41=Entry(Labelframe4).place(x=230,y=60,width=90)
    b51=Entry(Labelframe4).place(x=215,y=85,width=105)
    btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=220,height=20)
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
    Labelframe5.place(x=400,y=170,width=340,height=108)
    a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
    b11=Entry(Labelframe5).place(x=110,y=10,width=210)
    b21=Entry(Labelframe5).place(x=110,y=35,width=210)
    b31=Entry(Labelframe5).place(x=110,y=60,width=90)
    b41=Entry(Labelframe5).place(x=230,y=60,width=90)
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
    Labelframe6.place(x=10,y=317,width=340,height=80)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)
    a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
    b11val = IntVar(Labelframe6, value='0')
    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6,textvariable=b11val).place(x=80,y=30,width=70)
    Labelframe7=LabelFrame(Labelframe1,text="Customer type")
    Labelframe7.place(x=10,y=405,width=340,height=90)
    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3).place(x=180,y=15)
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
    Labelframe8.place(x=400,y=288,width=340,height=80)
    a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
    a12=Label(Labelframe8,text="City:").place(x=10,y=30)
    c=StringVar() 
    b11=ttk.Combobox(Labelframe8,textvariable=c)
    b11.place(x=110,y=5,width=210)
    b11['values'] = ('India','America')    
    b11.place(x=110,y=5) 
    b12=Entry(Labelframe8).place(x=110,y=30,width=210)
    Labelframe9=LabelFrame(Labelframe1,text="Notes")
    Labelframe9.place(x=400,y=380,width=340,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=20,y=10,width=295,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)
    btn1=Button(add_customer,width=50,compound = LEFT,image=tick ,text="  OK").place(x=20, y=545)
    btn2=Button(add_customer,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=665, y=545)
    add_customer.mainloop()
#-----------------------------------------------------------------------------------Edit Customer
def cus_edit_customer():
    edit_customer = Toplevel()  
    edit_customer.title("Edit Customer Details ")
    p2 = PhotoImage(file = "images/fbicon.png")
    edit_customer.iconphoto(False, p2)
    edit_customer.geometry("775x580+300+100")
    Labelframe1=LabelFrame(edit_customer,text="Customer")
    Labelframe1.place(x=10,y=10,width=755,height=525)
    a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
    a2=Label(Labelframe1,text="Category:")
    a3=Label(Labelframe1,text="Status :")
    a3.place(x=620,y=7)
    b1=Entry(Labelframe1)
    ca=StringVar() 
    b2=ttk.Combobox(Labelframe1,textvariable = ca )    
    b2['values'] = ('Default')  
    b2.place(x=390,y=220) 
    b2.current(0)
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)   
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 0, offvalue = 1)
    chkbtn1.place(x=670,y=6)
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
    Labelframe2.place(x=10,y=35,width=340,height=125)
    a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
    b1=Entry(Labelframe2).place(x=110,y=10,width=210)
    b2=Entry(Labelframe2).place(x=110,y=35,width=210,height=63)  
    btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=85,height=20)
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
    Labelframe3.place(x=400,y=35,width=340,height=125)
    a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
    b11=Entry(Labelframe3).place(x=110,y=10,width=210)
    b21=Entry(Labelframe3).place(x=110,y=35,width=210,height=63)
    Labelframe4=LabelFrame(Labelframe1,text="Contact")
    Labelframe4.place(x=10,y=170,width=340,height=137)
    a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
    a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
    b11=Entry(Labelframe4).place(x=110,y=10,width=210)
    b21=Entry(Labelframe4).place(x=110,y=35,width=210)
    b31=Entry(Labelframe4).place(x=110,y=60,width=90)
    b41=Entry(Labelframe4).place(x=230,y=60,width=90)
    b51=Entry(Labelframe4).place(x=215,y=85,width=105)
    btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=220,height=20)
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
    Labelframe5.place(x=400,y=170,width=340,height=108)
    a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
    b11=Entry(Labelframe5).place(x=110,y=10,width=210)
    b21=Entry(Labelframe5).place(x=110,y=35,width=210)
    b31=Entry(Labelframe5).place(x=110,y=60,width=90)
    b41=Entry(Labelframe5).place(x=230,y=60,width=90)
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
    Labelframe6.place(x=10,y=317,width=340,height=80)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)
    a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
    b11val = IntVar(Labelframe6, value='0')
    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6,textvariable=b11val).place(x=80,y=30,width=70)
    Labelframe7=LabelFrame(Labelframe1,text="Customer type")
    Labelframe7.place(x=10,y=405,width=340,height=90)
    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3).place(x=180,y=15)
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
    Labelframe8.place(x=400,y=288,width=340,height=80)
    a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
    a12=Label(Labelframe8,text="City:").place(x=10,y=30)
    c=StringVar() 
    b11=ttk.Combobox(Labelframe8,textvariable=c)
    b11.place(x=110,y=5,width=210)
    b11['values'] = ('India','America')    
    b11.place(x=110,y=5) 
    b12=Entry(Labelframe8).place(x=110,y=30,width=210)
    Labelframe9=LabelFrame(Labelframe1,text="Notes")
    Labelframe9.place(x=400,y=380,width=340,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=20,y=10,width=295,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)
    btn1=Button(edit_customer,width=50,compound = LEFT,image=tick ,text="  OK").place(x=20, y=545)
    btn2=Button(edit_customer,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=665, y=545)
    edit_customer.mainloop()
#-----------------------------------------------------------------------------------Delete Customer
def cus_delete_customer():
   
    messagebox.askyesno("Delete Customers", "Are you sure want to delete 1 Customer(s) ?")
#-----------------------------------------------------------------------------------Preview Invoice Customer
def cus_previewinvoice_customer():
  cus_in_preview = Toplevel()
  cus_in_preview.title("F-Billing Revolution Invoice Report ")
  cus_in_p2= PhotoImage(file = "images/fbicon.png")
  cus_in_preview.iconphoto(False, cus_in_p2)
  cus_in_preview.geometry("1800x1800+0+0")
  cus_in_frame = Frame(cus_in_preview,width=1500,height=1800,bg="red")
  cus_in_frame.pack(expand=True, fill=BOTH,  padx=10, pady=20)
  cus_in_frame.place(x=0,y=30)
  cus_in_canvas=Canvas(cus_in_frame,bg='grey',width=1400,height=1200,scrollregion=(0,0,1500, 1200))


  cus_in_vertibar=Scrollbar(cus_in_frame,orient=VERTICAL)
  cus_in_vertibar.pack(side=RIGHT,fill=Y)
  cus_in_vertibar.config(command=cus_in_canvas.yview)
  cus_in_canvas.config(width=1338,height=710)

  cus_in_canvas.config(yscrollcommand=cus_in_vertibar.set)
  cus_in_canvas.pack(expand=True,side=LEFT,fill=BOTH)
  # canvas.create_rectangle(235,10,1025,1430,  outline='yellow',fill='White')
  # canvas = Canvas(preview)
  # canvas.place(relwidth=1, relheight=1,x=250,y=10) 
  cus_in_paperheigth = cus_in_preview.winfo_fpixels('1m') * 297
  cus_in_paperwidth = cus_in_preview.winfo_fpixels('1m') * 210
  cus_in_canvas.create_rectangle(265, 20, 265+cus_in_paperwidth, 20+cus_in_paperheigth, outline='orange', fill='white')
#-----------------------------------------------------------------------------------print Invoice Customer
def cus_printinvoice_customer():

  def property1():
    propert=Toplevel()
    propert.title("OneNote for Windows 10 Document Properties")
    p2 = PhotoImage(file = "images/fbicon.png")
    propert.iconphoto(False, p2)
    propert.geometry("580x470+380+210")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Options")
      p2 = PhotoImage(file = "images/fbicon.png")
      propert1.iconphoto(False, p2)
      propert1.geometry("580x470+410+220")
      property1_Frame1=LabelFrame(propert1,height=405, width=560)
      property1_Frame1.place(x=10, y=10)  
      name=Label(property1_Frame1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(property1_Frame1, text="Paper/Output").place(x=30, y=35)
      size=Label(property1_Frame1, text="Paper size:").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(property1_Frame1, width = 28, textvariable = n )
      search['values'] = ('A4','Letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(property1_Frame1, text="Copy Count:").place(x=55, y=95)
      nocopy = Spinbox(property1_Frame1,from_=0,to=100000000, width=28).place(x=150, y=95)    
      btn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      btn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425)     
      
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=450, width=581)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)
    property_Frame1=LabelFrame(property_Frame,height=380, width=560)
    property_Frame1.place(x=10, y=10)   
    name=Label(property_Frame1, text="Orientation:").place(x=10, y=15)
    n = StringVar()
    search = ttk.Combobox(property_Frame1, width = 28, textvariable = n )
    search['values'] = ('Landscape','Portrait')
    search.place(x=10,y=40)
    search.current(0)
    text=Text(property_Frame1,width=40).place(x=217, y=20,height=300)
    btn=Button(property_Frame1, text="Advanced...", width=10,command=property2).place(x=430, y=335)
    btn=Button(property_Frame,text="OK", width=10,).place(x=390, y=400)
    btn=Button(property_Frame, text="Cancel", width=10,).place(x=490, y=400)     
 
  print1=Toplevel()
  print1.title("Print")
  p2 = PhotoImage(file = "images/fbicon.png")
  print1.iconphoto(False, p2)   
  print1.geometry("580x390+350+200")
  printerframe=LabelFrame(print1, text="Printer", height=85, width=563)
  printerframe.place(x=10, y=5)   
  name=Label(printerframe, text="Name:").place(x=10, y=5)
  v=StringVar() 
  e1= ttk.Combobox(printerframe,textvariable=v)
  e1['values'] = ('OneNote for Windows10','Microsoft XPS Document Writer','Microsoft Print PDF','Fax')   
  e1.place(x=70,y=5,width=310) 
  e1.current(0)
  where=Label(printerframe, text="Where:").place(x=10, y=35)
  printocheckvar=IntVar()
  printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
  printochkbtn.place(x=390, y=35)
  btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=470, y=5)
  pageslblframe=LabelFrame(print1, text="Pages", height=140, width=277)
  pageslblframe.place(x=10, y=95)
  radvar=IntVar()
  radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
  radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
  radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
  pagecountentry = Entry(pageslblframe, width=30).place(x=80, y=47)
  pageinfolabl=Label(pageslblframe,text="Enter page numbers and/or page ranges\n      seperated by commas. For example:1,3,5-12")
  pageinfolabl.place(x=0, y=75)
  copylblframe=LabelFrame(print1, text="Copies", height=140, width=277)
  copylblframe.place(x=295, y=95)
  nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
  noentry = Spinbox(copylblframe,from_=0,to=100000000, width=18).place(x=140, y=5)      
  one=Frame(copylblframe, width=30, height=50, bg="black").place(x=20, y=40)     
  two=Frame(copylblframe, width=30, height=50, bg="grey").place(x=15, y=45)     
  three=Frame(copylblframe, width=30, height=50, bg="white").place(x=10, y=50)      
  four=Frame(copylblframe, width=30, height=50, bg="black").place(x=80, y=40)      
  fiv=Frame(copylblframe, width=30, height=50, bg="grey").place(x=75, y=45)      
  six=Frame(copylblframe, width=30, height=50, bg="white").place(x=70, y=50)      
  collatecheckvar=IntVar()
  collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
  collatechkbtn.place(x=120, y=40)
  othrlblframe=LabelFrame(print1, text="Other", height=100, width=277)
  othrlblframe.place(x=10, y=240)
  printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
  va=StringVar()  
  dropprint= ttk.Combobox(othrlblframe,textvariable=va)
  dropprint['values'] = ('AllPages','Odd Pages','Even Pages')     
  dropprint.place(x=80,y=0,width=185) 
  dropprint.current(0)
  orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
  dropord = ttk.Combobox(othrlblframe, width=28).place(x=80, y=25)
  val=StringVar() 
  dropord= ttk.Combobox(othrlblframe,textvariable=val)
  dropord['values'] = ('Direct(1-9)','Reverse(1-9)')   
  dropord.place(x=80,y=25,width=185) 
  dropord.current(0)
  duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
  val1=StringVar() 
  droplex= ttk.Combobox(othrlblframe,textvariable=val1)
  droplex['values'] = ('Default','Vertical','Horizontal','Simplex') 
  droplex.place(x=80,y=50,width=185) 
  droplex.current(0)
  prmodelblframe=LabelFrame(print1, text="Print mode",height=100, width=277)
  prmodelblframe.place(x=295, y=240)
  val11=StringVar() 
  dropscal= ttk.Combobox(prmodelblframe,textvariable=val11)
  dropscal['values'] = ('Default','Split big Pages','Join Small Pages','Scale') 
  dropscal.place(x=5,y=5,width=260,height=40) 
  dropscal.current(0)
  poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=50)
  val12=StringVar() 
  droppos= ttk.Combobox(prmodelblframe,textvariable=val12)
  droppos['values'] = ('Default')   
  droppos.place(x=136,y=50,width=129) 
  droppos.current(0)
  okbtn=Button(print1, text="Ok", width=10).place(x=390, y=350)
  canbtn=Button(print1, text="Cancel", width=10).place(x=490, y=350)
#-----------------------------------------------------------------------------------Customer Sms
def cus_customersms():
  send_SMS=Toplevel()
  send_SMS.title("Send SMS notification")
  p2 = PhotoImage(file = "images/fbicon.png")
  send_SMS.iconphoto(False, p2)
  send_SMS.geometry("580x500+380+150")
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=485, width=585)
  SMS_Service_Account = Frame(sms_Notebook, height=485, width=585)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)
  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification,width=92).place(x=10, y=35,height=25)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=65)
  stex=Entry(SMS_Notification, width=60).place(x=10, y=90,height=120)
  no=Label(SMS_Notification, text="0/160 characters")
  no.place(x=285, y=210)
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=395, y=65)
  dcl=Entry(SMS_Notification, width=27)
  dcl.place(x=395, y=90,height=200)
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=365, height=60)
  smstype.place(x=10, y=230)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=15, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=195, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=552, height=120)
  tiplbf.place(x=10, y=292)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS number with the country code. Do not use the + sign at the beginning(example\nUS number: 8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)
  btn1=Button(SMS_Notification,width=150,compound = LEFT,image=tick ,text="  Send SMS notification").place(x=10, y=425,height=31)
  btn2=Button(SMS_Notification,width=215,compound = LEFT,image=warnin,text="  Confirm SMS cost before sending").place(x=190, y=425,height=31)
  btn3=Button(SMS_Notification,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=472, y=425,height=31)
  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=555, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="EXPERTTEXTING(www.experttexting.com-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=210, y=5)
  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=555, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type,width=29).place(x=100, y=5,height=23)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=29).place(x=100, y=45,height=23)
  combo=Label(sms1type,text="Route").place(x=320, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type,textvariable = n )
  combo1['values'] = ('1-Economy (test first)','2-Standard (default)','3-Premium') 
  combo1.place(x=375,y=5,height=23,width=165)  
  combo1.current(0)
  btn1=Button(sms1type,width=110,compound = LEFT,image=saves,text="  Save settings").place(x=420, y=35,height=31)  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=555, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=2, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=2, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=2, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=2, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=130, y=200)  
#-----------------------------------------------------------------------------------Import Customer
def cus_import_customer():
    top=Toplevel()
    top.title("Import Customers list from Excel(XLS)File")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("785x540+280+100")
    importframe=Frame(top)
    importframe.place(x=0,y=0,height=700,width=785)
    impolbl=Label(importframe,text="Import source Excel(XLS) File:").place(x=10,y=10)
    impoentry=Entry(importframe,bg="white")
    impoentry.place(x=10,y=40,width=400,height=25)
    previewlbl=Label(importframe,text="Source XLS File preview").place(x=10,y=75)
    langs = ()
    langs_var = StringVar(value=langs)
    listbox = Listbox(
        importframe,
        listvariable=langs_var,
        width=71,
        height=8,
        selectmode='extended')
    listbox.place(x=10,y=102,height=390) 
    scrollbar = Scrollbar(
        importframe,
        orient='vertical',
        command=listbox.yview
    )
    
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=422,y=104,height=370)

    scrollbar = Scrollbar(
        importframe,
        orient='horizontal',
        
        command=listbox.xview
    ) 
    listbox['xscrollcommand'] = scrollbar.set
    scrollbar.place(x=12,y=474,width=427)
    lb1=Label(importframe,text="Select import source XLs file first after build column associations").place(x=10,y=500)
    
    def callback(url):
        webbrowser.open_new(url) 

    link1 = Label(importframe, text="More info", fg="blue", cursor="hand2")
    link1.place(x=360,y=500)
    link1.bind("<Button-1>", lambda e: callback("https://f-billing.com/faq.php"))
    importbutton=Button(top,command=lambda:cus_export_customer(),image=folder,compound=LEFT)
    importbutton.place(x=410,y=40,height=25,width=30)
    lb1=Label(importframe,text="     Please associate datafields with data columns").place(x=500,y=10)
    id1=Label(importframe,text="CUSTOMER ID = ",fg="blue")
    id1.place(x=460,y=40)
    no = StringVar() 
    idd = ttk.Combobox(importframe, width = 27, textvariable = no ) 
    idd['values'] = ('    -NotAssociated-')
    idd.place(x=580,y=40,height=23) 
    idd.current(0)
    name1=Label(importframe,text="CUSTOMER NAME = ",fg="blue")
    name1.place(x=460,y=65)
    namevar = StringVar() 
    name = ttk.Combobox(importframe, width = 27, textvariable = namevar ) 
    name['values'] = ('    -NotAssociated-' 
                              )  
    name.place(x=580,y=65,height=23) 
    name.current(0)
    category1=Label(importframe,text="CATEGORY = ",fg="blue")
    category1.place(x=460,y=90)
    categoryvar = StringVar() 
    category = ttk.Combobox(importframe, width = 27, textvariable = categoryvar ) 
    category['values'] = ('    -NotAssociated-' 
                              ) 
    category.place(x=580,y=90,height=23) 
    category.current(0)
    add=Label(importframe,text="ADDRESS = ",fg="blue")
    add.place(x=460,y=115)
    addvar = StringVar() 
    addc = ttk.Combobox(importframe, width = 27, textvariable = addvar ) 
    addc['values'] = ('    -NotAssociated-' 
                              )
    addc.place(x=580,y=115,height=23) 
    addc.current(0)
    tel1=Label(importframe,text="TEL.= ")
    tel1.place(x=460,y=140)
    telvar = StringVar() 
    telc = ttk.Combobox(importframe, width = 27, textvariable = telvar ) 
    telc['values'] = ('    -NotAssociated-' 
                              )  
    telc.place(x=580,y=140,height=23) 
    telc.current(0)
    fax1=Label(importframe,text="FAX = ")
    fax1.place(x=460,y=165)
    faxvar = StringVar() 
    faxc = ttk.Combobox(importframe, width = 27, textvariable = faxvar )
    faxc['values'] = ('    -NotAssociated-' 
                              )
    faxc.place(x=580,y=165,height=23) 
    faxc.current(0)
    email1=Label(importframe,text="EMAIL = ")
    email1.place(x=460,y=190)
    emailvar = StringVar() 
    emailc = ttk.Combobox(importframe, width = 27, textvariable = emailvar ) 
    emailc['values'] = ('    -NotAssociated-'
                              )    
    emailc.place(x=580,y=190,height=23) 
    emailc.current(0)
    cp1=Label(importframe,text="CONTACT PERSION = ")
    cp1.place(x=460,y=215)
    cpvar = StringVar() 
    cp = ttk.Combobox(importframe, width = 27, textvariable = cpvar )  
    cp['values'] = ('    -NotAssociated-' 
                              )     
    cp.place(x=580,y=215,height=23) 
    cp.current(0)
    sn2=Label(importframe,text="SHIP TO NAME = ")
    sn2.place(x=460,y=240)
    snvar = StringVar() 
    sn = ttk.Combobox(importframe, width = 27, textvariable = snvar )
    sn['values'] = ('    -NotAssociated-' 
                              )
    sn.place(x=580,y=240,height=23) 
    sn.current(0)
    saa2=Label(importframe,text="SHIP TO ADDESS = ")
    saa2.place(x=460,y=265)
    saa2var = StringVar() 
    saa = ttk.Combobox(importframe, width = 27, textvariable = saa2var ) 
    saa['values'] = ('    -NotAssociated-')
    saa.place(x=580,y=265,height=23) 
    saa.current(0)
    stt2=Label(importframe,text="SHIP TO TEL. = ")
    stt2.place(x=460,y=290)
    stt2var = StringVar() 
    stt = ttk.Combobox(importframe, width = 27, textvariable = stt2var )
    stt['values'] = ('    -NotAssociated-' 
                              ) 
    stt.place(x=580,y=290,height=23) 
    stt.current(0)
    stf2=Label(importframe,text="SHIP TO FAX = ")
    stf2.place(x=460,y=315)
    stf2var = StringVar() 
    stf = ttk.Combobox(importframe, width = 27, textvariable = stf2var )
    stf['values'] = ('    -NotAssociated-' 
                              )   
    stf.place(x=580,y=315,height=23) 
    stf.current(0)
    dd2=Label(importframe,text="DISCOUNT = ")
    dd2.place(x=460,y=340)
    dd2var = StringVar() 
    dd = ttk.Combobox(importframe, width = 27, textvariable = dd2var) 
    dd['values'] = ('    -NotAssociated-'
                              )
    dd.place(x=580,y=340,height=23) 
    dd.current(0)
    st112=Label(importframe,text="SPECIAL TAX 1 = ")
    st112.place(x=460,y=365)
    st112var = StringVar() 
    st11 = ttk.Combobox(importframe, width = 27, textvariable = st112var )  
    st11['values'] = ('    -NotAssociated-' 
                              )   
    st11.place(x=580,y=365,height=23) 
    st11.current(0)
    st222=Label(importframe,text="SPECIAL TAX 2 = ")
    st222.place(x=460,y=390)
    st222var = StringVar() 
    st22 = ttk.Combobox(importframe, width = 27, textvariable = st222var )
    st22['values'] = ('    -NotAssociated-'
                              )     
    st22.place(x=580,y=390,height=23) 
    st22.current(0)
    vrn2=Label(importframe,text="VAT REG.NUMBER = ")
    vrn2.place(x=460,y=415)
    vrn2var = StringVar() 
    vrn = ttk.Combobox(importframe, width = 27, textvariable = vrn2var ) 
    vrn['values'] = ('    -NotAssociated-' 
                              )     
    vrn.place(x=580,y=415,height=23) 
    vrn.current(0)
    avt2=Label(importframe,text="ACTIVE = ")
    avt2.place(x=460,y=440)
    avt2var = StringVar() 
    avt = ttk.Combobox(importframe, width = 27, textvariable = avt2var )
    avt['values'] = ('    -NotAssociated-'
                              )
    avt.place(x=580,y=440,height=23) 
    avt.current(0)
    tee2=Label(importframe,text="TAX EXEMPTED= ")
    tee2.place(x=460,y=465)
    teevar = StringVar() 
    tee= ttk.Combobox(importframe, width = 27, textvariable = teevar )
    tee['values'] = ('    -NotAssociated-' 
                              ) 
    tee.place(x=580,y=465,height=23) 
    tee.current(0)
    btn=Button(importframe,text="Clear associations", width=15,).place(x=560, y=500)
    btn=Button(importframe, text="Next", width=10,).place(x=685, y=500)     
    top.mainloop()
#-----------------------------------------------------------------------------------Export Customer
def cus_export_customer():
    name = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xslm', '*.xlsx')),('CSV', '*.csv',)])
    if name:
        if name.endswith('.csv'):
            df = pd.read_csv(name)
        else:
            df = pd.read_excel(name)

            filename = name
#-----------------------------------------------------------------------------------Search Customer
def cus_search_customers():
    top = Toplevel()  
    top.title("Find Text")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("520x180+390+250")
    findwhat1=Label(top,text="Find What:")
    findwhat1.place(x=5,y=15)
    n = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = n )
    findwhat.place(x=85,y=15,height=23) 
    findButton = Button(top, text ="Find next",width=10)
    findButton.place(x=420,y=15)
    findin1=Label(top,text="Find in:")
    findin1.place(x=5,y=40)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n )
    findIN['values'] = ('Customer name',  
                              'Customer ID', 
                              'Category', 
                              'Customer name', 
                              'Contact Person', 
                              'Customer Tel.', 
                              'SMS number',
                              'Type',
                              '<<All>>')    
    findIN.place(x=85,y=40,height=23) 
    findIN.current(0)
    closeButton = Button(top, text ="Close",width=10)
    closeButton.place(x=420,y=45)
    match1=Label(top,text="Match:")
    match1.place(x=5,y=65)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
    match['values'] = ('From any part of the field','Whole field',  
                              'From beging of field')
    match.place(x=85,y=65,height=23) 
    match.current(0)
    search1=Label(top,text="Search:")
    search1.place(x=5,y=90)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n )
    search['values'] = ('Up','Down','All') 
    search.place(x=85,y=90,height=23) 
    checkvarStatus4=IntVar()
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button4.place(x=60,y=120)
    checkvarStatus5=IntVar()  
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button5.place(x=270,y=120)
    top.mainloop()
#-----------------------------------------------------------------------------------Refresh Customer
def cus_refresh_customers(self):
    self.destroy()
    self.__init__()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$(((End)))

################################################################################((function For Invoice bottom table))
# #-------------------------------------------------------------------------------bottom tree invoice
def cus_inv_btm():
  
  cus_inv2_s=ttk.Style()
  cus_inv2_s.configure('Treeview.Heading',background='white')
  cus_inv2_tree=ttk.Treeview(tab7,selectmode='browse')
  
  cus_inv2_tree.place(x=0,y=415,height=280)
  cus_inv2_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
  cus_inv2_vertical_bar.place(x=1083,y=415,height=280)
  cus_inv2_tree["columns"]=("1","2","3","4","5","6","7","8","9")
  cus_inv2_tree["show"]='headings'


  cus_inv2_tree.column("1",width=20,anchor='c')
  cus_inv2_tree.column("2",width=140,anchor='c')
  cus_inv2_tree.column("3",width=110,anchor='c')
  cus_inv2_tree.column("4",width=110,anchor='c')
  cus_inv2_tree.column("5",width=120,anchor='c')
  cus_inv2_tree.column("6",width=120,anchor='c')
  cus_inv2_tree.column("7",width=160,anchor='c')
  cus_inv2_tree.column("8",width=160,anchor='c')
  cus_inv2_tree.column("9",width=140,anchor='c')
  cus_inv2_tree.heading("1",text="")
  cus_inv2_tree.heading("2",text="#ID")
  cus_inv2_tree.heading("3",text="Issue Date")
  cus_inv2_tree.heading("4",text="Due Date")
  cus_inv2_tree.heading("5",text="Recurring")
  cus_inv2_tree.heading("6",text="Status")
  cus_inv2_tree.heading("7",text="Invoice Total")
  cus_inv2_tree.heading("8",text="Total Paid")
  cus_inv2_tree.heading("9",text="Balance")
# #-------------------------------------------------------------------------------bottom tree order
def cus_ord_btm():
  cus_ord_s=ttk.Style()
  cus_ord_s.configure('Treeview.Heading',background='white')
  cus_ord_tree=ttk.Treeview(tab7,selectmode='browse')
  cus_ord_tree.place(x=0,y=415,height=280)
  cus_ord_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
  cus_ord_vertical_bar.place(x=1083,y=415,height=280)
  cus_ord_tree["columns"]=("1","2","3","4","5","6","7","8","9")
  cus_ord_tree["show"]='headings'


  cus_ord_tree.column("1",width=20,anchor='c')
  cus_ord_tree.column("2",width=140,anchor='c')
  cus_ord_tree.column("3",width=110,anchor='c')
  cus_ord_tree.column("4",width=110,anchor='c')
  cus_ord_tree.column("5",width=120,anchor='c')
  cus_ord_tree.column("6",width=120,anchor='c')
  cus_ord_tree.column("7",width=160,anchor='c')
  cus_ord_tree.column("8",width=160,anchor='c')
  cus_ord_tree.column("9",width=140,anchor='c')
  cus_ord_tree.heading("1",text="")
  cus_ord_tree.heading("2",text="#ID")
  cus_ord_tree.heading("3",text="Issue Date")
  cus_ord_tree.heading("4",text="Due Date")
  cus_ord_tree.heading("5",text="Emailed on")
  cus_ord_tree.heading("6",text="Print on")
  cus_ord_tree.heading("7",text="Subtotal")
  cus_ord_tree.heading("8",text="Extra Cost")
  cus_ord_tree.heading("9",text="Order Total")
# #-------------------------------------------------------------------------------bottom tree Estimates
def cus_est_btm():
  cus_est_s=ttk.Style()
  cus_est_s.configure('Treeview.Heading',background='white')
  cus_est_tree=ttk.Treeview(tab7,selectmode='browse')
  cus_est_tree.place(x=0,y=415,height=280)
  cus_est_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
  cus_est_vertical_bar.place(x=1083,y=415,height=280)
  cus_est_tree["columns"]=("1","2","3","4","5","6","7","8","9")
  cus_est_tree["show"]='headings'


  cus_est_tree.column("1",width=20,anchor='c')
  cus_est_tree.column("2",width=140,anchor='c')
  cus_est_tree.column("3",width=110,anchor='c')
  cus_est_tree.column("4",width=110,anchor='c')
  cus_est_tree.column("5",width=120,anchor='c')
  cus_est_tree.column("6",width=120,anchor='c')
  cus_est_tree.column("7",width=160,anchor='c')
  cus_est_tree.column("8",width=160,anchor='c')
  cus_est_tree.column("9",width=140,anchor='c')
  cus_est_tree.heading("1",text="")
  cus_est_tree.heading("2",text="#ID")
  cus_est_tree.heading("3",text="Issue Date")
  cus_est_tree.heading("4",text="Due Date")
  cus_est_tree.heading("5",text="Emailed on")
  cus_est_tree.heading("6",text="Print on")
  cus_est_tree.heading("7",text="Subtotal")
  cus_est_tree.heading("8",text="Extra Cost")
  cus_est_tree.heading("9",text="Estimate Total")
# #-------------------------------------------------------------------------------bottom tree statement
def cus_stm_btm():
  cus_stm_s=ttk.Style()
  cus_stm_s.configure('Treeview.Heading',background='white')
  cus_stm_tree=ttk.Treeview(tab7,selectmode='browse')
  cus_stm_tree.place(x=0,y=415,height=280)
  cus_stm_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
  cus_stm_vertical_bar.place(x=1083,y=415,height=280)
  cus_stm_tree["columns"]=("1","2","3","4","5","6","7","8","9")
  cus_stm_tree["show"]='headings'


  cus_stm_tree.column("1",width=20,anchor='c')
  cus_stm_tree.column("2",width=140,anchor='c')
  cus_stm_tree.column("3",width=110,anchor='c')
  cus_stm_tree.column("4",width=110,anchor='c')
  cus_stm_tree.column("5",width=120,anchor='c')
  cus_stm_tree.column("6",width=120,anchor='c')
  cus_stm_tree.column("7",width=160,anchor='c')
  cus_stm_tree.column("8",width=160,anchor='c')
  cus_stm_tree.column("9",width=140,anchor='c')
  cus_stm_tree.heading("1",text="")
  cus_stm_tree.heading("2",text="#ID")
  cus_stm_tree.heading("3",text="Issue Date")
  cus_stm_tree.heading("4",text="Due Date")
  cus_stm_tree.heading("5",text="Recurring")
  cus_stm_tree.heading("6",text="Status")
  cus_stm_tree.heading("7",text="Invoice Total")
  cus_stm_tree.heading("8",text="Total Paid")
  cus_stm_tree.heading("9",text="Balance")
# #-------------------------------------------------------------------------------bottom tree payment
def cus_pym_btm():
  cus_pym_s=ttk.Style()
  cus_pym_s.configure('Treeview.Heading',background='white')
  cus_pym_tree=ttk.Treeview(tab7,selectmode='browse')
  cus_pym_tree.place(x=0,y=415,height=280)
  cus_pym_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
  cus_pym_vertical_bar.place(x=1083,y=415,height=280)
  cus_pym_tree["columns"]=("1","2","3","4","5","6","7")
  cus_pym_tree["show"]='headings'


  cus_pym_tree.column("1",width=20,anchor='c')
  cus_pym_tree.column("2",width=170,anchor='c')
  cus_pym_tree.column("3",width=160,anchor='c')
  cus_pym_tree.column("4",width=110,anchor='c')
  cus_pym_tree.column("5",width=160,anchor='c')
  cus_pym_tree.column("6",width=300,anchor='c')
  cus_pym_tree.column("7",width=160,anchor='c')
  cus_pym_tree.heading("1",text="")
  cus_pym_tree.heading("2",text="Invoice ID")
  cus_pym_tree.heading("3",text="Payment Id")
  cus_pym_tree.heading("4",text="Payment Date")
  cus_pym_tree.heading("5",text="Paid By")
  cus_pym_tree.heading("6",text="Description")
  
  cus_pym_tree.heading("7",text="Amount")
# #-------------------------------------------------------------------------------bottom tree purchase order
def cus_pod_btm():
  cus_por_s=ttk.Style()
  cus_por_s.configure('Treeview.Heading',background='white')
  cus_por_tree=ttk.Treeview(tab7,selectmode='browse')
  cus_por_tree.place(x=0,y=415,height=280)
  cus_por_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
  cus_por_vertical_bar.place(x=1083,y=415,height=280)
  cus_por_tree["columns"]=("1","2","3","4","5","6","7")
  cus_por_tree["show"]='headings'


  cus_por_tree.column("1",width=20,anchor='c')
  cus_por_tree.column("2",width=170,anchor='c')
  cus_por_tree.column("3",width=130,anchor='c')
  cus_por_tree.column("4",width=130,anchor='c')
  cus_por_tree.column("5",width=300,anchor='c')
  cus_por_tree.column("6",width=150,anchor='c')
  cus_por_tree.column("7",width=180,anchor='c')
  cus_por_tree.heading("1",text="")
  cus_por_tree.heading("2",text="ID#")
  cus_por_tree.heading("3",text="Issue Date")
  cus_por_tree.heading("4",text="Due Date")
  cus_por_tree.heading("5",text="Vendor")
  cus_por_tree.heading("6",text="Status")

  cus_por_tree.heading("7",text="P.Order Total")
####################################################################################################################
#----------------------------------------------------------------------------Button bottam table-----
cus_btn=Button(tab7, text="Invoices", width=15, command=lambda:cus_inv_btm())
cus_btn.place(x=7, y=390)
cus_btn=Button(tab7, text="Orders", width=15, command=lambda:cus_ord_btm())
cus_btn.place(x=125, y=390)
cus_btn=Button(tab7, text="Estimates", width=15, command=lambda:cus_est_btm())
cus_btn.place(x=243, y=390)
cus_btn=Button(tab7, text="Statement", width=15, command=lambda:cus_stm_btm())
cus_btn.place(x=361, y=390)
cus_btn=Button(tab7, text="Payments", width=15, command=lambda:cus_pym_btm())
cus_btn.place(x=479,y=390)
cus_btn=Button(tab7, text="Purchase O.", width=15, command=lambda:cus_pod_btm())
cus_btn.place(x=597, y=390)

#-------------------------------------------------------------------------Bottom Table one-------------
cus_inv_s=ttk.Style()
cus_inv_s.configure('Treeview.Heading',background='white')
cus_inv_tree=ttk.Treeview(tab7,selectmode='browse')
cus_inv_tree.place(x=0,y=415,height=280)
cus_inv_vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
cus_inv_vertical_bar.place(x=1083,y=415,height=280)
cus_inv_tree["columns"]=("1","2","3","4","5","6","7","8","9")
cus_inv_tree["show"]='headings'


cus_inv_tree.column("1",width=20,anchor='c')
cus_inv_tree.column("2",width=140,anchor='c')
cus_inv_tree.column("3",width=110,anchor='c')
cus_inv_tree.column("4",width=110,anchor='c')
cus_inv_tree.column("5",width=120,anchor='c')
cus_inv_tree.column("6",width=120,anchor='c')
cus_inv_tree.column("7",width=160,anchor='c')
cus_inv_tree.column("8",width=160,anchor='c')
cus_inv_tree.column("9",width=140,anchor='c')
cus_inv_tree.heading("1",text="")
cus_inv_tree.heading("2",text="#ID")
cus_inv_tree.heading("3",text="Issue Date")
cus_inv_tree.heading("4",text="Due Date")
cus_inv_tree.heading("5",text="Recurring")
cus_inv_tree.heading("6",text="Status")
cus_inv_tree.heading("7",text="Invoice Total")
cus_inv_tree.heading("8",text="Total Paid")
cus_inv_tree.heading("9",text="Balance")

#---------------------------------------------------------------------------------Bottom 
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