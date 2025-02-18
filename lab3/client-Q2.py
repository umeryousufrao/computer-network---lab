import socket

c = socket.socket()
c.connect(('localhost', 9999))
msg = c.recv(1024).decode()
print(msg, end='')
marks = input()
c.send(marks.encode())
grade = c.recv(1024).decode()
print(f"Your grade is: {grade}")

c.close()
