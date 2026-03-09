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

- Python 3
- TCP Sockets
- Multithreading
- Standard Python libraries only

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

The server uses **multi-threading**.

Each client connection runs in a **separate thread**, allowing the server to handle multiple clients simultaneously.

Example:

```python
threading.Thread(target=handle, args=(client_socket,))
```

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

The server will notify other users.

---

# Testing

The application was tested under the following scenarios:

### Multiple Clients

Multiple clients connected simultaneously and exchanged messages successfully.

### Simultaneous Messaging

Different users sending messages at the same time were handled correctly.

### Client Disconnection

When a client exits or disconnects unexpectedly, the server removes the client and notifies other users.

### Chat History

Users can request previous messages using the `HISTORY` command.

---

# Logging

All events are logged in:

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
