import EchoCommon

HOST=EchoCommon.HOST
PORT=EchoCommon.PORT

def handle_client(sock,addr):
    try:
        msg=EchoCommon.recv_msg(sock)
        print('{}:{}'.format(addr,msg))
        EchoCommon.send_msg(sock,msg)
    except (ConnectionError,BrokenPipeError):
        print('socket error')
    finally:
        print('closed connection to {}'.format(addr))
        sock.close()

if __name__=='__main__':
    listen_sock = EchoCommon.create_listen_socket(HOST,PORT)
    addr=listen_sock.getsockname()
    print('listening on {}'.format(addr))

    while True:
        client_sock,addr=listen_sock.accept()
        print('connection from {}'.format(addr))
        handle_client(client_sock,addr)