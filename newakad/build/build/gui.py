
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk
import customtkinter

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\newakad\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

qty=0
qty1=0
qty2=0
qty3=0
qty4=0
qty5=0
qty6=0
qty7=0
qty8=0
qty9=0
qty10=0
qty11=0



window = Tk()

window.geometry("1440x1005")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1005,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

#iteam plus
def itemplus():
    global qty
    qty+=1
    my_label.config(text = qty)

def item1plus():
    global qty1
    qty1+=1
    my_label1.config(text = qty1)

def item2plus():
    global qty2
    qty2+=1
    my_label2.config(text = qty2)

def item3plus():
    global qty3
    qty3+=1
    my_label3.config(text = qty3)

def item4plus():
    global qty4
    qty4+=1
    my_label4.config(text = qty4)

def item5plus():
    global qty5
    qty5+=1
    my_label5.config(text = qty5)

def item6plus():
    global qty6
    qty6+=1
    my_label6.config(text = qty6)

def item7plus():
    global qty7
    qty7+=1
    my_label7.config(text = qty7)

def item8plus():
    global qty8
    qty8+=1
    my_label8.config(text = qty8)

def item9plus():
    global qty9
    qty9+=1
    my_label9.config(text = qty9)

def item10plus():
    global qty10
    qty10+=1
    my_label10.config(text = qty10)

def item11plus():
    global qty11
    qty11+=1
    my_label11.config(text = qty11)


#item mins
def itemmins():
    global qty
    if(qty>0):
         qty-=1
    my_label.config(text = qty)
    
def item1mins():
    global qty1
    if(qty1>0):
         qty1-=1
    my_label1.config(text = qty1)

def item2mins():
    global qty2
    if(qty2>0):
         qty2-=1
    my_label2.config(text = qty2)

def item3mins():
    global qty3
    if(qty3>0):
         qty3-=1
    my_label3.config(text = qty3)

def item4mins():
    global qty4
    if(qty4>0):
         qty4-=1
    my_label4.config(text = qty4)

    
def item5mins():
    global qty5
    if(qty5>0):
         qty5-=1
    my_label5.config(text = qty5)

def item6mins():
    global qty6
    if(qty6>0):
         qty6-=1
    my_label6.config(text = qty6)

def item7mins():
    global qty7
    if(qty7>0):
         qty7-=1
    my_label7.config(text = qty7)

def item8mins():
    global qty8
    if(qty8>0):
         qty8-=1
    my_label8.config(text = qty8)

def item9mins():
    global qty9
    if(qty9>0):
         qty9-=1
    my_label9.config(text = qty9)

def item10mins():
    global qty10
    if(qty10>0):
         qty10-=1
    my_label10.config(text = qty10)

def item11mins():
    global qty11
    if(qty11>0):
         qty11-=1
    my_label11.config(text = qty11)
    
#LaBL
my_label= Label(window,text = qty ,font="BOLD 30")
my_label.place(x=121,
    y=270,
    width=50,
    height=50)    
    
my_label1= Label(window,text = qty1 ,font="BOLD 30")
my_label1.place(x=393,
    y=270,
    width=50,
    height=50)    
    
my_label2= Label(window,text = qty2 ,font="BOLD 30")
my_label2.place(x=671,
    y=270,
    width=50,
    height=50)  

my_label3= Label(window,text = qty3 ,font="BOLD 30")
my_label3.place(x=946,
    y=270,
    width=50,
    height=50)  

   
my_label4= Label(window,text = qty4 ,font="BOLD 30")
my_label4.place(x=1248,
    y=274,
    width=50,
    height=50)  

my_label5= Label(window,text = qty5 ,font="BOLD 30")
my_label5.place(x=107,
    y=573,
    width=50,
    height=50)  

my_label6= Label(window,text = qty6,font="BOLD 30")
my_label6.place(x=385,
    y=570,
    width=50,
    height=50)  

my_label7= Label(window,text = qty7,font="BOLD 30")
my_label7.place(x=666,
    y=570,
    width=50,
    height=50)  

my_label8= Label(window,text = qty8,font="BOLD 30")
my_label8.place(x=941,
    y=570,
    width=50,
    height=50)  

my_label9= Label(window,text = qty9,font="BOLD 30")
my_label9.place(x=1249,
    y=570,
    width=50,
    height=50)  

my_label10= Label(window,text = qty10,font="BOLD 30")
my_label10.place(x=1249,
    y=883,
    width=50,
    height=50)  

my_label11= Label(window,text = qty11,font="BOLD 30")
my_label11.place(x=112,
    y=873,
    width=50,
    height=50)  

   
#making a tree
columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")
tree.place(x=284,
    y=635,
    width=846,
    height=267)


#add item
def add_item():
    global qty
    if(qty>0):
         desc = "قصب"
         price = 10
         line_total= qty*price
         invoice_item = [qty, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty,desc,price,line_total)
    
def add_item1():
    global qty1
    if(qty1>0):
         desc = "موز"
         price = 10
         line_total= qty*price
         invoice_item = [qty1, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty1,desc,price,line_total)
    
def add_item2():
    global qty2
    if(qty2>0):
         desc = "بطيخ"
         price = 10
         line_total= qty2*price
         invoice_item = [qty2, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty2,desc,price,line_total)
    
def add_item3():
    global qty3
    if(qty3>0):
         desc = "فراوله"
         price = 10
         line_total= qty3*price
         invoice_item = [qty3, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty3,desc,price,line_total)
    
def add_item4():
    global qty4
    if(qty4>0):
         desc = "مانجا"
         price = 30
         line_total= qty4*price
         invoice_item = [qty4, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty4,desc,price,line_total)
    
def add_item5():
    global qty5
    if(qty5>0):
         desc = "رمان"
         price = 30
         line_total= qty5*price
         invoice_item = [qty5, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty5,desc,price,line_total)
    
def add_item6():
    global qty6
    if(qty6>0):
         desc = "تفاح"
         price = 20
         line_total= qty6*price
         invoice_item = [qty6, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty6,desc,price,line_total)
    


def add_item7():
    global qty7
    if(qty7>0):
         desc = "اناناس"
         price = 35
         line_total= qty7*price
         invoice_item = [qty7, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty7,desc,price,line_total)
    
def add_item8():
    global qty8
    if(qty8>0):
         desc = "دراجون فروت"
         price = 10
         line_total= qty8*price
         invoice_item = [qty8, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty8,desc,price,line_total)
    
def add_item9():
    global qty9
    if(qty9>0):
         desc = "كيوي"
         price = 10
         line_total= qty9*price
         invoice_item = [qty9, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty9,desc,price,line_total)
    
def add_item10():
    global qty10
    if(qty10>0):
         desc = "برتقال"
         price = 10
         line_total= qty10*price
         invoice_item = [qty10, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty10,desc,price,line_total)
    
def add_item11():
    global qty11
    if(qty11>0):
         desc = "لمون"
         price = 10
         line_total= qty11*price
         invoice_item = [qty11, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty11,desc,price,line_total)
    
    
#new_invice
invoice_list = []
def new_invoice():
    tree.delete(*tree.get_children())
    
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = "mahmod"
    phone = "666-666"
    subtotal = sum(item[3] for item in invoice_list) 
    salestax = 0.1
    total = subtotal*(1-salestax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
   
    new_invoice()    

def enter_data(qt,descz,pricez,totalz):
    
    # Create Table
    conn = sqlite3.connect('data1.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS akado_men 
            (qt INT, descz TEXT, pricez FLOAT, totalz FLOAT )
    '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO akado_men (qt, descz, pricez, 
    totalz) VALUES 
    (?, ?, ?,?)'''
    data_insert_tuple = (qt,
                          descz, pricez, totalz)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
 


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    512.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item1(),
    relief="flat"
)
button_1.place(
    x=308.0,
    y=50.0,
    width=216.52166748046875,
    height=200.0
)

canvas.create_text(
    449.0,
    158.0,
    anchor="nw",
    text="20",
    fill="#FFFFFF",
    font=("Taprom Regular", 64 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item10(),
    relief="flat"
)
button_2.place(
    x=33.0,
    y=642.0,
    width=216.52166748046875,
    height=231.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item11(),
    relief="flat"
)
button_3.place(
    x=1166.0,
    y=655.0,
    width=216.52166748046875,
    height=231.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item9(),
    relief="flat"
)
button_4.place(
    x=1161.0,
    y=343.0,
    width=216.52166748046875,
    height=231.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item4(),
    relief="flat"
)
button_5.place(
    x=1152.0,
    y=44.0,
    width=216.52166748046875,
    height=230.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item8(),
    relief="flat"
)
button_6.place(
    x=858.0,
    y=343.0,
    width=216.52166748046875,
    height=230.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item7(),
    relief="flat"
)
button_7.place(
    x=583.0,
    y=349.0,
    width=216.52166748046875,
    height=224.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item6(),
    relief="flat"
)
button_8.place(
    x=308.0,
    y=349.0,
    width=216.52166748046875,
    height=224.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item(),
    relief="flat"
)
button_9.place(
    x=33.0,
    y=50.0,
    width=216.52166748046875,
    height=223.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item2(),
    relief="flat"
)
button_10.place(
    x=583.0,
    y=50.0,
    width=216.52166748046875,
    height=223.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item3(),
    relief="flat"
)
button_11.place(
    x=858.0,
    y=44.0,
    width=216.52166748046875,
    height=226.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item5(),
    relief="flat"
)
button_12.place(
    x=33.0,
    y=349.0,
    width=216.52166748046875,
    height=224.0
)

canvas.create_rectangle(
    1201.0,
    44.0,
    1372.0,
    186.0,
    fill="#FFFFFF",
    outline="")

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemplus(),
    relief="flat"
)
button_13.place(
    x=61.0,
    y=270.0,
    width=50.0,
    height=50.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5plus(),
    relief="flat"
)
button_14.place(
    x=46.0,
    y=571.0,
    width=50.0,
    height=50.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item11plus(),
    relief="flat"
)
button_15.place(
    x=50.0,
    y=870.0,
    width=50.0,
    height=50.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item1plus(),
    relief="flat"
)
button_16.place(
    x=328.0,
    y=271.0,
    width=50.0,
    height=50.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6plus(),
    relief="flat"
)
button_17.place(
    x=328.0,
    y=569.0,
    width=50.0,
    height=50.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2plus(),
    relief="flat"
)
button_18.place(
    x=600.0,
    y=271.0,
    width=50.0,
    height=50.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:item7plus(),
    relief="flat"
)
button_19.place(
    x=604.0,
    y=567.0,
    width=50.0,
    height=50.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3plus(),
    relief="flat"
)
button_20.place(
    x=881.0,
    y=270.0,
    width=50.0,
    height=50.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8plus(),
    relief="flat"
)
button_21.place(
    x=881.0,
    y=571.0,
    width=50.0,
    height=50.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4plus(),
    relief="flat"
)
button_22.place(
    x=1184.0,
    y=274.0,
    width=50.0,
    height=50.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:item9plus(),
    relief="flat"
)
button_23.place(
    x=1184.0,
    y=571.0,
    width=50.0,
    height=50.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item10plus()
)
button_24.place(
    x=1192.0,
    y=882.0,
    width=50.0,
    height=50.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemmins(),
    relief="flat"
)
button_25.place(
    x=181.0,
    y=271.0,
    width=50.0,
    height=50.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5mins(),
    relief="flat"
)
button_26.place(
    x=166.0,
    y=570.0,
    width=50.0,
    height=50.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item11mins(),
    relief="flat"
)
button_27.place(
    x=179.0,
    y=870.0,
    width=50.0,
    height=50.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item1mins(),
    relief="flat"
)
button_28.place(
    x=456.0,
    y=271.0,
    width=50.0,
    height=50.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6mins(),
    relief="flat"
)
button_29.place(
    x=441.0,
    y=570.0,
    width=50.0,
    height=50.0
)

button_image_30 = PhotoImage(
    file=relative_to_assets("button_30.png"))
button_30 = Button(
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item10mins(),
    relief="flat"
)
button_30.place(
    x=1312.0,
    y=883.0,
    width=50.0,
    height=50.0
)

button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
button_31 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2mins(),
    relief="flat"
)
button_31.place(
    x=735.0,
    y=271.0,
    width=50.0,
    height=50.0
)

button_image_32 = PhotoImage(
    file=relative_to_assets("button_32.png"))
button_32 = Button(
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7mins(),
    relief="flat"
)
button_32.place(
    x=720.0,
    y=570.0,
    width=50.0,
    height=50.0
)

button_image_33 = PhotoImage(
    file=relative_to_assets("button_33.png"))
button_33 = Button(
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:item9mins(),
    relief="flat"
)
button_33.place(
    x=1311.0,
    y=571.0,
    width=50.0,
    height=50.0
)

button_image_34 = PhotoImage(
    file=relative_to_assets("button_34.png"))
button_34 = Button(
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3mins(),
    relief="flat"
)
button_34.place(
    x=1012.0,
    y=271.0,
    width=50.0,
    height=50.0
)

button_image_35 = PhotoImage(
    file=relative_to_assets("button_35.png"))
button_35 = Button(
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8mins(),
    relief="flat"
)
button_35.place(
    x=997.0,
    y=570.0,
    width=50.0,
    height=50.0
)

button_image_36 = PhotoImage(
    file=relative_to_assets("button_36.png"))
button_36 = Button(
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4mins(),
    relief="flat"
)
button_36.place(
    x=1304.0,
    y=272.0,
    width=50.0,
    height=50.0
)

button_image_37 = PhotoImage(
    file=relative_to_assets("button_37.png"))
button_37 = Button(
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_invoice(),
    relief="flat"
)
button_37.place(
    x=284.0,
    y=917.0,
    width=407.0,
    height=58.0
)

button_image_38 = PhotoImage(
    file=relative_to_assets("button_38.png"))
button_38 = Button(
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_invoice(),
    relief="flat"
)
button_38.place(
    x=723.0,
    y=917.0,
    width=407.0,
    height=58.0
)

def check():
    if entry_user.get() == 'mahmoud' and entry_pass.get() == "asd":
        LOGIN.destroy()
LOGIN = Frame( window)

# Create a photoimage object of the image in the path
# 1440x950
LOGIN.place(x=0,y=0,width=1512,height=982)
LOGIN.configure(background="white")
LOGIN_IM = Image.open(r"D:\newakad\build\build\assets\frame0\my  app.png")
test_LOGIN = ImageTk.PhotoImage(LOGIN_IM)
LOGOIN = Label(LOGIN,background="white",image=test_LOGIN).place(
    x=0,
    y=0,
    
)






entry_user = customtkinter.CTkEntry(master=LOGIN,
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               
                               width=534,
                               height=56,
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=20)
entry_user.place(x=456,y=501)

entry_pass = customtkinter.CTkEntry(master=LOGIN,
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               width=534,
                               height=56,
                               show="*",
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=20)
entry_pass.place(x=459,y=631)

button_login = customtkinter.CTkButton(master=LOGIN,
                                 #text="LOGIN",
                                 width=530,
                                 height=64,
                                 fg_color=("#1E1E1E","#1E1E1E"),
                                 border_width=0,
                                 corner_radius=40,
                                 text="LOGIN",
                                 command=check)
button_login.place(x=458,y=761)



#LOGO.image = test

w = Frame( window)
# Create a photoimage object of the image in the path
w.place(x=0,y=0,width=1512,height=982)
image1 = Image.open(r"D:\newakad\build\build\assets\frame0\LOGO.png")
test = ImageTk.PhotoImage(image1)
LOGO = Label(w,image=test).pack()
#LOGO.image = test

window.after(2000,lambda:w.destroy())

window.resizable(False, False)
window.mainloop()
