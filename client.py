import socket

HOST = "127.0.0.1" #loopback (point to my laptop IP adđress
SERVER_PORT = 65432 # > 50000
FORMAT = "utf8" 

def clientChat(client):
    list = ["nien", "kim", "tran"]
    msg = None
    while msg != "x":
        msg = input("message: ")
        client.sendall(msg.encode(FORMAT))
        msg = client.recv(1024).decode(FORMAT)
        print("server message: ", msg)
        if (msg == "list"): 
            sendList(list, client)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("CLIENT SIDE")

def sendList(list, client):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)
        
    #finish sending
    msg = "end"
    client.sendall(msg.encode(FORMAT))

try:
    client.connect((HOST, SERVER_PORT)) #connect to server you want to
    print("client address: ", client.getsockname())

    username = input("username: ")
    password = input("password: ")

    client.sendall(username.encode(FORMAT)) #because the data send has the type of byte so you need to encode
    client.recv(1024) #receive message from server, this line of code use to make sure that the above message successfully send to the server before sending the other one
    client.sendall(password.encode(FORMAT))
    client.recv(1024)
    
    #simple chat in client section
    #clientChat(client)
    
    #how to send a list from client to server
    clientChat(client)
    
    #python threading (lap trinh da luong)
    
except:
    print("Error")

input()