import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b'Thank you for connecting')  # Encode the string to bytes
    # Or use: c.send('Thank you for connecting'.encode('utf-8'))
    c.close()