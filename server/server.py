import socket
import os
import pickle
import json

HOST = "127.0.0.1"
PORT = 65432
FORMAT = "utf8"

def sendFile(conn):
    msg = "FOLDER"
    conn.sendall(msg.encode(FORMAT))
    conn.recv(1024)

    imgs = ["./imgs/thumbnail_banhmi.jpg", "./imgs/thumbnail_bo.jpg", "./imgs/thumbnail_bundau.jpg", "./imgs/thumbnail_banhdau.jpg", "./imgs/thumbnail_comcari.jpg", "./imgs/thumbnail_comga.jpg", "./imgs/thumbnail_dimsum.jpg", "./imgs/thumbnail_goicuon.jpg", "./imgs/thumbnail_mochi.jpg", "./imgs/thumbnail_saladucga.jpg", "./imgs/banhmi.jpg", "./imgs/bo.jpg", "./imgs/bundau.jpg", "./imgs/banhdau.jpg", "./imgs/comcari.jpg", "./imgs/comga.jpg", "./imgs/dimsum.jpg", "./imgs/goicuon.jpg", "./imgs/mochi.jpg", "./imgs/saladucga.jpg", "./imgs/cart.png", "./imgs/icon.ico"]
    n = str(len(imgs))
    conn.sendall(n.encode(FORMAT))
    for img in imgs:
        f = open(img, "rb")
        size_img = os.path.getsize(img)
        conn.sendall(str(size_img).encode(FORMAT))
        # print(size_img)
        data = f.read(size_img)
        print("sending", img, "to client")
        conn.sendall(data)
        print("finish sending", img, "to client")
        f.close()
        
        conn.recv(1024)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("SERVER SIDE")

server.bind((HOST, PORT))
server.listen()

# try:
conn, addr = server.accept()
print("client", addr, "has joined")

msg = conn.recv(1024).decode(FORMAT)
conn.sendall(msg.encode(FORMAT))
if (msg == "FOOD"):
    #send FOOD LIST
    with open('foodData.json') as f:
        data = json.load(f)
    print(data)
    food_list = pickle.dumps(data['food'])
    conn.sendall(food_list)
conn.recv(1024) #client finish receiving food_list
sendFile(conn)
# except:
    # print("error")
    
input()
