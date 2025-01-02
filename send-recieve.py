import socket

def sent():
    host = socket.gethostname() #get local hostname
    port = 5000 # !!!! port to listen on
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Sender waiting for connection at {host}:{port}")
    conn, address = server_socket.accept()
    print(f"Connection established with: {address}")
    
    while True:
        data = conn.recv(1024).decode()
        if not data: 
            break #exit if no data is recived
        print(f"Reciver: {data}")
        mesage = input("You:") #Input message to reply
        conn.send(message.encode())
    conn.close()

def receive():
    host = input("Enter the sender's IP address: ")  # sender's IP address
    port = 5000  #!!!! port to connect to

    client_socket = socket.socket()
    client_socket.connect((host, port))  #connect to the sender

    while True:
        message = input("You: ") 
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode()
        if not data:
            break  #exit if received
        print(f"Sender: {data}")
    client_socket.close()

if __name__ == "__main__":
    mode = input("Select mode (send/receive): ").strip().lower()
    if mode == "send":
        send()
    elif mode == "receive":
        receive()
    else:
        print("Invalid mode! Please enter 'send' or 'receive'.")

        