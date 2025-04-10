import socket 

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip_add = "192.168.217.61"
port = 1234
complete = (ip_add , port)
message = input("kya aaya ")
encode_msg = message.encoder('ascii')
s.sendto(encode_msg , complete)

