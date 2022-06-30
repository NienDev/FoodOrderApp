ed")

msg = conn.recv(1024).decode(FORMAT)
conn.sendall(msg.encode(FORMAT))
if (msg == "FOOD"):
    #send FOOD LIST
    with open('foodData.json') as f:
        data = json.load(f)
    # print(data)
    food_list = pickle.dumps(data['food'])
    conn.sendall(food_list)
conn.recv(1024) #client finish receiving food_list
sendFile(conn)

with open('orderData.json') as f:
    orderData = json.load(f)

sendClientInfo(orderData, addr)

msg = None
msg = conn.recv(4096)
conn.sendall(msg)
# conn.sendall(msg)
finish_msg = conn.recv(4096).decode(FORMAT)
conn.sendall(finish_msg.encode(FORMAT))
while (finish_msg != "FINISH"):
    # newOrder = conn.recv(4096)
    # if ((msg != "FINISH") and (msg.decode(FORMAT) == "FINISH")):
        # break
    
    newOrder = msg
    newOrder = pickle.loads(newOrder)
    # before append new order, find whether this client have ordered before, if yes delete that order and append this new order
    deleteOrder(orderData, newOrder)
    
    orderData.append(newOrder)
    msg = "DONE"
    conn.sendall(msg.encode(FORMAT))
    
    with open('orderData.json', 'w') as f:
        json.dump(orderData, f, indent=2)
    
    print(orderData)
    msg = conn.recv(4096) #waiting for the next order
    conn.sendall(msg)
    finish_msg = conn.recv(1024).decode(FORMAT)


# msg = None
# while (msg != "FINISH"):
    # msg = recv(1024).decode(FORMAT)
    

# except:
    # print("error")
    
input()
