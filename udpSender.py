 Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = int(sys.argv[3])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
s.bind((server_address)

while 1:
    if not len(data):
       break
       
    data = sys.stdin.readline().strip()
    data, address = sock.recvfrom(4096)
       
    if data:
       sent = sock.sendto(data, address)
   
    for i in range (1, n + 1):
        data1 = data + "(" + str(i) + ")"
        print ("data sent: " + data)
#       s.sendall(data.encode('utf-8'))
        s.sendto(data1.encode('utf-8'), server_address)
s.shutdown(1)
