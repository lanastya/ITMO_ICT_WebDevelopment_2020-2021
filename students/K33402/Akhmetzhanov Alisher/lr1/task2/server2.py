import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    udata = data.decode("utf-8")
    print("Data: " + udata)
    a, b = data.split()

    conn.send(str(math.sqrt(int(a) ** 2 + int(b) ** 2)).encode("UTF-8"))


conn.close()