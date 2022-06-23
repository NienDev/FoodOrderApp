import socket
import pickle
import json

HOST = "127.0.0.1"
PORT = 65432
FORMAT = "utf8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("SERVER SIDE")

server.bind((HOST, PORT))
server.listen()

try:
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
except:
    print("error")
    
input()
