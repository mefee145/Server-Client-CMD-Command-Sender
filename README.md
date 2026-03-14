```markdown
# Simple Python Socket Shell

This project is a basic Remote Shell implementation using Python sockets. It allows a Server to send system commands to a Client, which executes them and returns the output.

## Features
- **Remote Command Execution:** Execute system commands (e.g., `dir`, `ipconfig`, `whoami`) on the client machine from the server.
- **Directory Navigation:** Supports `cd` commands to change directories persistently on the client machine.
- **Real-time Feedback:** Captures both standard output (`stdout`) and errors (`stderr`), sending them back to the server.
- **Persistent Connection:** The server can keep the connection open and send multiple commands sequentially.

## Prerequisites
- Python 3.x installed on both machines.
- The `socket` and `subprocess` modules (built-in).

## How to Run

1. **Start the Server:**
   Run the `server.py` script on your machine:
   ```bash
   python server.py

```

The server will start listening for connections on port 5555.

2. **Run the Client:**
On the target machine, run the `client.py` script:
```bash
python client.py

```


3. **Execute Commands:**
Once connected, you can type commands in the server terminal, such as:
* `dir`
* `cd ..`
* `ipconfig`
* `exit` (to close the connection)



## Safety Notice

This project is for **educational purposes only**. Using these tools on computers you do not own is illegal and unethical. Ensure you are testing within a controlled, authorized environment.

```

---

### Nasıl Kullanacaksın?
1. Proje klasöründe **`README.md`** adında bir dosya oluştur.
2. Yukarıdaki metni kopyalayıp içine yapıştır ve kaydet.
3. GitHub'a yüklediğinde bu dosya otomatik olarak deponun ana sayfasında proje açıklaması olarak görünecektir.

Bu metni kendine göre özelleştirebilirsin. Başka bir özellik (örneğin dosya indirme/yükleme) eklemek istersen, onu da dokümantasyona ekleyebiliriz. Başka bir isteğin var mı?

```
