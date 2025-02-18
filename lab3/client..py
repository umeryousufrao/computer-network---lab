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

# Client Code
def client():
    s = socket.socket()
    s.connect(('localhost', 1000))
    print("Connected to the server.")
    
    while True:
        message = input("Client: ")
        s.send(message.encode())
        save_chat(message, "Client")
        
        if message.lower() == 'exit':
            break
        
        response = s.recv(1024).decode()
        if response.lower() == 'exit':
            print("Server disconnected.")
            break
        print("Server:", response)
        save_chat(response, "Server")
    
    s.close()

if __name__ == "__main__":
    client()