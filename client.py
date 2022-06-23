import requests
import socket
import json
import pickle
from io import BytesIO
import os
from tkinter import *
from PIL import ImageTk, Image

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
        #turn off the show_welcome window
        logo.forget()
        welcome_label.forget()
        btn.forget()
        
        #show menu
        for idx in range(5):
            img = Image.open("./food_imgs/pic" + str(idx) + ".jpg")
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            label = Button(FRAME)
            label.image = img
            label['image']=img
            label.pack() 
    
def show_welcome(logo, frame, welcome_label, btn):
    global root
    
    
   
    frame.pack(padx=50, pady=50)
    
    logo.pack()
    
    welcome_label.pack(pady=(20,40))
    
    btn.pack(pady=(0,20))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    #glocal variables
    FOOD_LISTS = []
    LIST_IMG_LABELS = []

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
    
    
    
    #widgets
    FRAME = LabelFrame(root, padx=50, pady=10)
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
    
    root.eval('tk::PlaceWindow . center')
    
    root.mainloop()
    
    
except:
    print("error")
    
input()







