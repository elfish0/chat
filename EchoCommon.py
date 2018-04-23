# 通用模块
import socket

HOST = ''
PORT = 4040

def create_listen_socket(HOST, PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(100)
    return sock

def recv_msg(sock):
    data =bytearray()
    msg = ''
    while not msg:
        recvd = sock.recv(4096)
        if not recvd:
            raise  ConnectionError()
        data = data + recvd
        if b'\0' in recvd:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def prep_msg(msg):
    msg += '\0'
    return msg.encode('utf-8')

def send_msg(sock, msg):
    data = prep_msg(msg)
    sock.sendall(data)
