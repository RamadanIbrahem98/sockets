import socket
from datetime import datetime

class TCPClient:
    ''' A simple TCP Client that uses IPv4 '''

    def __init__(self, host, port):
        self.host = host        # host address
        self.port = port        # host port
        self.conn_sock = None   # connection socket

    def printwt(self, msg):
        ''' Print message with current date and time '''

        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_date_time}] {msg}')

    def create_socket(self):
        ''' Create a socket that uses IPv4 and TCP '''

        self.printwt('Creating connection socket ...')
        self.conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_sock.settimeout(100)

        self.printwt('Socket created')

    def interact_with_server(self , clientMessage):
        ''' Connect and interact with a TCP Server. '''

        try:
            # connect to server
            self.printwt(f'Connecting to server [{self.host}] on port [{self.port}] ...')
            self.conn_sock.connect((self.host, self.port))

            # send data
            self.printwt('Sending name to server to get phone number ...')
            self.conn_sock.sendall(clientMessage.encode('utf-8'))
            self.printwt('[ SENT ]')
            print('\n', clientMessage, '\n')

            # receive data
            resp = self.conn_sock.recv(1024)
            self.printwt('[ RECEIVED ]')
            print('\n', resp.decode(), '\n')
            self.printwt('Interaction completed successfully...')
            return resp.decode()

        except OSError as err:
            self.printwt('Cannot connect to server')
            print(err)

        finally:
            # close socket
            self.printwt('Closing connection socket...')
            self.conn_sock.close()
            self.printwt('Socket closed')

