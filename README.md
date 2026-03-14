# 🐍 Simple Python Socket Shell 🌐

This project is a basic **Remote Command Execution** tool built with Python. It allows you to control a client machine remotely via network sockets. 🖥️➡️💻

## ✨ Features

* **Remote Execution:** Send system commands from the Server to the Client. ⚡
* **Persistent Navigation:** Supports `cd` commands to navigate through directories. 📂
* **Robust Feedback:** Captures both successful outputs and error messages. ✅❌
* **Real-time Communication:** Persistent connection for multiple commands. 📡

## 🛠️ Prerequisites

* Python 3.x installed on both machines. 🐍
* Basic knowledge of networking (IPs and Ports). 🌐

## 🚀 How to Run

1. **Start the Server:** 🏃‍♂️
```bash
python server.py

```


*The server will start listening for connections on port 5555.* 👂
2. **Run the Client:** 🎯
On the target machine, execute:
```bash
python client.py

```


3. **Execute Commands:** ⌨️
Once connected, type your commands in the Server terminal:
* `dir` (List files) 📄
* `cd ..` (Go back a folder) 🔙
* `ipconfig` (Network info) 📶
* `exit` (Close connection) 🔌



## ⚠️ Important Safety Notice

This project is for **educational purposes ONLY**. 🎓 Using these tools on computers without explicit permission is **illegal and unethical**. Always test in a controlled, authorized environment! 🛡️
