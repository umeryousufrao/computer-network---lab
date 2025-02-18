import socket

s = socket.socket()
print("Socket created")
s.bind(('localhost', 9999))
s.listen(5)
print("Waiting for connection")

c, address = s.accept()
print("Got connection from", address)

c.send("Enter your Marks: ".encode())
marks = int(c.recv(1024).decode())
print(f"Client IP: {address} - Marks: {marks}")

if marks >= 90:
    grade = "A+"
elif marks >= 86:
    grade = "A"
elif marks >= 82:
    grade = "A-"
elif marks >= 78:
    grade = "B+"
elif marks >= 74:
    grade = "B"
elif marks >= 70:
    grade = "B-"
elif marks >= 66:
    grade = "C+"
elif marks >= 62:
    grade = "C"
elif marks >= 58:
    grade = "C-"
elif marks >= 54:
    grade = "D+"
elif marks >= 50:
    grade = "D-"
else:
    grade = "F"

c.send(grade.encode())
c.close()
print("Connection closed")

s.close()
print("Server Closed")
