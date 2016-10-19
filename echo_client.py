import socket

HOST = '192.168.99.100'  # Symbolic name meaning all available interfaces
R_PORT = 8082              # Arbitrary non-privileged port
S_PORT = 8083
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((HOST, R_PORT))
s.connect((HOST, S_PORT))
print 'Connected'
while 1:
    data = r.recv(1024)
    print data
    s.sendall(data)
s.close()