import socket
#192.168.1.20
HOST = "127.0.0.1" #loopback (point to my laptop IP adđress
SERVER_PORT = 65432 # > 50000
FORMAT = "utf8"

def serverChat(conn):
    msg = None
    while msg != "x":
        msg = conn.recv(1024).decode(FORMAT)
        print("Client Message: ", msg)
        msg = input("Server message: ")
        conn.sendall(msg.encode(FORMAT))
        if msg == "list":
            list = recvList(conn)
            print(list)
        
def recvList(conn):
    list = []
    item = conn.recv(1024).decode(FORMAT)
    while (item != "end"):
        list.append(item)
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)
    
    return list
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #declare socket, SOCK_STREAM: TCP protocol, s used to open and host this server and waiting

s.bind((HOST, SERVER_PORT)) # host on my IP ADDRESS
s.listen() #waiting 

print("SERVER SIDE")
print("Server:", HOST, SERVER_PORT)
print("Waiting for client")

#use try ... except means try to connect to something, if something corrupt instead of the error occurs in the terminal, we can skip the try and implement the except
try: 
    conn, addr = s.accept() #when client send message, server accept that message, conn used to send and receive data on connect link, addr is address of client

    print("client address: ", addr)
    print("conn: ", conn.getsockname())

    username = conn.recv(1024).decode(FORMAT)
    conn.sendall(username.encode(FORMAT))
    password = conn.recv(1024).decode(FORMAT)
    print("Username: ", username)
    print("Password: ", password)
    conn.sendall(password.encode(FORMAT))
    
    #simple char in server section
    #serverChat(conn)
    serverChat(conn)
except:
    print("Error")
    
input()