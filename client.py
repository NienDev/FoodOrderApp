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
                def back_to_show_image():
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
                
                wrap_frame2 = LabelFrame(frame2)
                wrap_frame2.grid(row=0,column=2)
                
                btn2 = Button(wrap_frame2, command=back_to_show_image, text="x")
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
            
        show_image()
        
def show_welcome(logo, frame, welcome_label, btn):
    global root
    
    
   
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    logo.pack()
    
    welcome_label.pack(pady=(20,40))
    
    btn.pack(pady=(0,20))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #glocal variables
    FOOD_LISTS = []
    LIST_IMG_LABELS = []   
    amount_dic = []
    for i in range(21):
        amount_dic.append(int(0))
    print(amount_dic)

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
    root.geometry("1280x700+0+0")
    
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
    
    show_welcome(LOGO_IMG, FRAME, WELCOME_LABEL, BTN_MENU)
    

    
    root.mainloop()
    
    
except:
    print("error")
    
input()






