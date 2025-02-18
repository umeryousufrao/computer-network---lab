import socket
import json

# Function to store chat messages in a JSON file
def save_chat(message, sender):
    chat_log = []
    file_name = "chat_history.json"
    
    try:
        with open(file_name, "r") as file:
            chat_log = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # File doesn't exist or is empty
    
    chat_log.append({"sender": sender, "message": message})
    
    with open(file_name, "w") as file:
        json.dump(chat_log, file, indent=4)

# Server Code
def server():
    s = socket.socket()
    s.bind(('localhost', 1000))
    s.listen(5)
    print("Waiting for a connection...")
    
    c, addr = s.accept()
    print("Connected to", addr)
    
    while True:
        data = c.recv(1024).decode()
        if data.lower() == 'exit':
            print("Client disconnected.")
            break
        print("Client:", data)
        save_chat(data, "Client")
        
        reply = input("Server: ")
        c.send(reply.encode())
        save_chat(reply, "Server")
        
        if reply.lower() == 'exit':
            break
    
    c.close()
    s.close()

if __name__ == "__main__":
    server()


