import socket

# Server Setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()
print("! Made By HebeleKedi !\n")
print("Server is listening...")

# Establish connection
conn, addr = server.accept()
print(f"Connected to {addr}")

# Transaction loop
try:
    while True:
        # Input the Commands
        command = input(">>> ")
        # Sending Commands
        conn.sendall(command.encode("utf-8").strip())

        # Getting Results
        data = conn.recv(4096)
        if data:
            decoded_data = data.decode("utf-8", errors="replace")
            print(decoded_data)
        
        # Exit condition
        if command.lower() == "exit":
            print("Closing connection...")
            break

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    conn.close()
    server.close()