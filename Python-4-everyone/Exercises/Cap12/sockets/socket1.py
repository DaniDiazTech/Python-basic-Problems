import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(mysock)

print(type(mysock))

mysock.connect(('data.pr4e.org', 80))

print(mysock)
print(type(mysock))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
