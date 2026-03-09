import socket
import threading
from datetime import datetime

# get host info
hn = socket.gethostname()
ip = socket.gethostbyname(hn)

# listen on all
h = "0.0.0.0"
p = 12345

print("host:", hn)
print("ip:", ip)
print("port:", p)


# lists for clients and names
clis = []
names = {}
# history: {username: [[time, message], ...]}
history = {}

# log events to file audit_event.txt
def audit_event(username, event, message=""):
    with open("audit_event.txt", "a") as f:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if event == "joined":
            f.write(f"[{t}] {username} joined\n")
        elif event == "quit":
            f.write(f"[{t}] {username} quit\n")
        elif event == "msg":
            f.write(f"[{t}] {username} msg: {message}\n")

# send msg to all
def sendall(msg, notme=None):
    for c in clis:
        if c != notme:
            try:
                c.send(msg.encode())
            except:
                rmv_cli(c)

# remove client
def rmv_cli(c):
    if c in clis:
        n = names.get(c, "???")
        clis.remove(c)
        names.pop(c, None)
        c.close()
        m = n + " left chat."
        print(m)
        sendall(m)
        audit_event(n, "quit")

# handle client
def handle(c):
    try:
        j = c.recv(1024).decode()
        if j.startswith("JOIN"):
            n = j.split(" ", 1)[1]
            names[c] = n
            clis.append(c)
            if n not in history:
                history[n] = []
            m = n + " joined chat."
            print(m)
            sendall(m)
            audit_event(n, "joined")

        while True:
            m = c.recv(1024).decode()
            if not m:
                rmv_cli(c)
                break
            if m.startswith("MSG"):
                t = m.split(" ", 1)[1]
                ts = datetime.now().strftime("%H:%M:%S")
                f = "["+ts+"] "+names[c]+": "+t
                print(f)
                sendall(f, notme=c)
                # store in history
                uname = names[c]
                if uname not in history:
                    history[uname] = []
                history[uname].append([ts, t])
                audit_event(uname, "msg", t)

            elif m == "USERS":
                ul = ", ".join(names.values())
                c.send(("Online users: "+ul).encode())

            elif m == "HISTORY":
                # Show all users' message history
                all_msgs = []
                for uname, msgs in history.items():
                    for msg in msgs:
                        all_msgs.append(f"[{msg[0]}] {uname}: {msg[1]}")
                if not all_msgs:
                    c.send(b"No history found.")
                else:
                    c.send(("\n".join(all_msgs)).encode())
            elif m.startswith("QUIT"):
                rmv_cli(c)
                break
    except:
        rmv_cli(c)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((h, p))
    s.listen(10)
    print("server waiting for clients...")
    while True:
        cs, addr = s.accept()
        print("got conn from", addr)
        t = threading.Thread(target=handle, args=(cs,))
        t.start()
