import socket 

server = socket.socket(socket.AF_INIT,socket.SOCK_DGRAM)
server.blind(("0.0.0.0",3000))

print("waiting")
msg,addr = server.recvfrom(1024)
print(f"received {addr}: {msg.decode('ascii')}")

server.close()