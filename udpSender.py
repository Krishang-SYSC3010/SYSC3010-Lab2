Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

test = ('localhost', 1007)
s.bind((test)
       
while 1:
    data = sys.stdin.readline().strip()
    if not len(data):
       break
    for i in range (1, n + 1)
       data = "Message " + str(i)
    #  s.sendall(data.encode('utf-8'))
       s.sendto(data1.encode('utf-8'), server_address)
    if data:
       data, address = sock.recvfrom(port)
s.shutdown(1)
