# Multi-Client Chat Application

A simple **TCP-based multi-client chat application** built using **Python socket programming**.  
The system follows a **client–server architecture** where multiple users can communicate with each other in real time through a central server.

This project was developed as part of a **Computer Networks programming assignment**.

---

# Project Structure

```
chat-app/
│
├── server/
│   └── server.py
│
├── client/
│   └── client.py
│
├── README.md
└── Report.pdf
```

---

# Features

## Server

- Accepts connections from multiple clients
- Maintains a list of connected users
- Broadcasts messages to all users
- Notifies users when someone joins or leaves
- Handles unexpected client disconnections
- Supports up to **10 concurrent clients**
- Logs events in `audit_event.txt`
- Stores chat history

## Client

- Connects to server using **IP address and port**
- Allows user to choose a **username**
- Sends messages to the server
- Receives messages from other users in real time
- Allows user to exit cleanly using `/quit`

---

# Communication Protocol

The system uses a simple **application-layer protocol**.

| Command | Description |
|--------|-------------|
| JOIN <username> | Join chat |
| MSG <message> | Send message |
| USERS | Get list of online users |
| HISTORY | Retrieve chat history |
| QUIT | Leave chat |

### Example

Client joins:

```
JOIN Satyam
```

Client sends message:

```
MSG Hello everyone!
```

Server broadcast:

```
[12:30:45] Satyam: Hello everyone!
```

---

# Technologies Used

- Python
- TCP Sockets

Libraries used:

```
socket
threading
datetime
```

No external networking libraries were used.

---

# System Architecture

The application follows a **client–server architecture**.

```
          Client 1
             │
             │
Client 2 ─── Server ─── Client 3
             │
             │
          Client 4
```

The **server acts as a central hub**, managing communication between all connected clients.

---

# Concurrency Model

The server uses **multi-threading** for sending and getting msgs.

Each client connection runs in a **separate thread**, allowing the server to handle multiple clients simultaneously.

This ensures that communication with one client does not block others.

---

# How to Run the Application

## 1. Start the Server

Open terminal and run:

```bash
python3 server/server.py
```

Output:

```
server waiting for clients...
```

---

## 2. Start a Client

Open another terminal and run:

```bash
python3 client/client.py
```

Enter:

```
Server IP address
Username
```

---

## 3. Start Chatting

Type messages and press enter.

Example:

```
Hello everyone
```

Other users will receive:

```
[12:45:20] Satyam: Hello everyone
```

---

## 4. Exit Chat

Type:

```
/quit
```

## 5. See active users

Type:

```
/users
```

## 6. See history

Type:

```
/history
```

The server will notify other users.

---

# Testing

The application was tested under the following scenarios: Server running with three clients

### Server
```
jk@tp:~/sem6/CN/chat-app$ python3 server/server.py 
host: tp
ip: 127.0.1.1
port: 12345
server waiting for clients...
got conn from ('127.0.0.1', 49138)
Jittu joined chat.
got conn from ('127.0.0.1', 44402)
satyam joined chat.
got conn from ('127.0.0.1', 33126)
sanjay joined chat.
[22:33:18] Jittu: Hii how are you al?👋
[22:33:42] satyam: I am doing great, thank you for asking!
[22:33:43] satyam: 😊
[22:34:08] sanjay: Glay to see you all 😄
sanjay left chat.
satyam left chat.
[22:38:48] Jittu: /usrs
[22:39:02] Jittu: it seems everyone left
[22:39:17] Jittu: ok, I am leaving the text.
Jittu left chat.
```

### Clinet 1 (Sanjay):
```
jk@tp:~/sem6/CN/chat-app$ python3 client/client.py 
type server ip: 127.0.1.1
ur name: sanjay
sanjay joined chat.
[22:33:18] Jittu: Hii how are you al?👋
[22:33:42] satyam: I am doing great, thank you for asking!
[22:33:43] satyam: 😊
Glay to see you all 😄
/history
[22:33:18] Jittu: Hii how are you al?👋
[22:33:42] satyam: I am doing great, thank you for asking!
[22:33:43] satyam: 😊
[22:34:08] sanjay: Glay to see you all 😄
/users
Online users: Jittu, satyam, sanjay
/quit
server gone or smth
jk@tp:~/sem6/CN/chat-app$ 
```

### Clinet 2 (Satyam):
```
jk@tp:~/sem6/CN/chat-app$ python3 client/client.py 
type server ip: 127.0.1.1
ur name: satyam
satyam joined chat.
sanjay joined chat.
[22:33:18] Jittu: Hii how are you al?👋
I am doing great, thank you for asking!
😊
[22:34:08] sanjay: Glay to see you all 😄
sanjay left chat.
/users
Online users: Jittu, satyam
/history
[22:33:18] Jittu: Hii how are you al?👋
[22:33:42] satyam: I am doing great, thank you for asking!
[22:33:43] satyam: 😊
[22:34:08] sanjay: Glay to see you all 😄
/quit
server gone or smth
jk@tp:~/sem6/CN/chat-app$ 
```

### Clinet 3 (Jittu):
```
jk@tp:~/sem6/CN/chat-app$ python3 client/client.py 
type server ip: 127.0.1.1
ur name: Jittu
Jittu joined chat.
satyam joined chat.
sanjay joined chat.
Hii how are you all?👋          
[22:33:42] satyam: I am doing great, thank you for asking!
[22:33:43] satyam: 😊
[22:34:08] sanjay: Glay to see you all 😄
sanjay left chat.
satyam left chat.
/usrs           
/users
Online users: Jittu
it seems everyone left
ok, I am leaving the text.
/quit
server gone or smth
jk@tp:~/sem6/CN/chat-app$ 
```

### Audit Event captured logs:
```
[2026-03-09 22:31:46] Jittu joined
[2026-03-09 22:32:10] satyam joined
[2026-03-09 22:32:24] sanjay joined
[2026-03-09 22:33:18] Jittu msg: Hii how are you al?👋
[2026-03-09 22:33:42] satyam msg: I am doing great, thank you for asking!
[2026-03-09 22:33:43] satyam msg: 😊
[2026-03-09 22:34:08] sanjay msg: Glay to see you all 😄
[2026-03-09 22:37:02] sanjay quit
[2026-03-09 22:38:23] satyam quit
[2026-03-09 22:38:48] Jittu msg: /usrs
[2026-03-09 22:39:02] Jittu msg: it seems everyone left
[2026-03-09 22:39:17] Jittu msg: ok, I am leaving the text.
[2026-03-09 22:39:20] Jittu quit

```

Multiple clients connected simultaneously and exchanged messages successfully.

### Simultaneous Messaging

Different users sending messages at the same time were handled correctly.

### Client Disconnection

When a client exits or disconnects unexpectedly, the server removes the client and notifies other users.

### Chat History

Users can request previous messages using the `HISTORY` command.

---

# Logging

All events are stored in a text file.

```
audit_event.txt
```

Example log:

```
[2026-03-09 19:22:01] Satyam joined
[2026-03-09 19:22:15] Satyam msg: Hello everyone
[2026-03-09 19:25:30] Satyam quit
```

---

# Challenges Faced

- During development, the server sometimes failed to start due to the port already being in use. This was resolved by enabling socket address reuse (SO_REUSEADDR). I’ve taken help from gpt to solve this.
- Log Storage: Initially logs were stored in a list, but the data was lost when the server restarted. Therefore, a text file was used to store logs persistently with timestamps.
- Handling Multiple Clients Simultaneously ensuring Broadcasting Messages reaching Efficiently.

---

# Author

**Jitendra Kumar**  
B.Tech Computer Science  
Sitare University (SRMU)  
