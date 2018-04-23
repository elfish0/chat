import sys,socket
import EchoCommon

HOST=sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT=EchoCommon.PORT

if __name__=='__main__':
    while True:
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((HOST,PORT))
            print('\nconnected to {}:{}'.format(HOST,PORT))
            print("type message,enter to send,'q' to quit" )
            msg=input()
            if msg=='q':break
            EchoCommon.send_msg(sock,msg)
            print('sent message:{}'.format(msg))
            msg=EchoCommon.recv_msg(sock)
            print('received echo :'+msg)
        except ConnectionError:
            print('socket error')
            break
        finally:
            sock.close()
            print('closed connection to server\n')