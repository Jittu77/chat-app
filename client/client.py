import socket
import threading

# port number
port = 12345

# get server ip from user
ip = input("type server ip: ")

# make socket for client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
s.connect((ip, port))

# get username
uname = input("ur name: ")

# tell server who i am
s.send(("JOIN " + uname).encode())

# function to get msgs from server
def getmsgs():
    while True:
        try:
            m = s.recv(1024).decode()
            if m:
                print(m)
        except:
            print("server gone or smth")
            s.close()
            break

# function to send msgs to server
def sendmsgs():
    while True:
        m = input()
        if m == "/quit":
            s.send(b"QUIT")
            s.close()
            break
        elif m == "/users":
            s.send(b"USERS")
        elif m == "/history":
            s.send(b"HISTORY")
        elif m.strip() != "":
            s.send(("MSG " + m).encode())

# make threads for both
t1 = threading.Thread(target=getmsgs)
t1.start()
t2 = threading.Thread(target=sendmsgs)
t2.start()