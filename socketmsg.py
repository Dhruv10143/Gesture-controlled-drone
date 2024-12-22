import socket
msgFromClient = 'Howdy132'
bytesToSend = msgFromClient.encode('utf-8')
serverAddress = ('192.168.239.155',2222)
bufferSize = 409600000
UDPClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def msg(msg) :
    # cmd=input('Enter String or Char')
    msg=msg.encode('utf-8')
    UDPClient.sendto(msg, serverAddress)
    print("Message Gone")
    data,address = UDPClient.recvfrom(bufferSize)
    data = data.decode('utf-8')
    print('Data from Server',data)
    print('server IP Address:',address[0])
    print('Server Port:',address[1])
    print('bufferSize',bufferSize)
    del data

msg("9")