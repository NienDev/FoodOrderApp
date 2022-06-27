import requests
import socket
import json
import pickle
from io import BytesIO
import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

HOST = "127.0.0.1"
PORT = 65432
FORMAT = "utf8"
 
    
    
def download_food_image(Food_Info):
    #create folder
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'food_imgs')
    if not os.path.exists(final_directory):
       os.makedirs(final_directory)
       
       for idx, info in enumerate(Food_Info):
       
        # print(pic_url)
        with open('./food_imgs/pic' + str(idx) + '.jpg', 'wb') as handle:
            response = requests.get(info['url'], stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)       

def show_menu(logo, welcome_label, btn, client, img_labels):
        global root
        global FRAME
        global Food_Info
        global amount_dic
        global totalmoney
        global IS_VALID
        #turn off the show_welcome window
        logo.forget()
        welcome_label.forget()
        btn.forget()
        FRAME.forget()
        
        frame = LabelFrame(root)
        frame.pack(padx=20,pady=20,fill=BOTH,expand=1)
        #show menu
            #create main frame
        main_frame =Frame(frame)
        main_frame.pack(fill=BOTH, expand=1)
            #create  a canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            
            #add a scrollbar to canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        
            #configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))   
            
            #create another frame in canvas
        second_frame = Frame(my_canvas)
            
            #add that new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        
        
        frame1 = LabelFrame(second_frame)
        frame1.grid(row=0, column=0, padx=10, pady=10)
        frame2 = LabelFrame(second_frame)
        frame2.grid(row=0, column=1, padx=10, pady=10)
        frame3 = LabelFrame(second_frame)
        frame3.grid(row=1, column=0, padx=10, pady=10)
        frame4 = LabelFrame(second_frame)
        frame4.grid(row=1, column=1, padx=10, pady=10)
        
        def show_receipt():
            global totalmoney
            pop = Toplevel(root)
            pop.title = "Receipt"
            
            main_label = Label(pop, text="Your Bill")
            main_label.pack()
            
            food_frame = LabelFrame(pop)
            food_frame.pack()
            
            # food 1 
            def remove_order1():
                totalmoney[0] -= amount_dic[1] * int(Food_Info[0]['price'])
                amount_dic[1] = 0
                print(amount_dic)
                food_thumbnail_label1.grid_remove()
                text_label.grid_remove()
                amount_label.grid_remove()
                undo_btn.grid_remove()
                order_frame1.forget()
                
                totalmoney_label.config(text="Total Money: " + str(totalmoney[0]))
                totalmoney_label.pack()
            
            if (amount_dic[1] != 0):
                order_frame1 = LabelFrame(food_frame)
                order_frame1.pack(padx=20, pady=20)
                
                food_thumbnail1 = Image.open("./food_imgs/food1.png")
                food_thumbnail1 = ImageTk.PhotoImage(food_thumbnail1)
                food_thumbnail_label1 = Label(order_frame1, image=food_thumbnail1)
                food_thumbnail_label1.image = food_thumbnail1
                food_thumbnail_label1['image']=food_thumbnail1
                food_thumbnail_label1.grid(row=0, column=0, rowspan=2, padx=20, pady=20)
                
                text_label = Label(order_frame1, text=Food_Info[0]['name'], justify=LEFT, font='Roboto 16 bold')
                text_label.grid(row=0, column=1, columnspan=2, pady=20, sticky="sw")
                
                amount_label = Label(order_frame1, text="Amount: " +  str(amount_dic[1]) + "\nPrice: " + Food_Info[0]['price'], justify=LEFT)
                amount_label.grid(row=1, column=1, pady=20,sticky="nw")
                
                undo_btn = Button(order_frame1, text="UNDO", command=remove_order1)
                undo_btn.grid(row=0, column=3, rowspan=2,sticky="ne", padx=(20,0))
                
            #food 2
            def remove_order2():
                totalmoney[0] -= amount_dic[2] * int(Food_Info[1]['price'])
                amount_dic[2] = 0
                print(amount_dic)
                food_thumbnail_label2.grid_remove()
                text_label2.grid_remove()
                amount_label2.grid_remove()
                undo_btn2.grid_remove()
                order_frame2.forget()
                
                totalmoney_label.config(text="Total Money: " + str(totalmoney[0]))
                totalmoney_label.pack()
            
            if (amount_dic[2] != 0):
                order_frame2 = LabelFrame(food_frame)
                order_frame2.pack(padx=20, pady=20)
                
                food_thumbnail2 = Image.open("./food_imgs/food1.png")
                food_thumbnail2 = ImageTk.PhotoImage(food_thumbnail2)
                food_thumbnail_label2 = Label(order_frame2, image=food_thumbnail2)
                food_thumbnail_label2.image = food_thumbnail2
                food_thumbnail_label2['image']=food_thumbnail2
                food_thumbnail_label2.grid(row=0, column=0, rowspan=2, padx=20, pady=20)
                
                text_label2 = Label(order_frame2, text=Food_Info[1]['name'], justify=LEFT, font='Roboto 16 bold')
                text_label2.grid(row=0, column=1, columnspan=2, pady=20, sticky="sw")
                
                amount_label2 = Label(order_frame2, text="Amount: " +  str(amount_dic[2]) + "\nPrice: " + Food_Info[1]['price'], justify=LEFT)
                amount_label2.grid(row=1, column=1, pady=20,sticky="nw")
                
                undo_btn2 = Button(order_frame2, text="UNDO", command=remove_order2)
                undo_btn2.grid(row=0, column=3, rowspan=2,sticky="ne", padx=(20,0))
            
            
            #total money section
            totalmoney[0] = 0
            for i in range(5):
                totalmoney[0] += amount_dic[i+1] * int(Food_Info[i]['price'])
            
            totalmoney_label = Label(pop, text="Total Money: " + str(totalmoney[0]))
            totalmoney_label.pack(side=LEFT, fill = BOTH, expand = True)
            
            def show_thank_window():
                thanks_window = Toplevel(root)
                thanks_window.title = "Finish ordering"
                thanks_window.geometry("200x200")
                label = Label(thanks_window, text="Thank you, enjoy your meal")
                label.pack()
                
                # take off all the widget of show receipt and show menu
                pop.destroy()
                pop.update()
                frame.forget()
                show_welcome()
                
            def show_invalid():
                thanks_window = Toplevel(root)
                thanks_window.title = "INVALID"
                thanks_window.geometry("200x200")
                label = Label(thanks_window, text="Your number is INVALID")
                label.pack()
            
                
            def paid():
                def checkCreditNumber(e):
                    number = str(e.get())
                    if (len(number) == 10) and (number.isdigit()):
                        IS_VALID[0] = True
                        show_thank_window()
                        credit_window.destroy()
                        STATE[0] = True
                    else:
                        show_invalid()
            
                if (cash.get() == 1):
                    show_thank_window()
                else:
                    credit_window =  Toplevel(root)
                    credit_window.title = "Pay by credit card"
                    credit_window.geometry("200x200")
                    e = Entry(credit_window, text="your card NUMBER", width=15)
                    e.pack()
                    credit_btn = Button(credit_window, text="Confirm", command=lambda: checkCreditNumber(e))
                    credit_btn.pack()
            
            cash = IntVar()
            credit = IntVar()
            paid_cash = Checkbutton(pop, text="Paid by cash", variable=cash)
            paid_credit = Checkbutton(pop, text="Paid by credit card", variable=credit)
            paid_cash.pack(side=LEFT)
            paid_credit.pack(side=LEFT)
            confirm_btn = Button(pop, text="Confirm", command=paid)
            confirm_btn.pack()
            
        img_cart = Image.open("./food_imgs/cart.png")
        img_cart = ImageTk.PhotoImage(img_cart)
        btn_show_receipt = Button(second_frame, command=show_receipt)
        btn_show_receipt.image = img_cart
        btn_show_receipt['image']=img_cart
        btn_show_receipt.grid(row=2, column=0, columnspan=4, padx=20, pady=20)
        
        def show_image():
            
            row1=0
            col1=0
     
            #image 1
            def show_food_description1():
                def back_to_show_image():
                    name_label1.grid_remove()
                    description_label1.grid_remove()
                    btn1.grid_remove()
                    amount1.grid_remove()
                    order_btn1.grid_remove()
                    wrap_frame1.grid_remove()
                
                def order1():
                    amount_dic[1] += int(amount1.get())
                    print(amount_dic)
                    back_to_show_image()
                
                wrap_frame1 = LabelFrame(frame1)
                wrap_frame1.grid(row=0,column=1)
                
                btn1 = Button(wrap_frame1, command=back_to_show_image, text="x")
                btn1.grid(row=0, column=1, padx=10, pady=10)
                
             
        
                food_name1 = Food_Info[0]['name']
                food_description1 = Food_Info[0]['description']
                name_label1 = Label(wrap_frame1, text=food_name1, font='Roboto 16 bold',wraplength=200)
                description_label1 = Label(wrap_frame1, wraplength=200 ,text=food_description1, justify=LEFT) 
                
                name_label1.grid(row=1, column=0, pady=20, padx=20)
                description_label1.grid(row=2, column=0,  pady=20)
                
                amount1 = Entry(wrap_frame1, width=10, borderwidth=4)
                amount1.insert(0, "Quantity")
                amount1.grid(row=3,column=0, pady=20)
                
                order_btn1 = Button(wrap_frame1, text="Order", command=order1)
                order_btn1.grid(row=3, column=1, padx=10)
            
            #image 2
            def show_food_description2():
                def back_to_show_image2():
                    name_label2.grid_remove()
                    description_label2.grid_remove()
                    btn2.grid_remove()
                    amount2.grid_remove()
                    order_btn2.grid_remove()
                    wrap_frame2.grid_remove()
                    # show_image()
            
                # btn_img2.grid_remove()
                def order2():
                    amount_dic[2] += int(amount2.get())
                    print(amount_dic)
                    back_to_show_image2()
                
                wrap_frame2 = LabelFrame(frame2)
                wrap_frame2.grid(row=0,column=2)
                
                btn2 = Button(wrap_frame2, command=back_to_show_image2, text="x")
                btn2.grid(row=0, column=1, padx=10, pady=10)
                
             
        
                food_name2 = Food_Info[1]['name']
                food_description2 = Food_Info[1]['description']
                name_label2 = Label(wrap_frame2, text=food_name2, font='Roboto 16 bold',wraplength=200)
                description_label2 = Label(wrap_frame2, wraplength=200 ,text=food_description2, justify=LEFT) 
                
                name_label2.grid(row=1, column=0, pady=20, padx=20)
                description_label2.grid(row=2, column=0,  pady=20)
                
                amount2 = Entry(wrap_frame2, width=10, borderwidth=4)
                amount2.insert(0, "Quantity")
                amount2.grid(row=3,column=0, pady=20)
                
                order_btn2 = Button(wrap_frame2, text="Order", command=order2)
                order_btn2.grid(row=3, column=1, padx=10)
            
            #image 3
            def show_food_description3():
                def back_to_show_image():
                    name_label3.grid_remove()
                    description_label3.grid_remove()
                    btn3.grid_remove()
                    amount3.grid_remove()
                    order_btn3.grid_remove()
                    wrap_frame3.grid_remove()
                
                def order3():
                    amount_dic[3] += int(amount3.get())
                    print(amount_dic)
                    back_to_show_image()
                    
                wrap_frame3 = LabelFrame(frame3)
                wrap_frame3.grid(row=0,column=2)
                
                btn3 = Button(wrap_frame3, command=back_to_show_image, text="x")
                btn3.grid(row=0, column=1, padx=10, pady=10)
                
             
        
                food_name3 = Food_Info[2]['name']
                food_description3 = Food_Info[2]['description']
                name_label3 = Label(wrap_frame3, text=food_name3, font='Roboto 16 bold',wraplength=200)
                description_label3 = Label(wrap_frame3, wraplength=200 ,text=food_description3, justify=LEFT) 
                
                name_label3.grid(row=1, column=0, pady=20, padx=20)
                description_label3.grid(row=2, column=0,  pady=20)
                
                amount3 = Entry(wrap_frame3, width=10, borderwidth=4)
                amount3.insert(0, "Quantity")
                amount3.grid(row=3,column=0, pady=20)
                
                order_btn3 = Button(wrap_frame3, text="Order", command=order3)
                order_btn3.grid(row=3, column=1, padx=10)
            
            #image 4
            def show_food_description4():
                def back_to_show_image():
                    name_label4.grid_remove()
                    description_label4.grid_remove()
                    btn4.grid_remove()
                    amount4.grid_remove()
                    order_btn4.grid_remove()
                    wrap_frame4.grid_remove()
                
                def order4():
                    amount_dic[4] += int(amount4.get())
                    print(amount_dic)
                    back_to_show_image()
                
                wrap_frame4 = LabelFrame(frame4)
                wrap_frame4.grid(row=0,column=2)
                
                btn4 = Button(wrap_frame4, command=back_to_show_image, text="x")
                btn4.grid(row=0, column=1, padx=10, pady=10)
                
             
        
                food_name4 = Food_Info[3]['name']
                food_description4 = Food_Info[3]['description']
                name_label4 = Label(wrap_frame4, text=food_name4, font='Roboto 16 bold',wraplength=200)
                description_label4 = Label(wrap_frame4, wraplength=200 ,text=food_description4, justify=LEFT) 
                
                name_label4.grid(row=1, column=0, pady=20, padx=20)
                description_label4.grid(row=2, column=0,  pady=20)
                
                amount4 = Entry(wrap_frame4, width=10, borderwidth=4)
                amount4.insert(0, "Quantity")
                amount4.grid(row=3,column=0, pady=20)
                
                order_btn4 = Button(wrap_frame4, text="Order", command=order4)
                order_btn4.grid(row=3, column=1, padx=10)
            
            img1 = Image.open("./food_imgs/pic" + str(0) + ".jpg")
            img1.thumbnail((800,400))
            img1.save("./food_imgs/p" + str(0) + ".jpg")
            img1 = Image.open("./food_imgs/p" + str(0) + ".jpg")
            img1 = ImageTk.PhotoImage(img1)
            
            btn_img1 = Button(frame1, command=lambda: show_food_description1())
            btn_img1.image = img1
            btn_img1['image']=img1
            btn_img1.grid(row=0, column=0, padx=20, pady=20)
            
            img2 = Image.open("./food_imgs/pic" + str(0) + ".jpg")
            img2.thumbnail((800,400))
            img2.save("./food_imgs/p" + str(0) + ".jpg")
            img2 = Image.open("./food_imgs/p" + str(0) + ".jpg")
            img2 = ImageTk.PhotoImage(img2)
            
            btn_img2 = Button(frame2, command=lambda: show_food_description2())
            btn_img2.image = img2
            btn_img2['image']=img2
            btn_img2.grid(row=0, column=1, padx=20, pady=20)
            
            img3 = Image.open("./food_imgs/pic" + str(0) + ".jpg")
            img3.thumbnail((800,400))
            img3.save("./food_imgs/p" + str(0) + ".jpg")
            img3 = Image.open("./food_imgs/p" + str(0) + ".jpg")
            img3 = ImageTk.PhotoImage(img3)
            
            btn_img3 = Button(frame3, command=lambda: show_food_description3())
            btn_img3.image = img3
            btn_img3['image']=img3
            btn_img3.grid(row=0, column=0, padx=20, pady=20)
            
            img4 = Image.open("./food_imgs/pic" + str(0) + ".jpg")
            img4.thumbnail((800,400))
            img4.save("./food_imgs/p" + str(0) + ".jpg")
            img4 = Image.open("./food_imgs/p" + str(0) + ".jpg")
            img4 = ImageTk.PhotoImage(img4)
             
            btn_img4 = Button(frame4, command=lambda: show_food_description4())
            btn_img4.image = img4
            btn_img4['image']=img4
            btn_img4.grid(row=0, column=0, padx=20, pady=20)
            
        show_image()
        
def show_welcome():
    global root

    FRAME.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    LOGO_IMG.pack()
    
    WELCOME_LABEL.pack(pady=(20,40))
    
    BTN_MENU.pack(pady=(0,20))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #glocal variables
    FOOD_LISTS = []
    LIST_IMG_LABELS = []   
    amount_dic = []
    totalmoney = []
    totalmoney.append(int(0))
    for i in range(21):
        amount_dic.append(int(0))
    print(amount_dic)
    STATE = []
    STATE.append(False) # false is pay by cash, true is pay by credit
    IS_VALID = []
    IS_VALID.append(False)

    client.connect((HOST, PORT))
    msg = "FOOD"
    client.sendall(msg.encode(FORMAT))
    client.recv(1024)
    #receive food info from server
    Food_Info = client.recv(4096)
    Food_Info = pickle.loads(Food_Info)
    FOOD_LISTS.append(Food_Info)
    download_food_image(Food_Info)

    root = Tk()
    root.option_add( "*font", "Roboto") #set default font
    root.title("FOOD ORDER APP")
    root.iconbitmap("icon.ico")
    root.geometry("1360x700+0+0")
    
    #widgets
    FRAME = LabelFrame(root, padx=20, pady=20)
    LOGO = ImageTk.PhotoImage(Image.open("logo.png"))
    LOGO_IMG = Label(FRAME, image=LOGO)
    WELCOME_LABEL = Label(FRAME, text="Welcome to NNP Restaurant", font=("Roboto", 20, "bold"))
    BTN_MENU = Button(FRAME, text="Show Food Menu", padx=20,pady=10, command=lambda: show_menu(LOGO_IMG, WELCOME_LABEL, BTN_MENU, client, IMG_LABELS))
    IMG_LABELS = []

    
    # img = ImageTk.PhotoImage(Image.open())
    # label = Label(FRAME, image=img)
    # IMG_LABELS.append(label)
    # IMG_LABELS[0].pack()
    
    # welcome
    
    show_welcome()
    

    
    root.mainloop()
    print(STATE)
    
except:
    print("error")
    
input()





